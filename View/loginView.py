from Controllers.auth_service import AuthService
from View.magazziniereView import FinestraM
from View.commessoView import FinestraC
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QMessageBox
from View.registrazioneView import FinestraR

class Finestra1(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.setWindowTitle("Finestra Iniziale")
        self.setGeometry(200, 200, 300, 200)
        self.F1L = QVBoxLayout()
        self.setLayout(self.F1L)
        self.Inserimento = QLineEdit()
        self.Inserimento.setPlaceholderText("Codice Utente")
        self.Accedi = QPushButton("Accedi")
        self.Registrati = QPushButton("Registrati")
        #self.Accedi.clicked.connect(self.afa)
        self.Registrati.clicked.connect(self.finestraRegistrazione)
        self.F1L.addWidget(self.Inserimento)
        self.F1L.addWidget(self.Accedi)
        self.Accedi.clicked.connect(self.accesso)
        self.F1L.addWidget(self.Registrati)
        self.finestra_r = FinestraR(self)
        # self.finestraR = FinestraR()
    def accesso (self) :
        A = AuthService()
        x = A.loginUtente(self.Inserimento.text())
        if x == None:
            pp = QMessageBox()
            pp.setWindowTitle('errore')
            pp.setText("Nome utente non esistente, riprovare")
            pp.exec()
        # else:
        #     print("ok")
        elif x['ruoloUtente'] == 'Magazziniere':
            self.hide()
            self.finestra_m = FinestraM()
            self.finestra_m.show()
        elif x['ruoloUtente'] == 'Commesso':
            self.hide()
            self.finestra_c = FinestraC()
            self.finestra_c.show()
        # elif x['ruoloUtente'] == 'Responsabile Commerciale':
        #     self.hide()
        #     self.finestra_rc = FinestraRC()
        #     self.finestra_rc.show()
        # elif x['ruoloUtente'] == 'Responsabile Commerciale':
        #     self.hide()
        #     self.finestra_ad = FinestraAD()
        #     self.finestra_ad.show()
        # self.hide()
        # self.finestraA = FinestraA()
        # self.finestraA.show()
    def finestraRegistrazione (self) :
        self.finestra_r.show()
        self.hide()
        #if self.finestraR.Registrazione() == True:
            #print("ciao")
            #self.show()
            #self.finestraR.hide()



