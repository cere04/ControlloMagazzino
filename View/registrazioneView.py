
from PyQt6.QtCore import Qt
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton,QHBoxLayout,QVBoxLayout, QTableWidget,
    QGridLayout, QLineEdit, QLabel, QComboBox, QMessageBox)
from PyQt6 import QtCore, QtGui, QtWidgets
from Controllers.auth_service import AuthService


class FinestraR(QWidget):
    def __init__(self, loginView):
        super().__init__()
        self.loginView = loginView
        self.finestra_1 = None
        self.setWindowTitle("Finestra di Registrazione")
        self.setGeometry(200, 200, 300, 200)
        self.LA = QGridLayout()
        self.setLayout(self.LA)
        #self.Main_window = QWidget()
        self.VL1 = QVBoxLayout()
        self.VL2 = QVBoxLayout()
        # VL3 = QVBoxLayout()
        self.VL4 = QVBoxLayout()
        self.VL3 = QVBoxLayout()
        self.LA.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # VL1.setAlignment(Qt.AlignTop)

        #self.PW = QLineEdit()
        #self.PW.setEchoMode(QLineEdit.Password)
        #Main_window.setLayout(LA)
        self.LA.addLayout(self.VL1, 1, 0)
        self.LA.addLayout(self.VL2, 1, 1)
        self.LA.addLayout(self.VL3, 1, 2)
        self.LA.addLayout(self.VL4, 0, 0)
        # LA.addLayout(VL5,2,0)
        #p = QLabel('INSERIRE NOME COGNOME E RUOLO')

        self.LA.addWidget(QLabel('INSERIRE NOME COGNOME E RUOLO'), 0, 0)
        self.Label1 = QLineEdit()
        self.Label2 = QLineEdit()
        self.label3 = QComboBox()
        #self.ruolo = ["Magazziniere", "Commesso", "Responsabile  Commerciale"]
        #for r in self.ruolo :
            #self.label3.addItems(r)
        self.label3.addItem("Magazziniere")
        self.label3.addItem("Commesso")
        self.label3.addItem("Responsabile Commerciale")
        self.Label1.setPlaceholderText("Mario")
        self.Label2.setPlaceholderText("Rossi")
        self.VL1.addWidget(QLabel('NOME'))
        self.VL1.addWidget(self.Label1)
        self.VL2.addWidget(QLabel('COGNOME'))

        # VL1.setContentsMargins(10,10,10,10)
        # VL1.setSpacing(200)
        self.VL2.addWidget(self.Label2)
        # VL3.addWidget(QLabel('Nome Utente'))
        # VL3.addWidget(PW)
        self.VL3.addWidget(QLabel('RUOLO'))
        self.VL3.addWidget(self.label3)
        self.ButtonA = QPushButton('Registrati')
        self.LA.addWidget(self.ButtonA, 3, 2)
        self.ButtonA.clicked.connect(self.Registrazione)
    def Registrazione (self) :
        #nome = self.Label1.text()
        #cognome = self.Label2.text()
        #ruolo = self.label3.currentText()
        b = AuthService()
        f = b.aggiungiUtenti(self.Label1.text(), self.Label2.text(), self.label3.currentText())
        a = QMessageBox()
        a.setWindowTitle('Nome Utente')
        a.setText('Registrazione avvenuta con successo \nIl tuo nome Utente è:'+ f )
        a.exec()
        self.hide()
        #self.finestra_1 = Finestra1()
        self.loginView.show()

