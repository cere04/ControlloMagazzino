from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from datetime import datetime
from ..entities.articolo import Articolo
from ..entities.enums import TipologiaArticolo, GenereArticolo


class IArticoloRepository(ABC):

    @abstractmethod
    def aggiungi_articolo(self, articolo: Articolo) -> bool:
        """Aggiunge un nuovo articolo al database"""
        pass

    @abstractmethod
    def modifica_articolo(self, articolo: Articolo) -> bool:
        """Modifica un articolo esistente"""
        pass

    @abstractmethod
    def elimina_articolo(self, sku: str) -> bool:
        """Elimina un articolo dal database"""
        pass

    @abstractmethod
    def get_articolo_by_sku(self, sku: str) -> Optional[Articolo]:
        """Recupera un articolo tramite SKU"""
        pass

    @abstractmethod
    def get_articoli(self, filtri: Optional[Dict] = None) -> List[Articolo]:
        """Recupera articoli in base ai filtri"""
        pass

    @abstractmethod
    def cerca_articoli(self, termine: str) -> List[Articolo]:
        """Cerca articoli per nome o descrizione"""
        pass

    @abstractmethod
    def get_articoli_per_tipologia(self, tipologia: TipologiaArticolo) -> List[Articolo]:
        """Recupera articoli per tipologia"""
        pass

    @abstractmethod
    def get_articoli_per_genere(self, genere: GenereArticolo) -> List[Articolo]:
        """Recupera articoli per genere"""
        pass

    @abstractmethod
    def aggiorna_giacenza(self, sku: str, quantita: int) -> bool:
        """Aggiorna la quantità disponibile di un articolo"""
        pass

    @abstractmethod
    def articolo_esiste(self, sku: str) -> bool:
        """Verifica se un articolo esiste"""
        pass