from typing import List, Optional
from ..entities.articolo import Articolo
from ..repositories.articolo_repository import IArticoloRepository
# from ..exceptions import ArticoloNonTrovatoException, PermessoNegatoException
from ..entities.enums import RuoloUtente


class ArticoloService:
    def __init__(self, articolo_repository: IArticoloRepository, auth_service: AuthService):
        self.articolo_repository = articolo_repository
        self.auth_service = auth_service

    def aggiungi_articolo(self, articolo: Articolo) -> bool:
        """Aggiunge un nuovo articolo (solo per admin)"""
        if not self.auth_service.verifica_permessi(RuoloUtente.ADMIN):
            raise PermessoNegatoException("Solo l'amministratore può aggiungere articoli")

        if self.articolo_repository.articolo_esiste(articolo.sku):
            return False

        return self.articolo_repository.aggiungi_articolo(articolo)

    def modifica_articolo(self, articolo: Articolo) -> bool:
        """Modifica un articolo esistente (solo per admin)"""
        if not self.auth_service.verifica_permessi(RuoloUtente.ADMIN):
            raise PermessoNegatoException("Solo l'amministratore può modificare articoli")

        if not self.articolo_repository.articolo_esiste(articolo.sku):
            raise ArticoloNonTrovatoException(f"Articolo con SKU {articolo.sku} non trovato")

        return self.articolo_repository.modifica_articolo(articolo)

    def elimina_articolo(self, sku: str) -> bool:
        """Elimina un articolo (solo per admin)"""
        if not self.auth_service.verifica_permessi(RuoloUtente.ADMIN):
            raise PermessoNegatoException("Solo l'amministratore può eliminare articoli")

        if not self.articolo_repository.articolo_esiste(sku):
            raise ArticoloNonTrovatoException(f"Articolo con SKU {sku} non trovato")

        return self.articolo_repository.elimina_articolo(sku)

    def get_articolo(self, sku: str) -> Optional[Articolo]:
        """Recupera un articolo per SKU"""
        return self.articolo_repository.get_articolo_by_sku(sku)

    def cerca_articoli(self, termine: str) -> List[Articolo]:
        """Cerca articoli per nome o descrizione"""
        return self.articolo_repository.cerca_articoli(termine)

    def get_giacenza_articolo(self, sku: str) -> int:
        """Recupera la giacenza attuale di un articolo"""
        articolo = self.get_articolo(sku)
        if not articolo:
            raise ArticoloNonTrovatoException(f"Articolo con SKU {sku} non trovato")

        giacenza = self.articolo_repository.get_giacenza_articolo(sku)
        return giacenza.quantita if giacenza else 0