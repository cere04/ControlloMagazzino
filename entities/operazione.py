import os
from datetime import datetime
from typing import List, Dict, Any
from zipimport import path_sep


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

    def aggiungiVendita(self, sku, quantitaVendita, paese):
        """Aggiunge una vendita al database"""
        lista_operazioni = letturaDatabaseOperazioni("Model/databaseOperazioni.txt")
        self.id_auto = max(op['idOperazione'] for op in lista_operazioni) + 1 if lista_operazioni else 1
        self.data_formatted = self.data.strftime("%d-%m-%Y")
        line = (
            f"\n{sku}, "
            f"{quantitaVendita}, "
            f"-{quantitaVendita}, "
            f"{paese}, "
            f"{self.data_formatted}, "
            f"{self.id_auto}"
        )
        with open("Model/databaseOperazioni.txt", 'a') as file:
            file.write(line)

    def aggiungiGiacenza(self, sku, quantitaGiacenza):
        """Aggiunge una vendita al database"""
        lista_operazioni = letturaDatabaseOperazioni("Model/databaseOperazioni.txt")
        self.id_auto = max(op['idOperazione'] for op in lista_operazioni) + 1 if lista_operazioni else 1
        self.data_formatted = self.data.strftime("%d-%m-%Y")
        line=(
            f"\n{sku}, "
            f"{0}, "
            f"{quantitaGiacenza}, "
            f"Brancadoro, "
            f"{self.data_formatted}, "
            f"{self.id_auto}"
        )
        with open("Model/databaseOperazioni.txt", 'a') as file:
            file.write(line)

    def modificaGiacenza(self, id_set, sku_set, quantitaGiacenza, paese):

        lista_operazioni = letturaDatabaseOperazioni("Model/databaseOperazioni.txt")
        operazione_giacenza_trovata= False

        for op in lista_operazioni:
            if op['idOperazione'] == id_set:

                operazione_giacenza_trovata=True

                if sku_set is not None:
                    op['sku'] = sku_set

                if quantitaGiacenza != 0:
                    op['giacenza'] = quantitaGiacenza  # Aggiornamento automatico

                if paese is not None:
                    op['paese'] = paese

                op['vendita']=0

            lines = []
            for op1 in lista_operazioni:
                data_formatted = op1['data'].strftime('%d-%m-%Y')
                line = (
                    f"{op1['sku']}, "
                    f"{op1['vendita']}, "
                    f"{op1['giacenza']}, "
                    f"{op1['paese']}, "
                    f"{data_formatted}, "
                    f"{op1['idOperazione']}"
                )
                lines.append(line)

            try:
                with open("Model/databaseOperazioni.txt", 'w') as file:
                    file.write("\n".join(lines))
            except Exception as e:
                raise RuntimeError(f"Errore salvataggio database: {str(e)}")

        if not operazione_giacenza_trovata:
            raise ValueError(f"ID operazione {id_set} non trovato")

    def modificaVendita(self, id_set, sku_set, quantitaVendita, paese):
        lista_operazioni = letturaDatabaseOperazioni("Model/databaseOperazioni.txt")
        operazione_trovata= False

        sku_set:str
        quantitaVendita:int
        paese:str

        for op in lista_operazioni:
            if op["idOperazione"] == id_set:
                operazione_trovata=True

                if sku_set is not None:
                    op['sku'] = sku_set

                if quantitaVendita != 0:
                    op['vendita'] = quantitaVendita

                if paese is not None:
                    op['paese'] = paese

        lines = []
        for op1 in lista_operazioni:
            data_formatted = op1['data'].strftime('%d-%m-%Y')
            line = (
                f"{op1['sku']}, "
                f"{op1['vendita']}, "
                f"{op1['giacenza']}, "
                f"{op1['paese']}, "
                f"{data_formatted}, "
                f"{op1['idOperazione']}"
            )
            lines.append(line)

            try:
                with open("Model/databaseOperazioni.txt", 'w') as file:
                    file.write("\n".join(lines))
            except Exception as e:
                raise RuntimeError(f"Errore salvataggio database: {str(e)}")

        if not operazione_trovata:
            raise ValueError(f"ID operazione {id_set} non trovato")




# test metodi

# operazione = Operazione()
# operazione.modificaVendita(437, "922WE", 10, None)
# operazione.modificaGiacenza(437, "922WE", 51, "Italia", None)
# operazione.aggiungiGiacenza("922WE", 15)
# operazione.aggiungiVendita("922WE", 50, "Germania")