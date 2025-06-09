from Controllers.auth_service import AuthService
from View.adminView import adminWindow
from View.magazziniereView import FinestraM
from View.commessoView import FinestraC
from View.registrazioneView import FinestraR
from View.responsabileView import FinestraRC
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QMessageBox, QMainWindow

class Finestra1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finestra Iniziale")
        self.setGeometry(200, 200, 300, 200)
        layout = QVBoxLayout(self)

        self.Inserimento = QLineEdit()
        self.Inserimento.setPlaceholderText("Codice Utente")
        layout.addWidget(self.Inserimento)

        self.Accedi = QPushButton("Accedi")
        layout.addWidget(self.Accedi)
        self.Accedi.clicked.connect(self.accesso)

        self.Registrati = QPushButton("Registrati")
        layout.addWidget(self.Registrati)
        self.Registrati.clicked.connect(self.finestraRegistrazione)

        self.finestra_r = FinestraR(self)

    def finestraRegistrazione(self):
        self.finestra_r.show()

    def accesso(self):
        codice = self.Inserimento.text().strip()
        A = AuthService()
        user = A.loginUtente(codice)

        if user is None:
            QMessageBox.critical(self, "Errore", "Nome utente non esistente, riprovare")
            return

        ruolo = user.get('ruoloUtente')
        self.hide()

        if ruolo == 'Magazziniere':
            self.finestra_m = FinestraM()
            self.finestra_m.show()

        elif ruolo == 'Commesso':
            self.finestra_c = FinestraC()
            self.finestra_c.show()

        elif ruolo == 'Responsabile Commerciale':
            self.finestra_rc = FinestraRC()
            self.finestra_rc.show()

        elif ruolo == 'Amministratore':
            self.finestra_a = QMainWindow()
            self.ui_admin = adminWindow()
            self.ui_admin.setupUi(self.finestra_a)
            self.finestra_a.show()

        else:
            QMessageBox.warning(self, "Ruolo sconosciuto", f"Ruolo '{ruolo}' non gestito.")