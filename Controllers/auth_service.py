from entities.enums import RuoloUtente
from entities.utente import Utente


class AuthService:

    def login(self, codice_dipendente: str) -> bool:
        """Esegue il login con il codice dipendente"""
        utente = self.utente_repository.get_utente_by_codice(codice_dipendente)

        if utente and utente.attivo:
            self.utente_corrente = utente
            self.utente_repository.aggiorna_ultimo_accesso(utente.id)
            return True
        return False

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

    def aggiungiDbUtenti(self, utente: Utente) -> bool:
        """Aggiunge un nuovo utente al sistema"""
        pass