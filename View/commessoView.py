from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel,
    QMessageBox, QGroupBox, QFormLayout
)
from entities.operazione import Operazione, letturaDatabaseArticoli

class FinestraC(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finestra dei Commessi")
        self.setGeometry(200, 200, 700, 300)

        layoutMain = QHBoxLayout()

        # ---------- SEZIONE NUOVA VENDITA ----------
        nuovaVenditaBox = QGroupBox("Nuova Vendita")
        nuovaVenditaLayout = QFormLayout()

        self.sku_av = QLineEdit()
        self.sku_av.setPlaceholderText("Inserisci SKU")
        self.numero_av = QLineEdit()
        self.numero_av.setPlaceholderText("Inserisci Quantità")
        self.paese_av = QLineEdit()
        self.paese_av.setPlaceholderText("Inserisci Paese")

        nuovaVenditaLayout.addRow("SKU:", self.sku_av)
        nuovaVenditaLayout.addRow("Quantità:", self.numero_av)
        nuovaVenditaLayout.addRow("Paese:", self.paese_av)

        btn_aggiungi = QPushButton("Aggiungi")
        btn_aggiungi.clicked.connect(self.aggiunta)
        nuovaVenditaLayout.addWidget(btn_aggiungi)

        nuovaVenditaBox.setLayout(nuovaVenditaLayout)
        layoutMain.addWidget(nuovaVenditaBox)

        # ---------- SEZIONE MODIFICA VENDITA ----------
        modificaVenditaBox = QGroupBox("Modifica Vendita")
        modificaVenditaLayout = QFormLayout()

        self.id_Vendita = QLineEdit()
        self.id_Vendita.setPlaceholderText("ID Vendita")
        self.sku_mv = QLineEdit()
        self.sku_mv.setPlaceholderText("SKU")
        self.numero_mv = QLineEdit()
        self.numero_mv.setPlaceholderText("Quantità")
        self.paese_mv = QLineEdit()
        self.paese_mv.setPlaceholderText("Paese")

        modificaVenditaLayout.addRow("ID Vendita:", self.id_Vendita)
        modificaVenditaLayout.addRow("SKU:", self.sku_mv)
        modificaVenditaLayout.addRow("Quantità:", self.numero_mv)
        modificaVenditaLayout.addRow("Paese:", self.paese_mv)

        btn_modifica = QPushButton("Modifica")
        btn_modifica.clicked.connect(self.modifica_v_)
        modificaVenditaLayout.addWidget(btn_modifica)

        modificaVenditaBox.setLayout(modificaVenditaLayout)
        layoutMain.addWidget(modificaVenditaBox)

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
        SKU_AV = self.sku_av.text()
        N_AV = self.numero_av.text()
        P_AV = self.paese_av.text()

        if SKU_AV == '' or N_AV == '' or P_AV == '':
            QMessageBox.critical(self, 'ERRORE', 'Ci sono dei campi vuoti')
        else:
            lista_articoli = letturaDatabaseArticoli("Model/databaseArticoli.txt")
            n = 0
            for art in lista_articoli:
                if art['sku'] == SKU_AV:
                    n += 1
            if n == 1:
                O = Operazione()
                O.aggiungiVendita(SKU_AV, N_AV, P_AV)
            else:
                QMessageBox.critical(self, 'ERRORE', 'SKU NON ESISTENTE')

    def modifica_v_(self):
        SKU_MV = self.sku_mv.text()
        lista_articoli = letturaDatabaseArticoli("Model/databaseArticoli.txt")
        n = False
        for art in lista_articoli:
            if art['sku'] == SKU_MV or SKU_MV == '':
                n = True
        if n:
            try:
                id_vendita = int(self.id_Vendita.text())
            except ValueError:
                QMessageBox.critical(self, 'ERRORE', 'ID non valido')
                return

            OpP = Operazione()
            risultato = OpP.modificaVendita(id_vendita, SKU_MV, self.numero_mv.text(), self.paese_mv.text())

            if risultato is True:
                QMessageBox.critical(self, 'ERRORE', "L'operazione selezionata non è una vendita")
            elif risultato == 'non trovato':
                QMessageBox.critical(self, 'ERRORE', "L'operazione non esiste")
        else:
            QMessageBox.critical(self, 'ERRORE', "SKU non esiste")
