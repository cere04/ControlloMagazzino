from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel,
    QMessageBox, QGroupBox, QFormLayout
)
from entities.operazione import Operazione, letturaDatabaseArticoli

class FinestraM(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finestra dei Magazzinieri")
        self.setGeometry(200, 200, 700, 300)

        layoutMain = QHBoxLayout()

        # ---------- SEZIONE NUOVA GIACENZA ----------
        nuovaGiacenzaBox = QGroupBox("Nuova Giacenza")
        nuovaGiacenzaLayout = QFormLayout()

        self.sku_ag = QLineEdit()
        self.sku_ag.setPlaceholderText("Inserisci SKU")
        self.numero_ag = QLineEdit()
        self.numero_ag.setPlaceholderText("Inserisci Quantità")

        nuovaGiacenzaLayout.addRow("SKU:", self.sku_ag)
        nuovaGiacenzaLayout.addRow("Quantità:", self.numero_ag)

        btn_aggiungi = QPushButton("Aggiungi")
        btn_aggiungi.clicked.connect(self.aggiunta)
        nuovaGiacenzaLayout.addWidget(btn_aggiungi)

        nuovaGiacenzaBox.setLayout(nuovaGiacenzaLayout)
        layoutMain.addWidget(nuovaGiacenzaBox)

        # ---------- SEZIONE MODIFICA GIACENZA ----------
        modificaBox = QGroupBox("Modifica Giacenza")
        modificaLayout = QFormLayout()

        self.id_Giacenza = QLineEdit()
        self.id_Giacenza.setPlaceholderText("ID Operazione")

        self.sku_mg = QLineEdit()
        self.sku_mg.setPlaceholderText("SKU")
        self.numero_mg = QLineEdit()
        self.numero_mg.setPlaceholderText("Quantità")

        modificaLayout.addRow("ID Operazione:", self.id_Giacenza)
        modificaLayout.addRow("SKU:", self.sku_mg)
        modificaLayout.addRow("Quantità:", self.numero_mg)

        btn_modifica = QPushButton("Modifica")
        btn_modifica.clicked.connect(self.modifica_)
        modificaLayout.addWidget(btn_modifica)

        modificaBox.setLayout(modificaLayout)
        layoutMain.addWidget(modificaBox)

        self.setLayout(layoutMain)

        # ---------- STILE ----------
        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                font-family: Arial, sans-serif;
                color: #000000;
            }
            QGroupBox {
                border: 2px solid #0F4C81;
                border-radius: 8px;
                margin-top: 10px;
                padding: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
                color: #0F4C81;
                font-weight: bold;
                font-size: 16px;
            }
            QLineEdit {
                padding: 8px;
                border: 2px solid #cccccc;
                border-radius: 8px;
                font-size: 14px;
                color: black;
            }
            
            QLineEdit:focus {
                border: 2px solid #3A81F1;
            }
            
            QPushButton {
                padding: 10px;
                background-color: #0F4C81;
                color: white;
                border: none;
                border-radius: 8px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1666AA;
            }

            QPushButton:pressed {
                background-color: #0C3C66;
            }
        """)

    def aggiunta(self):
        SKU_AG = self.sku_ag.text()
        N_AG = self.numero_ag.text()

        if SKU_AG == '' or N_AG == '':
            QMessageBox.critical(self, 'ERRORE', 'Ci sono dei campi vuoti')
        else:
            lista_articoli = letturaDatabaseArticoli("Model/databaseArticoli.txt")
            n = 0
            for art in lista_articoli:
                if art['sku'] == SKU_AG:
                    n += 1
            if n == 1:
                O = Operazione()
                O.aggiungiGiacenza(self.sku_ag.text(), self.numero_ag.text())
            else:
                QMessageBox.critical(self, 'ERRORE', 'SKU NON ESISTENTE')

    def modifica_(self):
        SKU_MG = self.sku_mg.text()
        lista_articoli = letturaDatabaseArticoli("Model/databaseArticoli.txt")
        n = False
        for art in lista_articoli:
            if art['sku'] == SKU_MG or SKU_MG == '':
                n = True
        if n:
            Opp = Operazione()
            k = Opp.modificaGiacenza(int(self.id_Giacenza.text()), self.sku_mg.text(), self.numero_mg.text(), None)
            if k is True:
                QMessageBox.critical(self, 'ERRORE', "L'operazione selezionata non è una giacenza")
            elif k == 'Errore':
                QMessageBox.critical(self, 'ERRORE', "L'operazione non esiste")
        else:
            QMessageBox.critical(self, 'ERRORE', "SKU non esiste")
