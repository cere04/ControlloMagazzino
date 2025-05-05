from abc import ABC, abstractmethod
from typing import Optional, List
from ..entities.utente import Utente
from ..entities.enums import RuoloUtente


class IUtenteRepository(ABC):

    @abstractmethod
    def aggiungi_utente(self, utente: Utente) -> bool:
        """Aggiunge un nuovo utente al sistema"""
        pass

    @abstractmethod
    def modifica_utente(self, utente: Utente) -> bool:
        """Modifica un utente esistente"""
        pass

    @abstractmethod
    def disattiva_utente(self, user_id: int) -> bool:
        """Disattiva un utente"""
        pass

    @abstractmethod
    def verifica_credenziali(self, email: str, password_hash: str) -> Optional[Utente]:
        """Verifica le credenziali di accesso"""
        pass


    @abstractmethod
    def email_esistente(self, email: str) -> bool:
        """Verifica se un'email è già registrata"""
        pass

    @abstractmethod
    def codice_dipendente_esistente(self, codice: str) -> bool:
        """Verifica se un codice dipendente è già registrato"""
        pass