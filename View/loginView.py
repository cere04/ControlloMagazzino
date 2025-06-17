from Controllers.auth_service import AuthService
from View.adminView import adminWindow
from View.magazziniereView import FinestraM
from View.commessoView import FinestraC
from View.registrazioneView import FinestraR
from View.responsabileView import FinestraRC
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QMessageBox, QMainWindow, QLabel

class Finestra1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finestra Iniziale")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout(self)

        self.label_login = QLabel("Login")
        self.label_login.setObjectName("TitoloLogin")
        self.label_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_login)

        self.Inserimento = QLineEdit()
        self.Inserimento.setPlaceholderText("Codice Utente")
        layout.addWidget(self.Inserimento)

        self.Accedi = QPushButton("Accedi")
        layout.addWidget(self.Accedi)
        self.Accedi.clicked.connect(self.accesso)

        self.Registrati = QPushButton("Registrati")
        self.Registrati.setObjectName("Registrati")
        layout.addWidget(self.Registrati)
        self.Registrati.clicked.connect(self.finestraRegistrazione)

        self.finestra_r = FinestraR(self)

        # ✅ Applica stile coerente
        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
                color: black;
            }
            
            QLabel#TitoloLogin {
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 10px;
                color: #0F4C81;
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

            QPushButton#Registrati {
                background-color: transparent;
                color: #0F4C81;
                text-decoration: underline;
                font-weight: normal;
            }

            QPushButton#Registrati:hover {
                color: #1666AA;
            }

            QMessageBox {
                background-color: white;
            }
        """)

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
