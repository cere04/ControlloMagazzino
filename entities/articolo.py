from datetime import datetime
from typing import Optional, List
from .enums import TipologiaArticolo, GenereArticolo, UnitaMisura


class Articolo: #dovremmo aggiungere () anche se non c'è una superclasse
    # qui dovremmo mettere gli attributi con ambito di classe (cioè attributi che non cambiano per ogni istanza) mentre con init mettimao gli attributi con ambito di istanza
    def __init__(self,  #l'init è il costruttore e serve per istanziare la classe
                 sku: str,
                 nome: str,
                 tipologia: TipologiaArticolo,
                 genere: GenereArticolo,
                 unita_misura: UnitaMisura,
                 ):
        self.sku = sku #attributi dell'stanza
        self.nome = nome #da levare(?)
        self.tipologia = tipologia
        self.genere = genere
        self.unita_misura = unita_misura #serve?

    def __repr__(self):
        return f"Articolo(sku={self.sku}, nome='{self.nome}', tipologia={self.tipologia}, " \
               f"genere={self.genere}, unita_misura={self.unita_misura})"

    #rename è necessaria?
    # con la funzione print(Articolo_1.__dict__) restituisce i valori degli attributi dell'oggetto Articolo_1