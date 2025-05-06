import os
from datetime import datetime
from typing import List, Dict, Tuple

def letturaDatabaseOperazioni(nome_file: str) -> List[Dict[str, any]]:
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
                        'sku': campi[0],
                        'vendita': int(campi[1]),
                        'giacenza': int(campi[2]),
                        'paese': campi[3],
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

def letturaDatabaseArticoli(nome_file: str) -> List[Dict[str, str]]:
    """
    Legge il file databaseArticoli.txt e restituisce una lista di dizionari

    Args:
        nome_file: percorso del file da leggere

    Returns:
        Lista di dizionari con i dati degli articoli
    """
    articoli = []

    try:
        with open(nome_file, 'r') as file:
            for linea in file:
                linea = linea.strip()
                if not linea:
                    continue

                campi = [campo.strip() for campo in linea.split(',')]
                if len(campi) != 3:
                    continue

                articoli.append({
                    'sku': campi[0],
                    'genere': campi[1],
                    'tipologia': campi[2]
                })

    except ValueError as e:
        print(f"Errore conversione dati nella linea {linea}: {e}")
    except Exception as e:
        print(f"Errore durante la lettura del file articoli: {e}")

    return articoli

def calcolaVenditeTotali(operazioni: List[Dict[str, any]]) -> List[int]:
    """
    Calcola le vendite totali per ogni mese dell'anno

    Args:
        operazioni: lista delle operazioni dal database

    Returns:
        Una lista con 12 elementi (uno per mese) contenente i totali delle vendite
    """

    vendite_totali = [0] * 12

    for op in operazioni:
        # Considera solo le operazioni di vendita (vendita positiva)
        if op['vendita'] > 0:
            mese = op['data'].month - 1  # Converti in indice (0-11)
            vendita = op['vendita']
            vendite_totali[mese] += vendita

    return vendite_totali

def filtroSKU(operazioni: List[Dict[str, any]], sku_list: List[str]) -> List[int]:
    """
    Calcola le vendite totali per ogni mese dell'anno

    Args:
        operazioni: lista delle operazioni dal database

    Returns:
        Una lista con 12 elementi (uno per mese) contenente i totali delle vendite
    """

    if not sku_list:
        return operazioni

    sku_set = set(sku_list)
    return[op for op in operazioni if op['sku'] in sku_set]


def filtroGenere(operazioni: List[Dict[str, any]], articoli: List[Dict[str, any]], generi: List[str]) -> List[Dict[str, any]]:
    """
    Filtra le operazioni per genere (uomo/donna)

    Args:
        operazioni: lista delle operazioni da filtrare
        generi: lista di generi da includere ('uomo', 'donna')

    Returns:
        Lista filtrata delle operazioni
    """
    if not generi:
        return operazioni

    test = []

    for art in articoli:
        if art['genere'] in generi:
            test.append(art['sku'])

    return [op for op in operazioni if op['sku'] in test]

# def filtroTipologia(operazioni: List[Dict[str, any]], tipologie: List[str]) -> List[Dict[str, any]]:
#     """
#     Filtra le operazioni per tipologia (calzatura, borsa, capi di abbigliamento)
#
#     Args:
#         operazioni: lista delle operazioni da filtrare
#         tipologie: lista di tipologie da includere
#
#     Returns:
#         Lista filtrata delle operazioni
#     """
#     if not tipologie or not DATABASE_ARTICOLI:
#         return operazioni
#
#     # Crea un set di SKU per le tipologie richieste
#     sku_tipologie = {art['sku'] for art in DATABASE_ARTICOLI if art['tipologia'] in tipologie}
#
#     return [op for op in operazioni if op['sku'] in sku_tipologie]
#
#
# def filtroZona(operazioni: List[Dict[str, any]], zone: List[str]) -> List[Dict[str, any]]:
#     """
#     Filtra le operazioni per zona
#
#     Args:
#         operazioni: lista delle operazioni da filtrare
#         zone: lista di zone da includere
#
#     Returns:
#         Lista filtrata delle operazioni
#     """
#     if not zone:
#         return operazioni
#
#     # Nota: Assumendo che 'paese' sia la zona, altrimenti modificare
#     zone_set = set(zone)
#     return [op for op in operazioni if op['paese'] in zone_set]


def filtraOperazioni(operazioni: List[Dict[str, any]],
                     sku: List[str] = None,
                     generi: List[str] = None,
                     # tipologie: List[str] = None,
                     # zone: List[str] = None
                     ) -> List[Dict[str, any]]:
    """
    Applica tutti i filtri specificati alle operazioni

    Args:
        operazioni: lista delle operazioni da filtrare
        sku: lista di SKU da includere
        generi: lista di generi da includere
        tipologie: lista di tipologie da includere
        zone: lista di zone da includere

    Returns:
        Lista filtrata delle operazioni
    """
    filtrate = operazioni

    if sku:
        filtrate = filtroSKU(filtrate, sku)
    if generi:
        filtrate = filtroGenere(filtrate, articoli, generi)

    # if tipologie:
    #     filtrate = filtroTipologia(filtrate, tipologie)
    # if zone:
    #     filtrate = filtroZona(filtrate, zone)

    return filtrate

operazioni = letturaDatabaseOperazioni("../databaseOperazioni.txt")
articoli = letturaDatabaseArticoli("../databaseArticoli.txt")
# vendite_mensili = calcolaVenditeTotali(operazioni)
prova = filtraOperazioni(operazioni , [], ['uomo'])
print(prova)





















# def visualizzaVenditeMensili(vendite_mensili: List[int]):
#     """
#     Visualizza i totali delle vendite per ogni mese
#
#     Args:
#         vendite_mensili: lista con i totali delle vendite per ogni mese
#     """
#     mesi = [
#         "Gennaio", "Febbraio", "Marzo", "Aprile",
#         "Maggio", "Giugno", "Luglio", "Agosto",
#         "Settembre", "Ottobre", "Novembre", "Dicembre"
#     ]
#
#     print("\n=== VENDITE MENSILI ===")
#     for i, totale in enumerate(vendite_mensili):
#         print(f"{mesi[i]}: {totale}")
#     print("======================")


# test funzioni
# 1. Leggi il database

# if not operazioni:
#     print("Nessuna operazione trovata nel database")
# else:
#     print(f"Lettura completata. Trovate {len(operazioni)} operazioni")
#
#     # 2. Calcola le vendite per ogni mese

    # 3. Visualizza i risultati
    # visualizzaVenditeMensili(vendite_mensili)


# operazioni = letturaDatabase("../databaseOperazioni.txt")
# calcolaVenditeMensili(operazioni, 3)