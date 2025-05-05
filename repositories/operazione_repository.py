from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from datetime import datetime, date
from ..entities.operazione import Operazione
from ..entities.giacenza import Giacenza
from ..entities.vendita import Vendita
from ..entities.enums import TipoOperazione


class IOperazioneRepository(ABC):

    @abstractmethod
    def aggiungi_operazione(self, operazione: Operazione) -> bool:
        """Aggiunge una nuova operazione"""
        pass

    @abstractmethod
    def modifica_operazione(self, operazione: Operazione) -> bool:
        """Modifica un'operazione esistente"""
        pass

    @abstractmethod
    def get_operazione_by_id(self, id: int) -> Optional[Operazione]:
        """Recupera un'operazione tramite ID"""
        pass

    @abstractmethod
    def get_giacenze_attuali(self) -> List[Giacenza]:
        """Recupera le giacenze attuali"""
        pass

    @abstractmethod
    def get_giacenza_articolo(self, sku: str) -> Optional[Giacenza]:
        """Recupera la giacenza attuale di un articolo"""
        pass