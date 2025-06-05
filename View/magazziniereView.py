from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from entities.operazione import Operazione


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
        self.numero_ag.setMaximumWidth(100)
        self.numero_mg = QLineEdit()
        self.numero_ag.setMaximumWidth(100)
        self.sku_mg = QLineEdit()
        self.numero_ag.setMaximumWidth(100)
        self.id_Giacenza = QLineEdit()
        self.numero_ag.setMaximumWidth(100)
        aggiungi = QPushButton("Aggiungi")
        aggiungi.clicked.connect(self.aggiunta)
        # modifica = QPushButton("Modifica")

        layoutH5.addWidget(QLabel('NUOVA GIACENZA'))
        layoutH5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutM.addLayout(layoutH5)


        layoutH1.addWidget(QLabel('SKU:'))
        layoutH1.addWidget(self.sku_ag)
        layoutH1.addWidget(QLabel('QUANTITÀ:'))
        layoutH1.addWidget(self.numero_ag)
        layoutM.addLayout(layoutH1)

        layoutM.addWidget(aggiungi)

        # layoutH6.addWidget(QLabel('MODIFICA GIACENZA'))
        # layoutH6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # layoutM.addLayout(layoutH6)
        #
        # layoutH3.addWidget(QLabel('ID GIACENZA:'))
        # layoutH3.addWidget(self.numero_mg)
        # layoutH3.addWidget(QLabel('SKU:'))
        # layoutH3.addWidget(self.sku_mg)
        # layoutH3.addWidget(QLabel('QUANTITÀ:'))
        # layoutH3.addWidget(self.id_Giacenza)
        # layoutM.addLayout(layoutH3)
        #
        # layoutM.addWidget(modifica)
        #layoutM.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layoutM)
    def aggiunta(self):
        O = Operazione()
        x = O.aggiungiGiacenza(self.sku_ag.text(), self.numero_ag.text())
        print("operazione aggiunta")

    def modifica(self):
        pass
