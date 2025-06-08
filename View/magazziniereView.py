from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from entities.operazione import Operazione, letturaDatabaseArticoli


class FinestraM(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finestra dei Magazzinieri")
        self.setGeometry(200, 200, 300, 200)
        layoutM = QVBoxLayout()
        layoutH1 = QHBoxLayout()
        layoutH2 = QHBoxLayout()
        layoutH3 = QHBoxLayout()
        layoutH4 = QHBoxLayout()
        layoutH5 = QHBoxLayout()
        layoutH6 = QHBoxLayout()

        self.numero_ag = QLineEdit()
        self.numero_ag.setMaximumWidth(100)

        self.sku_ag = QLineEdit()
        self.sku_ag.setMaximumWidth(100)

        self.id_Giacenza = QLineEdit()
        self.id_Giacenza.setMaximumWidth(100)

        self.sku_mg = QLineEdit()
        self.sku_mg.setMaximumWidth(100)

        self.numero_mg = QLineEdit()
        self.numero_mg.setMaximumWidth(100)

        aggiungi = QPushButton("Aggiungi")
        aggiungi.clicked.connect(self.aggiunta)
        modifica = QPushButton("Modifica")
        modifica.clicked.connect(self.modifica_)

        layoutH5.addWidget(QLabel('NUOVA GIACENZA'))
        layoutH5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutM.addLayout(layoutH5)


        layoutH1.addWidget(QLabel('SKU:'))
        layoutH1.addWidget(self.sku_ag)
        layoutH1.addWidget(QLabel('QUANTITÀ:'))
        layoutH1.addWidget(self.numero_ag)
        layoutM.addLayout(layoutH1)

        layoutM.addWidget(aggiungi)

        layoutH6.addWidget(QLabel('MODIFICA GIACENZA'))
        layoutH6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutM.addLayout(layoutH6)

        layoutH3.addWidget(QLabel('ID GIACENZA:'))
        layoutH3.addWidget(self.id_Giacenza)

        layoutH3.addWidget(QLabel('SKU:'))
        layoutH3.addWidget(self.sku_mg)

        layoutH3.addWidget(QLabel('QUANTITÀ:'))
        layoutH3.addWidget(self.numero_mg)

        layoutM.addLayout(layoutH3)

        layoutM.addWidget(modifica)
        layoutM.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layoutM)
    def aggiunta(self):
        SKU_AG = self.sku_ag.text()
        N_AG = self.numero_ag.text()


        if SKU_AG == '' or N_AG == '':
            a = QMessageBox()
            a.setWindowTitle('ERRORE')
            a.setText('Ci sono dei campi vuoti')
            a.exec()
        else:
            lista_articoli = letturaDatabaseArticoli("Model/databaseArticoli.txt")
            n = 0
            for art in lista_articoli:
                if art['sku']==SKU_AG:
                    n += 1
            if n == 1:
                O = Operazione()
                O.aggiungiGiacenza(self.sku_ag.text(), self.numero_ag.text())
            else:
                o = QMessageBox()
                o.setWindowTitle('ERRORE')
                o.setText('SKU NON ESISTENTE')
                o.exec()


    def modifica_(self):
        SKU_MG = self.sku_mg.text()

        lista_articoli = letturaDatabaseArticoli("Model/databaseArticoli.txt")
        n = False
        for art in lista_articoli:
            if art['sku'] == SKU_MG or SKU_MG == '':
                n = True
        if n is True:
            Opp = Operazione()
            k = Opp.modificaGiacenza(int(self.id_Giacenza.text()), str(self.sku_mg.text()), str(self.numero_mg.text()),None)
            if k == True:
                p = QMessageBox()
                p.setWindowTitle('ERRORE')
                p.setText("L'operazione selezionata non è una giacenza")
                p.exec()
            elif k == 'Errore':
                u = QMessageBox()
                u.setWindowTitle('ERRORE')
                u.setText("L'operazione non esiste")
                u.exec()
        else :
            w = QMessageBox()
            w.setWindowTitle('ERRORE')
            w.setText("SKU non esiste ")
            w.exec()


        #oppp = Operazione()
        #iD = int(self.id_Giacenza.text())
        #sKu = str(self.sku_mg.text())
        #nuM = int(self.numero_mg.text())
        #oppp.modificaGiacenza(iD, sKu, nuM, None)
