"""
Gestionnaire de connexions WebSocket pour le broadcast temps réel.
"""
import json
from typing import Set

from fastapi import WebSocket


class ConnectionManager:
    """Gère toutes les connexions WebSocket actives."""

    def __init__(self):
        self.active: Set[WebSocket] = set()

    async def connect(self, ws: WebSocket) -> None:
        """Accepte et enregistre une nouvelle connexion."""
        await ws.accept()
        self.active.add(ws)

    def disconnect(self, ws: WebSocket) -> None:
        """Retire une connexion de la liste."""
        self.active.discard(ws)

    async def broadcast(self, payload: dict) -> None:
        """Envoie un message à TOUS les clients connectés.
        Nettoie automatiquement les connexions mortes."""
        dead = []
        for ws in self.active:
            try:
                await ws.send_text(json.dumps(payload))
            except Exception:
                dead.append(ws)
        for ws in dead:
            self.disconnect(ws)


# Instance globale utilisée par les routers et la background loop
manager = ConnectionManager()