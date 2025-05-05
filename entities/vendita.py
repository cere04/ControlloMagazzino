from datetime import datetime
from typing import Optional
from .operazione import Operazione
from .enums import TipoOperazione
from .articolo import Articolo
from .utente import Utente


class Vendita(Operazione):
    def __init__(self,
                 id: int,
                 articolo: Articolo,
                 quantita: float,
                 utente: Utente,
                 paese_vendita: str,
                 ):
        super().__init__(
            id=id,
            tipo=TipoOperazione.VENDITA,
            articolo=articolo,
            quantita=quantita,
            utente=utente,
        )

        self.paese_vendita = paese_vendita

    def __repr__(self):
        return f"Vendita(id={self.id}, articolo={self.articolo.sku}, " \
               f"quantita={self.quantita}, data={self.data}, " \
               f"utente={self.utente.email}, paese_vendita='{self.paese_vendita}', " \
               f"zona_vendita='{self.zona_vendita}')"