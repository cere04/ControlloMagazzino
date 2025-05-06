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


def calcolaVenditeMensili(operazioni: List[Dict[str, any]]) -> List[int]:
    """
    Calcola le vendite totali per ogni mese dell'anno

    Args:
        operazioni: lista delle operazioni dal database

    Returns:
        Una lista con 12 elementi (uno per mese) contenente i totali delle vendite
    """

    vendite_mensili = [0] * 12

    for op in operazioni:
        # Considera solo le operazioni di vendita (vendita positiva)
        if op['vendita'] > 0:
            mese = op['data'].month - 1  # Converti in indice (0-11)
            vendita = op['vendita']
            vendite_mensili[mese] += vendita

    return vendite_mensili

def visualizzaVenditeMensili(vendite_mensili: List[int]):
    """
    Visualizza i totali delle vendite per ogni mese

    Args:
        vendite_mensili: lista con i totali delle vendite per ogni mese
    """
    mesi = [
        "Gennaio", "Febbraio", "Marzo", "Aprile",
        "Maggio", "Giugno", "Luglio", "Agosto",
        "Settembre", "Ottobre", "Novembre", "Dicembre"
    ]

    print("\n=== VENDITE MENSILI ===")
    for i, totale in enumerate(vendite_mensili):
        print(f"{mesi[i]}: {totale}")
    print("======================")

    return

# 1. Leggi il database
operazioni = letturaDatabase("../databaseOperazioni.txt")

if not operazioni:
    print("Nessuna operazione trovata nel database")
else:
    print(f"Lettura completata. Trovate {len(operazioni)} operazioni")

    # 2. Calcola le vendite per ogni mese
    vendite_mensili = calcolaVenditeMensili(operazioni)

    # 3. Visualizza i risultati
    visualizzaVenditeMensili(vendite_mensili)


# operazioni = letturaDatabase("../databaseOperazioni.txt")
# calcolaVenditeMensili(operazioni, 3)