from entities.enums import RuoloUtente
from entities.utente import Utente, get_utente_by_id, letturaDatabaseUtenti


class AuthService:

    def loginUtente(self, id) -> bool:
        """Esegue il login con il codice dipendente"""
        # utente = self.utente.get_utente_by_id(id)
        lista_utenti=letturaDatabaseUtenti("../Model/databaseUtenti.txt")
        utente= get_utente_by_id(id, lista_utenti)

        if utente:
            return utente
        else:
            return None
        #return("Utente non trovato")

    def logout(self) -> None:
        """Esegue il logout dell'utente corrente"""
        self.utente_corrente = None

    def creaUtente(self, nome: str, cognome: str, ruolo: RuoloUtente, creato_da: Utente) -> Utente:
        pass
        # """Crea un nuovo utente (solo per admin)"""
        # if not SecurityUtils.verifica_ruolo(creato_da, RuoloUtente.ADMIN):
        #     raise PermessoNegatoException("Solo l'amministratore può creare utenti")
        #
        # # Genera un codice dipendente unico
        # ultimo_id = self.utente_repository.get_ultimo_id() or 0
        # codice_dipendente = InputValidator.genera_codice_utente(ultimo_id + 1)
        #
        # utente = Utente(
        #     id=0,  # Sarà generato dal repository
        #     nome=nome,
        #     cognome=cognome,
        #     codice_dipendente=codice_dipendente,
        #     ruolo=ruolo
        # )

        # if self.utente_repository.aggiungi_utente(utente):
        #     return utente
        # raise Exception("Impossibile creare l'utente")

    def verificaLivelloAccesso(self, ruolo_richiesto: RuoloUtente) -> bool:
        pass
        """Verifica se l'utente corrente ha i permessi richiesti"""
        # return SecurityUtils.verifica_ruolo(self.utente_corrente, ruolo_richiesto)

    def aggiungiUtenti(self,nome, cognome, ruolo ) -> bool:
        """Aggiunge un nuovo utente al sistema"""
        with open ("../Model/databaseUtenti.txt", "r") as  file1:
            n = 1
            for riga in file1 :
                n +=1
                if not riga:
                    continue

        cu = nome[0] + '.' + cognome + str(n) + ruolo[0]
        #print(cu)
        with open ("../Model/databaseUtenti.txt", "a") as file:
            file.write(f"\n{nome}, {cognome}, {ruolo}, {cu}")
        return cu



#test metodi

# lista_utenti=letturaDatabaseUtenti("../Model/databaseUtenti.txt")
utente=AuthService()
prova=utente.loginUtente("m.rossi1M")
print(prova)