"""
Service Stripe : création de sessions Checkout + gestion webhooks.
"""
import os
import stripe
from fastapi import HTTPException

# Configuration (lue depuis .env au démarrage du backend)
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

STRIPE_PRICE_STARTER = os.environ.get("STRIPE_PRICE_STARTER")
STRIPE_PRICE_PRO = os.environ.get("STRIPE_PRICE_PRO")

PLAN_PRICES = {
    "starter": STRIPE_PRICE_STARTER,
    "pro": STRIPE_PRICE_PRO,
}


def create_checkout_session(tenant, plan: str, success_url: str, cancel_url: str) -> str:
    if plan not in PLAN_PRICES:
        raise HTTPException(status_code=400, detail=f"Plan invalide : {plan}")

    price_id = PLAN_PRICES[plan]
    if not price_id:
        raise HTTPException(status_code=500, detail="Price ID Stripe non configuré")

    try:
        session = stripe.checkout.Session.create(
            mode="subscription",
            payment_method_types=["card"],
            line_items=[{"price": price_id, "quantity": 1}],
            success_url=success_url,
            cancel_url=cancel_url,
            client_reference_id=str(tenant.id),
            metadata={
                "tenant_id": str(tenant.id),
                "plan": plan,
            },
            allow_promotion_codes=True,
        )
        return session.url
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur Stripe : {str(e)}")


def construct_webhook_event(payload: bytes, sig_header: str):
    """
    Vérifie la signature Stripe et retourne l'événement.
    """
    webhook_secret = os.environ.get("STRIPE_WEBHOOK_SECRET")
    if not webhook_secret:
        raise HTTPException(status_code=500, detail="Webhook secret non configuré")

    try:
        return stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Payload invalide : {e}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Signature invalide : {e}")