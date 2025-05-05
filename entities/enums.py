from enum import Enum

class TipologiaArticolo(Enum):
    CALZATURE = "Calzature"
    BORSE = "Borse"
    ABBIGLIAMENTO = "Capi d'abbigliamento"

class GenereArticolo(Enum):
    UOMO = "Uomo"
    DONNA = "Donna"
    UNISEX = "Unisex"

class UnitaMisura(Enum):
    PEZZI = "Pezzi"
    PAIA = "Paia"

class RuoloUtente(Enum):
    COMMESSO = "Commesso"
    MAGAZZINIERE = "Magazziniere"
    ADMIN = "Amministratore"
    RESPONSABILE_COMMERCIALE = "Responsabile Commerciale"

class TipoOperazione(Enum):
    VENDITA = "Vendita"
    GIACENZA = "Giacenza"