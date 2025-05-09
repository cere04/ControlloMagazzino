import os
from datetime import datetime
from .enums import TipoOperazione
from .articolo import Articolo
from typing import List, Dict, Any


def letturaDatabaseArticoli(nome_file: str) -> List[Dict[str, str]]:
    """
    Legge il file databaseArticoli.txt e restituisce una lista di dizionari

    Args:
        nome_file: percorso del file da leggere

    Returns:
        Lista di dizionari con i dati degli articoli
    """
    lista_articoli = []

    try:
        with open(nome_file, 'r') as file:
            for linea in file:
                linea = linea.strip()
                if not linea:
                    continue

                campi = [campo.strip() for campo in linea.split(',')]
                if len(campi) != 3:
                    continue

                lista_articoli.append({
                    'sku': campi[0],
                    'genere': campi[1],
                    'tipologia': campi[2]
                })

    except ValueError as e:
        print(f"Errore conversione dati nella linea {linea}: {e}")
    except Exception as e:
        print(f"Errore durante la lettura del file articoli: {e}")

    return lista_articoli


def letturaDatabaseOperazioni(nome_file: str) -> List[Dict[str, any]]:
    """
    Legge il file di database e restituisce una lista di dizionari con i dati

    Args:
        nome_file: percorso del file da leggere

    Returns:
        Lista di dizionari con i dati delle operazioni
    """
    lista_operazioni = []

    # Verifica se il file esiste
    if not os.path.exists(nome_file):
        print(f"Errore: il file {nome_file} non esiste")
        return lista_operazioni

    try:
        with open(nome_file, 'r') as file:
            for linea in file:
                # Pulisci la linea e salta se vuota
                linea = linea.strip("\n")
                if not linea:
                    continue

                # Dividi i campi
                try:
                    campi = [campo.strip() for campo in linea.split(',')]

                    # Verifica che ci siano tutti i campi necessari
                    if len(campi) != 6:
                        print(f"Errore formato nella linea: {linea}")
                        continue

                    # Estrai e converti i campi
                    operazione = {
                        'sku': campi[0],
                        'vendita': int(campi[1]),
                        'giacenza': int(campi[2]),
                        'paese': campi[3],
                        'data': datetime.strptime(campi[4], '%d-%m-%Y').date(),
                        'idOperazione': int(campi[5])
                    }

                    lista_operazioni.append(operazione)

                except ValueError as e:
                    print(f"Errore conversione dati nella linea {linea}: {e}")
                    continue
                except Exception as e:
                    print(f"Errore processing linea {linea}: {e}")
                    continue

    except Exception as e:
        print(f"Errore durante la lettura del file: {e}")

    return lista_operazioni

class Operazione:
    def __init__(self,
                 id: int,
                 tipo: TipoOperazione,
                 articolo: Articolo,
                 quantitaVendita: float,
                 quantitaGiacenza: float,
                 data: datetime
    ):

        self.id = id
        self.tipo = tipo
        self.articolo = articolo
        self.quantitaVendita = quantitaVendita
        self.quantitaGiacenza = quantitaGiacenza
        self.data = data

    def aggiungiVendita(self):
        pass

    def aggiungiGiacenza(self):
        pass

    def modificaVendita(self):
        pass

    def modificaGiacenza(self):
        pass

    def aggiornaDb(self):
        """Aggiorna la quantità disponibile di un articolo"""
        pass