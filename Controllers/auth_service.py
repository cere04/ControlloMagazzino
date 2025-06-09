from entities.utente import Utente, get_utente_by_id, letturaDatabaseUtenti

class AuthService:

    def loginUtente(self, id) -> bool:
        """Esegue il login con il codice dipendente"""
        lista_utenti=letturaDatabaseUtenti("Model/databaseUtenti.txt")
        utente= get_utente_by_id(id, lista_utenti)

        if utente:
            return utente
        else:
            return None

    def aggiungiUtenti(self,nome, cognome, ruolo ) -> bool:
        """Aggiunge un nuovo utente al sistema"""
        if nome == '' or cognome == '':
            return  True
        else:
            with open ("Model/databaseUtenti.txt", "r") as  file1:
                n = 1
                for riga in file1 :
                    n +=1
                    if not riga:
                        continue

            cu = nome[0] + '.' + cognome + str(n) + ruolo[0]
            with open ("Model/databaseUtenti.txt", "a") as file:
                file.write(f"\n{nome}, {cognome}, {ruolo}, {cu}")
                return cu