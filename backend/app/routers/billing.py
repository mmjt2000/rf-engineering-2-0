"""
Routes Stripe : checkout + webhook.
"""
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_tenant
from app.models.tenant import Tenant
from app.services.stripe_service import (
    create_checkout_session,
    construct_webhook_event,
)

router = APIRouter(prefix="/api/billing", tags=["billing"])

@router.post("/webhook")
async def webhook(request: Request, db: Session = Depends(get_db)):
    """
    Reçoit les événements Stripe.
    """
    import traceback
    import logging
    logger = logging.getLogger("uvicorn.error")

    payload = await request.body()
    sig_header = request.headers.get("stripe-signature", "")

    logger.info(f"WEBHOOK received: sig_header len={len(sig_header)}, payload len={len(payload)}")

    try:
        event = construct_webhook_event(payload, sig_header)
    except Exception as e:
        logger.error(f"WEBHOOK construct_error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=400, detail=f"Construct error: {e}")

    try:
        event_type = event["type"]
        data = event["data"]["object"]
        logger.info(f"WEBHOOK type={event_type}")

        if event_type == "checkout.session.completed":
            data_dict = data.to_dict() if hasattr(data, "to_dict") else dict(data)
            metadata = data_dict.get("metadata") or {}
            if hasattr(metadata, "to_dict"):
                metadata = metadata.to_dict()
            tenant_id = metadata.get("tenant_id") or data_dict.get("client_reference_id")
            plan = metadata.get("plan")
            logger.info(f"WEBHOOK tenant_id={tenant_id} plan={plan}")

            if tenant_id and plan:
                tenant = db.query(Tenant).filter(Tenant.id == int(tenant_id)).first()
                logger.info(f"WEBHOOK tenant found: {tenant}")
                if tenant:
                    tenant.plan = plan
                    db.commit()
                    logger.info(f"WEBHOOK plan updated to {plan}")

        elif event_type == "customer.subscription.deleted":
            data_dict = data.to_dict() if hasattr(data, "to_dict") else dict(data)
            customer_id = data_dict.get("customer")
            tenant = db.query(Tenant).filter(Tenant.stripe_customer_id == customer_id).first()
            if tenant:
                tenant.plan = "trial"
                tenant.stripe_customer_id = None
                db.commit()

        return {"status": "ok"}

    except Exception as e:
        logger.error(f"WEBHOOK processing_error: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Processing error: {e}")
@router.post("/checkout")
def checkout(
    payload: dict,
    tenant=Depends(get_current_tenant),
    db: Session = Depends(get_db),
):
    """
    Crée une session Stripe Checkout et retourne l'URL de redirection.
    Body attendu : { "plan": "starter" | "pro" }
    """
    plan = (payload or {}).get("plan", "").lower()
    if plan not in ("starter", "pro"):
        raise HTTPException(status_code=400, detail="Plan doit être 'starter' ou 'pro'")

    # URLs de retour (à adapter si tu as un domaine plus tard)
    base_url = "http://127.0.0.1:8000"
    success_url = f"{base_url}/billing.html?checkout=success"
    cancel_url = f"{base_url}/billing.html?checkout=cancel"

    url = create_checkout_session(tenant, plan, success_url, cancel_url)
    return {"checkout_url": url}


