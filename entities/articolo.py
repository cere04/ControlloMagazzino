from .enums import TipologiaArticolo, GenereArticolo, UnitaMisura


class Articolo:
    # costruttore
    def __init__(self,
                 sku: str,
                 nome: str,
                 tipologia: TipologiaArticolo,
                 genere: GenereArticolo,
                 unita_misura: UnitaMisura,
                 ):
        self.sku = sku
        self.nome = nome
        self.tipologia = tipologia
        self.genere = genere
        self.unita_misura = unita_misura

    def __repr__(self):
        return f"Articolo(sku={self.sku}, nome='{self.nome}', tipologia={self.tipologia}, " \
               f"genere={self.genere}, unita_misura={self.unita_misura})"