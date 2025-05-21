from typing import List, Dict, Any
from entities.operazione import letturaDatabaseOperazioni, letturaDatabaseArticoli


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

def ordinamentoOperazioni(lista_operazioni: List[Dict[str, any]], mese_set):

    if mese_set == 2:
        giorni_mese = 28
    elif mese_set in {1, 3, 5, 7, 8, 10, 12}:
        giorni_mese = 31
    else:
        giorni_mese = 30

    operazioni_ordinate = [0] * giorni_mese

    for op in lista_operazioni:
        data_op = op['data']

        # Estrae mese e giorno dalla data
        mese_op = int(data_op.strftime("%m"))
        giorno_op = int(data_op.strftime("%d"))

        # Controlla se l'operazione appartiene al mese specificato
        if mese_op != mese_set:
            continue

        # Verifica che il giorno sia valido per il mese
        if giorno_op < 1 or giorno_op > giorni_mese:
            continue

        # Aggiunge la giacenza al giorno corrispondente
        operazioni_ordinate[giorno_op - 1] += op['giacenza']

    return operazioni_ordinate

def giacenzaMediaMensile(operazioni_ordinate, mese_set) -> List[int]:
    '''metodo per il calcolo della giacenza media'''

    totale=0
    somma_corrente=0
    ultimo_valore = 0

    if mese_set == 2:
        giorni_mese = 28
    elif mese_set in {1, 3, 5, 7, 8, 10, 12}:
        giorni_mese = 31
    else:
        giorni_mese = 30

    for i in range(giorni_mese):
        elemento_corrente = operazioni_ordinate[i]
        if elemento_corrente != 0:
            ultimo_valore = elemento_corrente
            somma_corrente+=ultimo_valore
        totale+=somma_corrente

        media=totale/giorni_mese
        media_round=round(media,2)
    return media_round

def indiceRotazione(vendite_totali, media_round):
    indice_rotazione_round=[0]*12

    for i in range(12):
        indice_rotazione=vendite_totali[i]/media_round[i]
        indice_rotazione_round[i]=round(indice_rotazione, 2)
    return indice_rotazione_round

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


#test metodi

lista_operazioni = letturaDatabaseOperazioni("../Model/databaseOperazioni.txt")
lista_articoli = letturaDatabaseArticoli("../Model/databaseArticoli.txt")

dati_filtrati = filtraOperazioni(lista_operazioni ,lista_articoli , [], [], [])

giacenza_media = [0] * 12

vendite_totali = calcolaVenditeTotali(lista_operazioni)

for i in range(12):
    operazioni_ordinate=ordinamentoOperazioni(dati_filtrati, i+1)
    giacenza_media[i]=giacenzaMediaMensile(operazioni_ordinate, i+1)

indice_rotazione=indiceRotazione(vendite_totali, giacenza_media)
print("vendite totali:", vendite_totali)
print("giacenza media:",giacenza_media)
print("indice rotazione:", indice_rotazione)







# vendite_mensili = calcolaVenditeTotali(operazioni)






















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