from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from entities.operazione import Operazione


class FinestraC(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finestra dei Commessi")
        self.setGeometry(200, 200, 300, 200)
        layoutM = QVBoxLayout()
        layoutH1 = QHBoxLayout()
        layoutH3 = QHBoxLayout()
        layoutH5 = QHBoxLayout()
        layoutH6 = QHBoxLayout()

        self.numero_av = QLineEdit()
        self.sku_av = QLineEdit()
        self.paese_av = QLineEdit()

        self.numero_mv = QLineEdit()
        self.sku_mv = QLineEdit()
        self.id_Vendita = QLineEdit()
        self.paese_mv = QLineEdit()

        aggiungi = QPushButton("Aggiungi")
        aggiungi.clicked.connect(self.aggiunta)
        modifica_v = QPushButton("Modifica")
        modifica_v.clicked.connect(self.modifica_v_)

        layoutH5.addWidget(QLabel('NUOVA VENDITA'))
        layoutH5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutM.addLayout(layoutH5)

        layoutH1.addWidget(QLabel('SKU:'))
        layoutH1.addWidget(self.sku_av)
        layoutH1.addWidget(QLabel('QUANTITÀ:'))
        layoutH1.addWidget(self.numero_av)
        layoutH1.addWidget(QLabel('PAESE:'))
        layoutH1.addWidget(self.paese_av)
        layoutM.addLayout(layoutH1)

        layoutM.addWidget(aggiungi)

        layoutH6.addWidget(QLabel('MODIFICA GIACENZA'))
        layoutH6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutM.addLayout(layoutH6)

        layoutH3.addWidget(QLabel('ID VENDITA:'))
        layoutH3.addWidget(self.id_Vendita)

        layoutH3.addWidget(QLabel('SKU:'))
        layoutH3.addWidget(self.sku_mv)

        layoutH3.addWidget(QLabel('QUANTITÀ:'))
        layoutH3.addWidget(self.numero_mv)

        layoutH3.addWidget(QLabel('PAESE:'))
        layoutH3.addWidget(self.paese_mv)

        layoutM.addLayout(layoutH3)

        layoutM.addWidget(modifica_v)
        layoutM.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layoutM)

    def aggiunta(self):
        SKU_AV = self.sku_av.text()
        N_AV = self.numero_av.text()
        P_AV = self.paese_av.text()
        if SKU_AV == '' or N_AV == '' or P_AV == '':
            a = QMessageBox()
            a.setWindowTitle('ERRORE')
            a.setText('Ci sono dei campi vuoti')
            a.exec()
        else:
            O = Operazione()
            x = O.aggiungiVendita(self.sku_av.text(), self.numero_av.text(), self.paese_av.text())

    def modifica_v_(self):
        #SKU_MV = str(self.sku_mv.text())
        #N_MV = int(self.numero_mv.text())
        #P_MV = str(self.paese_mv.text())
        #ID_VENDITA = int(self.id_Vendita.text())
        #if SKU_MV == '':
        #    SKU_MV = None
        #if N_MV == '':
         #   N_MV = None
        #if P_MV == '':
         #   P_MV = None
        #if ID_VENDITA == '':
         #   ID_VENDITA = None
        OpP = Operazione()
        OpP.modificaVendita(int(self.id_Vendita.text()), str(self.sku_mv.text()), str(self.numero_mv.text()) ,str(self.paese_mv.text()))

