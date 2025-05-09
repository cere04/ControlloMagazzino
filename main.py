import sys
from abc import ABCMeta, abstractmethod

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont
from GUI.gui import MainWindow

def run_app():
    app = QApplication(sys.argv)

    # Configurazione font di default
    font = QFont("Segoe UI")
    font.setPointSize(10)
    app.setFont(font)

    # Creazione e visualizzazione finestra principale
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    run_app()

class absClass(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def virtual_method(self):
        pass

class subClass(absClass):
    def virtual_method(self):
        a=1
        print(a)



# print("\nSeleziona filtri (separa numeri con virgola, 0 per nessuno):")
# print("1-SKU, 2-Genere, 3-Tipologia, 4-Paese")
# scelte = input("Scelte: ")
# scelte = {s.strip() for s in scelte.split(',')} if scelte else set()
#
# sku_vals = generi_vals = tipologia_vals = zone_vals = None
#
# if '1' in scelte:
#     sku_vals = input("Inserisci SKU (,) : ").split(',')
# if '2' in scelte:
#     generi_vals = input("Inserisci generi: ").split(',')
# if '3' in scelte:
#     tipologia_vals = input("Inserisci tipologie: ").split(',')
# if '4' in scelte:
#     zone_vals = input("Inserisci paesi/aree: ").split(',')
#
# risultati = filtraOperazioni(
#     lista_operazioni=operazioni,
#     lista_articoli=articoli,
#     sku=sku_vals,
#     generi=generi_vals,
#     tipologie=tipologia_vals,
#     zone=zone_vals
# )

# print(risultati)




# from utils import (
#     letturaDatabaseOperazioni,
#     letturaDatabaseArticoli,
#     filtraOperazioni
# )
#
# file_operazioni = input("../databaseOperazioni.txt): ")
# file_articoli = input("../databaseArticoli.txt): ")
#
# operazioni = letturaDatabaseOperazioni(file_operazioni)
# articoli = letturaDatabaseArticoli(file_articoli)
#
# print("\nSeleziona filtri (separa numeri con virgola, 0 per nessuno):")
# print("1-SKU, 2-Genere, 3-Tipologia, 4-Paese")
# scelte = input("Scelte: ")
# scelte = {s.strip() for s in scelte.split(',')} if scelte else set()
#
# sku_vals = generi_vals = tipologia_vals = zone_vals = None
#
# if '1' in scelte:
#     sku_vals = input("Inserisci SKU (,) : ").split(',')
# if '2' in scelte:
#     generi_vals = input("Inserisci generi: ").split(',')
# if '3' in scelte:
#     tipologia_vals = input("Inserisci tipologie: ").split(',')
# if '4' in scelte:
#     zone_vals = input("Inserisci paesi/aree: ").split(',')
#
# risultati = filtraOperazioni(
#     lista_operazioni=operazioni,
#     lista_articoli=articoli,
#     sku=sku_vals,
#     generi=generi_vals,
#     tipologie=tipologia_vals,
#     zone=zone_vals
# )


#ciao
#ciao