import os
from datetime import datetime
from entities.enums import TipoOperazione
from entities.articolo import Articolo
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
                 id= None,
                 tipo= None,
                 sku= None,
                 quantitaVendita = 0,
                 quantitaGiacenza = 0,
                 paese= None,
                 data = datetime.now(),
    ):

        try:
            self.quantitaVendita = int(quantitaVendita)
        except (ValueError, TypeError):
            self.quantitaVendita = 0

        try:
            self.quantitaGiacenza = int(quantitaGiacenza)
        except (ValueError, TypeError):
            self.quantitaGiacenza = 0

        self.id = id
        self.tipo = tipo
        self.sku = sku
        self.quantitaVendita = quantitaVendita
        self.quantitaGiacenza = quantitaGiacenza
        self.data = data
        self.paese = paese

    def aggiungiVendita(self):
        """Aggiunge una vendita al database con controlli."""
        lista_operazioni = letturaDatabaseOperazioni("../db/databaseOperazioni.txt")
        id_auto = max(op['idOperazione'] for op in lista_operazioni) + 1 if lista_operazioni else 1
        self.data_formatted = self.data.strftime("%d-%m-%Y")
        with open("../db/databaseOperazioni.txt", 'a') as file:
            file.write(f"\n{self.sku}, {self.quantitaVendita}, {-self.quantitaVendita}, {self.paese}, {self.data_formatted}, {id_auto}" )

    def aggiungiGiacenza(self):
        lista_operazioni = letturaDatabaseOperazioni("../db/databaseOperazioni.txt")
        id_auto = max(op['idOperazione'] for op in lista_operazioni) + 1 if lista_operazioni else 1
        self.data_formatted = self.data.strftime("%d-%m-%Y")
        with open("../db/databaseOperazioni.txt", 'a') as file:
            file.write(f"\n{self.sku}, {0}, {self.quantitaGiacenza}, {self.paese}, {self.data_formatted}, {id_auto}" )

    def modificaVendita(self, id_set, sku, quantitaVendita, quantitaGiacenza, data):
        lista_operazioni = letturaDatabaseOperazioni("../db/databaseOperazioni.txt")
        operazione_trovata = False

        for op in lista_operazioni:
            if op['idOperazione'] == id_set:
                operazione_trovata = True

                # Aggiorna solo i campi forniti
                if self.sku not in (None, ""):
                    op['sku'] = self.sku
                if self.quantitaVendita != 0:
                    op['quantitaVendita'] = self.quantitaVendita
                    op['quantitaGiacenza'] = -self.quantitaVendita  # Aggiornamento automatico

                if self.paese not in (None, ""):
                    op['paese'] = self.paese

                if self.data:
                    op['data'] = self.data.strftime("%d-%m-%Y")

                break
            # if not operazione_trovata:
            #     raise ValueError(f"ID operazione {id_set} non trovato")

            lines = []
            for op1 in lista_operazioni:
                line = (
                    f"{op1['sku']},"
                    f"{op1['quantitaVendita']},"
                    f"{op1['quantitaGiacenza']},"
                    f"{op1['paese']},"
                    f"{op1['data']},"
                    f"{op1['idOperazione']}"
                )
                lines.append(line)

            try:
                with open("../db/databaseOperazioni.txt", 'w') as file:
                    file.write("\n".join(lines))
            except Exception as e:
                raise RuntimeError(f"Errore salvataggio database: {str(e)}")

    def modificaGiacenza(self):
        pass

    # def aggiornaDb(self):
    #     """Scrive l'operazione nel file database."""
    #     nome_file = "db/databaseOperazioni.txt"
    #     data_str = self.data.strftime('%d-%m-%Y')
    #     sku = self.articolo.sku  # Assumendo che Articolo abbia attributo sku
    #     linea = (
    #         f"{sku}, {self.quantitaVendita}, {self.quantitaGiacenza}, "
    #         f"{self.paese}, {data_str}, {self.id}\n"
    #     )
    #     try:
    #         with open(nome_file, 'a') as file:
    #             file.write(linea)
    #     except Exception as e:
    #         print(f"Errore durante il salvataggio: {e}")
    #         raise


# test metodi
# operazione = Operazione(sku="922WE", quantitaGiacenza=15, paese="Italia")
operazione = Operazione(sku="922WE", quantitaVendita=15, paese="Italia")
# operazione.modificaVendita(90, "922WA", 51, 0, None)
operazione.aggiungiVendita()
