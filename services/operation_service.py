import os
from datetime import datetime
from typing import List, Dict, Any
from collections import defaultdict


def calcolaVenditeTotali(lista_operazioni: List[Dict[str, any]]) -> List[int]:
    """
    Calcola le vendite totali per ogni mese dell'anno

    Args:
        lista_operazioni: lista delle operazioni dal database

    Returns:
        Una lista con 12 elementi (uno per mese) contenente i totali delle vendite
    """

    vendite_totali = [0] * 12

    for op in lista_operazioni:
        # Considera solo le operazioni di vendita (vendita positiva)
        if op['vendita'] > 0:
            mese = op['data'].month - 1  # Converti in indice (0-11)
            vendita = op['vendita']
            vendite_totali[mese] += vendita

    return vendite_totali

def calcolaGiacenzaMedia(lista_operazioni: List[Dict[str, any]]) -> List[int]:
    sorted_operazioni = sorted(lista_operazioni, key=lambda x: x['data'])

    current_balance = 0
    giacenzaMedia = [0] * 12

    operazioni_per_mese = defaultdict(list)

    for op in lista_operazioni:
        mese = op['data'].month - 1  # Convert to 0-based index (0-11)
        operazioni_per_mese[mese].append(op)

    # Process each month in order from January (0) to December (11)
    for mese in range(12):
        initial_balance = current_balance
        sum_vendite = 0

        for op in operazioni_per_mese.get(mese, []):
            if op['giacenza'] < 0:
                sum_vendite += op['vendita']


        print(initial_balance)
        print(sum_vendite)

        # Update the current balance (final balance for the month)
        final_balance = initial_balance - sum_vendite

        average = (initial_balance + final_balance) // 2  # Using integer division
        giacenzaMedia[mese] = average

        # Update the current balance for the next month's initial balance
        current_balance = final_balance

    return giacenzaMedia

# --------------------------
# prova calcoloGiacenzaMedia
# --------------------------

# def calcolaGiacenzaMedia(lista_operazioni: List[Dict[str, any]]) -> List[int]:
#
#     giacenzeTotali = [0] * 12
#     giacenzeTotaliSucc = [0] * 13
#     giacenzaMedia = [0] * 12
#
#
#
#     for op in lista_operazioni:
#         if op['giacenza'] < 0:
#             mese = op['data'].month - 1  # Converti in indice (0-11)
#             mese_successivo = op['data'].month   # Converti in indice (0-11)
#             giacenza = op['vendita']
#             giacenzeTotali[mese] += giacenza
#             giacenzeTotaliSucc[mese_successivo] += giacenza
#             giacenzaMedia[mese] = (giacenzeTotali[mese] + giacenzeTotaliSucc[mese])/2
#
#
#     # print(giacenzeTotali)
#     # print(giacenzeTotaliSucc)
#     # print(giacenzaMedia)
#     return giacenzaMedia


def filtroSKU(lista_operazioni: List[Dict[str, any]], sku_list: List[str]) -> list[dict[str, Any]]:
    """
    Calcola le vendite totali per ogni mese dell'anno

    Args:
        operazioni: lista delle operazioni dal database

    Returns:
        Una lista con 12 elementi (uno per mese) contenente i totali delle vendite
        :param lista_operazioni:
        :param sku_list:
    """

    if not sku_list:
        return lista_operazioni

    sku_set = set(sku_list)
    return[op for op in lista_operazioni if op['sku'] in sku_set]


def filtroGenere(lista_operazioni: List[Dict[str, any]], lista_articoli: List[Dict[str, any]], generi: List[str]) -> List[Dict[str, any]]:
    """
    Filtra le operazioni per genere (uomo/donna)

    Args:
        lista_operazioni: lista delle operazioni da filtrare
        generi: lista di generi da includere ('uomo', 'donna')

    Returns:
        Lista filtrata delle operazioni
        :param generi:
        :param lista_operazioni:
        :param lista_articoli:
    """
    if not generi:
        return lista_operazioni

    test = []

    for art in lista_articoli:
        if art['genere'] in generi:
            test.append(art['sku'])

    return [op for op in lista_operazioni if op['sku'] in test]

def filtroTipologia(lista_operazioni: List[Dict[str, any]], lista_articoli: List[Dict[str, any]], tipologie: List[str]) -> List[Dict[str, any]]:
    """
    Filtra le operazioni per genere (uomo/donna)

    Args:
        lista_operazioni: lista delle operazioni da filtrare
        generi: lista di generi da includere ('uomo', 'donna')

    Returns:
        Lista filtrata delle operazioni
        :param tipologie:
        :param lista_operazioni:
        :param lista_articoli:
    """
    if not tipologie:
        return lista_operazioni

    test = []

    for art in lista_articoli:
        if art['tipologia'] in tipologie:
            test.append(art['sku'])

    return [op for op in lista_operazioni if op['sku'] in test]

def filtroZona(lista_operazioni: List[Dict[str, any]], zone: List[str]) -> list[dict[str, Any]]:
    """
    Calcola le vendite totali per ogni mese dell'anno

    Args:
        operazioni: lista delle operazioni dal database

    Returns:
        Una lista con 12 elementi (uno per mese) contenente i totali delle vendite
        :param zone:
        :param lista_operazioni:
    """

    if not zone:
        return lista_operazioni

    zone_set = set(zone)
    return[op for op in lista_operazioni if op['paese'] in zone_set]

def filtraOperazioni(lista_operazioni: List[Dict[str, any]],
                     lista_articoli: List[Dict[str, Any]],
                     sku: List[str] = None,
                     generi: List[str] = None,
                     tipologie: List[str] = None,
                     zone: List[str] = None
                     ) -> List[Dict[str, any]]:
    """
    Applica tutti i filtri specificati alle operazioni

    Args:
        lista_operazioni: lista delle operazioni da filtrare
        sku: lista di SKU da includere
        generi: lista di generi da includere
        tipologie: lista di tipologie da includere
        zone: lista di zone da includere

    Returns:
        Lista filtrata delle operazioni
        :param zone:
        :param tipologie:
        :param generi:
        :param sku:
        :param lista_operazioni:
        :param lista_articoli:
    """
    filtrate = lista_operazioni

    if sku:
        filtrate = filtroSKU(filtrate, sku)
    if generi:
        filtrate = filtroGenere(filtrate, lista_articoli, generi)
    if tipologie:
        filtrate = filtroTipologia(filtrate, lista_articoli, tipologie)
    if zone:
        filtrate = filtroZona(filtrate, zone)

    return filtrate


# operazioni = letturaDatabaseOperazioni("../databaseOperazioni.txt")
# articoli = letturaDatabaseArticoli("../databaseArticoli.txt")
# vendite_mensili = calcolaVenditeTotali(operazioni)
# dati_filtrati = filtraOperazioni(operazioni , ['287ZO'], [], [], ['Francia'])
# print(dati_filtrati)





















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