from datetime import datetime
from typing import Optional
from .enums import RuoloUtente


class Utente:
    def __init__(self,
                 id: int,
                 nome: str,
                 cognome: str,
                 codice_dipendente: str,
                 ruolo: RuoloUtente,
                 ):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.codice_dipendente = codice_dipendente
        self.ruolo = ruolo

    def __repr__(self):
        return f"Utente(id={self.id}, nome='{self.nome}', cognome='{self.cognome}', " \
               f"codice='{self.codice_dipendente}', ruolo={self.ruolo})"