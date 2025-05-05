import hashlib
import secrets
from typing import Optional
from ..entities.utente import Utente
from ..entities.enums import RuoloUtente

class SecurityUtils:
    # In un'implementazione reale, questi dovrebbero essere in configurazione
    DEFAULT_PASSWORD_LENGTH = 8
    SALT_LENGTH = 16

    @staticmethod
    def verifica_ruolo(utente: Optional[Utente], ruolo_richiesto: RuoloUtente) -> bool:
        """Verifica se l'utente ha il ruolo richiesto"""
        if not utente:
            return False
        # L'admin ha accesso a tutto
        if utente.ruolo == RuoloUtente.ADMIN:
            return True
        return utente.ruolo == ruolo_richiesto