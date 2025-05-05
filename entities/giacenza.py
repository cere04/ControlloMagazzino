from datetime import datetime
from typing import Optional
from .operazione import Operazione
from .enums import TipoOperazione
from .articolo import Articolo
from .utente import Utente


class Giacenza(Operazione):
    def __init__(self,
                 id: int,
                 articolo: Articolo,
                 quantita: float,
                 utente: Utente
                 ):
        super().__init__(
            id=id,
            tipo=TipoOperazione.GIACENZA,
            articolo=articolo,
            quantita=quantita,
            utente=utente
        )

    def __repr__(self):
        return f"Giacenza(id={self.id}, articolo={self.articolo.sku}, " \
               f"quantita={self.quantita}, data={self.data}, " \
               f"utente={self.utente.email}, zona_magazzino='{self.zona_magazzino}')"