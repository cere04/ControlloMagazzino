from enums import TipologiaArticolo, GenereArticolo, UnitaMisura


class Articolo:
    # costruttore
    def __init__(self,
                 sku: str,
                 tipologia: TipologiaArticolo,
                 genere: GenereArticolo
                 ):
        self.sku = sku
        self.tipologia = tipologia
        self.genere = genere

    def aggiungiArticolo(self):
        with open("db\databaseArticoli.txt", "a", encoding="utf-8") as file:
            file.write(f"{self.sku}, {self.genere}, {self.tipologia}\n")

articolo = Articolo("999ZZ", "Calzatura", "Donna")
articolo.aggiungiArticolo()


#Articolo1 = Articolo('stringa' , )
    #def modificaArticolo(self):
       # pass

    #def eliminaArticolo(self):
       # pass

   # def get_articolo_by_sku(self):
       # """Recupera un articolo tramite SKU"""
       # pass
