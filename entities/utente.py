from entities.enums import RuoloUtente
from abc import abstractmethod, ABC
from typing import List, Dict, Any

# from .operazione import letturaDatabaseArticoli

def letturaDatabaseUtenti(nome_file: str)-> List[Dict[str, str]]:

    lista_utenti=[]

    try:
        with open(nome_file, 'r') as file:
            n = 0
            for riga in file :
                riga = riga.strip()
                if not riga:
                    continue

                campi=[campo.strip() for campo in riga.split(',')]
                if len(campi)!=4:
                    continue

                lista_utenti.append({
                    'nome': campi[0],
                    'cognome': campi[1],
                    'ruoloUtente': campi[2],
                    'id': campi[3]
                })
    except ValueError as e:
        print(f"Errore conversione dati nella linea {riga}: {e}")
    except Exception as e:
        print(f"Errore durante la lettura del file articoli: {e}")

    return lista_utenti

def get_utente_by_id(id: str, lista_utenti: List[Dict[str, Any]]) -> dict[str, Any] | None:
    for utente in lista_utenti:
        if utente['id'] == id:
            return utente
    return None







    # def bottoneCliccato (self) :
    #     nome = self.Label1.text()
    #     cognome = self.Label2.text()
    #     ruolo = self.label3.currentText()
    # #NCR  = [nome , cognome , ruolo]
    # #LDA = PW.text()
    # print(nome + ' ' + cognome + ' ' + ruolo)
    # with open ("FilePassword.txt", "r") as  file1:
    #     n = 0
    #     for riga in file1 :
    #         ID = riga.split( )
    #         if nome == ID[0] and cognome == ID[1] and ruolo == ID[2]:
    #             n +=1
    # CU = nome[0:3] + cognome[0:3] + ruolo[0] + str(n)
    # print(CU)
    # with open ("File_ID.txt", "a") as file2:
    #     file2.write(f"\n{CU}")
    # with open ( "FilePassword.txt", "a") as file:
    #     file.write(f"\n{nome } {cognome } {ruolo}")

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


#test metodi

lista_utenti=letturaDatabaseUtenti("../Model/databaseUtenti.txt")
# print(lista_utenti)






