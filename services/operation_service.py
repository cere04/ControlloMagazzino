import os
from datetime import datetime
from typing import List, Dict, Tuple


def letturaDatabase(nome_file: str) -> List[Dict[str, any]]:
    """
    Legge il file di database e restituisce una lista di dizionari con i dati

    Args:
        nome_file: percorso del file da leggere

    Returns:
        Lista di dizionari con i dati delle operazioni
    """
    operazioni = []

    # Verifica se il file esiste
    if not os.path.exists(nome_file):
        print(f"Errore: il file {nome_file} non esiste")
        return operazioni

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
                        'vendita': int(campi[1]),
                        'data': datetime.strptime(campi[4], '%d-%m-%Y').date(),
                        'idOperazione': int(campi[5])
                    }

                    operazioni.append(operazione)

                except ValueError as e:
                    print(f"Errore conversione dati nella linea {linea}: {e}")
                    continue
                except Exception as e:
                    print(f"Errore processing linea {linea}: {e}")
                    continue

    except Exception as e:
        print(f"Errore durante la lettura del file: {e}")

    return operazioni


def calcolaVenditeMensili(operazioni: List[Dict[str, any]], mese: int) -> Tuple[int, Dict[str, int]]:
    """
    Calcola le vendite totali per un mese specifico

    Args:
        operazioni: lista delle operazioni dal database
        mese: mese da analizzare (1-12)

    Returns:
        Una tupla con (vendite_totali)
    """
    vendite_totali = 0

    for op in operazioni:
        # Considera solo le operazioni di vendita (vendita negativa)
        if op['vendita'] > 0 and op['data'].month == mese:
            vendita = op['vendita']
            vendite_totali += vendita

    print(vendite_totali)

operazioni = letturaDatabase("../databaseOperazioni.txt")
calcolaVenditeMensili(operazioni, 3)