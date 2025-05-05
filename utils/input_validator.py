import re
from datetime import datetime, date
from typing import Optional, Union
from ..entities.enums import TipologiaArticolo, GenereArticolo, RuoloUtente

class InputValidator:
    @staticmethod
    def valida_sku(sku: str) -> bool:
        """Valida il formato di uno SKU (es. AB12345)"""
        return bool(re.match(r'^[A-Z]{2}\d{5}$', sku))

    @staticmethod
    def valida_nome_articolo(nome: str) -> bool:
        """Valida il nome di un articolo"""
        return 2 <= len(nome) <= 50

    @staticmethod
    def valida_quantita(quantita: Union[int, float]) -> bool:
        """Valida che la quantità sia positiva"""
        return quantita > 0

    @staticmethod
    def valida_data(data_str: str) -> Optional[date]:
        """Converte e valida una data in formato YYYY-MM-DD"""
        try:
            return datetime.strptime(data_str, '%Y-%m-%d').date()
        except ValueError:
            return None

    @staticmethod
    def valida_zona(zona: str) -> bool:
        """Valida una zona di magazzino o vendita"""
        return 1 <= len(zona) <= 20

    @staticmethod
    def valida_nome_utente(nome: str) -> bool:
        """Valida nome e cognome utente"""
        return 2 <= len(nome) <= 30

    @staticmethod
    def valida_codice_utente(codice: str) -> bool:
        """Valida il codice utente (es. EMP001)"""
        return bool(re.match(r'^EMP\d{3}$', codice))

    @staticmethod
    def valida_tipologia(tipologia: str) -> bool:
        """Valida che la tipologia sia tra quelle consentite"""
        return tipologia in [t.value for t in TipologiaArticolo]

    @staticmethod
    def valida_genere(genere: str) -> bool:
        """Valida che il genere sia tra quelli consentiti"""
        return genere in [g.value for g in GenereArticolo]

    @staticmethod
    def valida_ruolo(ruolo: str) -> bool:
        """Valida che il ruolo sia tra quelli consentiti"""
        return ruolo in [r.value for r in RuoloUtente]

    @staticmethod
    def genera_codice_utente(ultimo_id: int) -> str:
        """Genera un nuovo codice utente (EMP + 3 cifre)"""
        return f"EMP{ultimo_id:03d}"

    @staticmethod
    def pulisci_input(testo: str) -> str:
        """Pulisce l'input da spazi bianchi e caratteri speciali"""
        return re.sub(r'[^\w\s-]', '', testo).strip()