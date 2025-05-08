from .enums import RuoloUtente
from abc import abstractmethod, ABC

#è giusto creare la classe astratta così?
class Utente(ABC):
    def __init__(self,
                 nome: str,
                 cognome: str,
                 codiceDipendente: str,
                 livelloAccesso: RuoloUtente
                 ):
        self.nome = nome
        self.cognome = cognome
        self.codiceDipendente = codiceDipendente
        self.livelloAccesso = livelloAccesso

    @abstractmethod
    def metodoAstratto(self):
        pass


class Admin(Utente):
    def __init__(self,
                 nome : str,
                 cognome : str,
                 codiceDipendente : str
    ):
        super().__init__(nome, cognome, codiceDipendente, RuoloUtente.ADMIN)


class ResponsabileCommerciale(Utente):
    def __init__(self,
                 nome:str,
                 cognome:str,
                 codiceDipendente:str
                 ):
        super().__init__(nome, cognome, codiceDipendente, RuoloUtente.RESPONSABILE_COMMERCIALE)


# -------------------------------------------------------------------------------------------------
# chiedere se serve inserire la generalizzazione anche sull'implementazione per questa sottoclasse
# -------------------------------------------------------------------------------------------------


# class Operatore(Utente):
#     def __init__(self,
#                  nome:str,
#                  cognome:str,
#                  codiceDipendente:str
#                  ):
#         super().__init__(nome, cognome, codiceDipendente, RuoloUtente.OPERATORE)

class Commesso(Utente):
    def __init__(self,
                 nome:str,
                 cognome:str,
                 codiceDipendente:str
                 ):
        super().__init__(nome, cognome, codiceDipendente, RuoloUtente.COMMESSO)

class Magazziniere(Utente):
    def __init__(self,
                 nome:str,
                 cognome:str,
                 codiceDipendente:str
                 ):
        super().__init__(nome, cognome, codiceDipendente, RuoloUtente.MAGAZZINIERE)









