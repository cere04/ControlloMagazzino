from datetime import datetime
from typing import Optional
from .enums import TipoOperazione
from .articolo import Articolo
from .utente import Utente


class Operazione:
    def __init__(self,
                 id: int,
                 tipo: TipoOperazione,
                 articolo: Articolo,
                 quantita: float,
                 utente: Utente
                 ):

        self.id = id
        self.tipo = tipo
        self.articolo = articolo
        self.quantita = quantita
        self.utente = utente

    def __repr__(self):
        return f"Operazione(id={self.id}, tipo={self.tipo}, articolo={self.articolo.sku}, " \
               f"quantita={self.quantita}, data={self.data}, utente={self.utente.email})"