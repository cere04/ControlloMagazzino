from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel,
    QMessageBox, QGroupBox, QFormLayout, QSpinBox
)
from entities.operazione import Operazione, letturaDatabaseArticoli


class FinestraM(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finestra dei Magazzinieri")
        self.setGeometry(200, 200, 700, 300)

        layoutMain = QHBoxLayout()
        layoutMain.setSpacing(20)  # Aggiunta spaziatura tra i gruppi

        # ---------- SEZIONE NUOVA GIACENZA ----------
        nuovaGiacenzaBox = QGroupBox("Nuova Giacenza")
        nuovaGiacenzaLayout = QFormLayout()
        nuovaGiacenzaLayout.setSpacing(15)  # Spaziatura interna

        self.sku_ag = QLineEdit()
        self.sku_ag.setPlaceholderText("Inserisci SKU")

        # SpinBox per la quantità con pulsanti integrati
        self.numero_ag = QSpinBox()
        self.numero_ag.setMinimum(1)
        self.numero_ag.setMaximum(10000)

        nuovaGiacenzaLayout.addRow("SKU:", self.sku_ag)
        nuovaGiacenzaLayout.addRow("Quantità:", self.numero_ag)

        btn_aggiungi = QPushButton("Aggiungi Giacenza")
        btn_aggiungi.clicked.connect(self.aggiunta)
        nuovaGiacenzaLayout.addWidget(btn_aggiungi)

        nuovaGiacenzaBox.setLayout(nuovaGiacenzaLayout)
        layoutMain.addWidget(nuovaGiacenzaBox)

        # ---------- SEZIONE MODIFICA GIACENZA ----------
        modificaBox = QGroupBox("Modifica Giacenza")
        modificaLayout = QFormLayout()
        modificaLayout.setSpacing(15)  # Spaziatura interna

        self.id_Giacenza = QLineEdit()
        self.id_Giacenza.setPlaceholderText("ID Operazione")

        self.sku_mg = QLineEdit()
        self.sku_mg.setPlaceholderText("SKU")

        # SpinBox per la quantità con pulsanti integrati
        self.numero_mg = QSpinBox()
        self.numero_mg.setMinimum(1)
        self.numero_mg.setMaximum(10000)

        modificaLayout.addRow("ID Operazione:", self.id_Giacenza)
        modificaLayout.addRow("SKU:", self.sku_mg)
        modificaLayout.addRow("Quantità:", self.numero_mg)

        btn_modifica = QPushButton("Modifica Giacenza")
        btn_modifica.clicked.connect(self.modifica_)
        modificaLayout.addWidget(btn_modifica)

        modificaBox.setLayout(modificaLayout)
        layoutMain.addWidget(modificaBox)

        self.setLayout(layoutMain)

        # ---------- STILE ----------
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f7fa;
                font-family: Arial, sans-serif;
                color: #2d3748;
            }

            /* Imposta sfondo trasparente per le etichette */
            QLabel {
                font-weight: 500;
                background-color: transparent;
            } 

            QGroupBox {
                border: 2px solid #0F4C81;
                border-radius: 8px;
                margin: 10px;
                padding: 15px;
                background-color: white;
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

            /* SpinBox styling */
            QSpinBox {
                padding: 8px;
                border: 2px solid #cccccc;
                border-radius: 8px;
                font-size: 14px;
                color: black;
                padding-right: 25px; /* Space for buttons */
                background-color: white;
            }

            QSpinBox:focus {
                border: 2px solid #3A81F1;
            }

            QSpinBox::up-button, QSpinBox::down-button {
                subcontrol-origin: border;
                subcontrol-position: center right;
                width: 16px;
                background-color: none;
            }

            QSpinBox::up-button {
                subcontrol-position: top right;
                margin-top: 2px;
                margin-right: 3px;
            }

            QSpinBox::down-button {
                subcontrol-position: bottom right;
                margin-bottom: 2px;
                margin-right: 3px;
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
        SKU_AG = self.sku_ag.text().strip()
        N_AG = self.numero_ag.value()  # Usiamo value() per lo SpinBox

        # Controllo campi vuoti
        if not SKU_AG:
            QMessageBox.critical(
                self,
                'Errore',
                'Il campo SKU deve essere compilato'
            )
            return

        # Verifica esistenza SKU
        lista_articoli = letturaDatabaseArticoli("Model/databaseArticoli.txt")
        sku_exists = any(art['sku'] == SKU_AG for art in lista_articoli)

        if not sku_exists:
            QMessageBox.critical(
                self,
                'Errore',
                f'Lo SKU "{SKU_AG}" non esiste nel database'
            )
            self.sku_ag.clear()
            return

        try:
            O = Operazione()
            O.aggiungiGiacenza(SKU_AG, N_AG)

            # Messaggio di successo
            QMessageBox.information(
                self,
                'Successo',
                f'Giacenza aggiunta con successo!\n'
                f'SKU: {SKU_AG}\n'
                f'Quantità: {N_AG}'
            )

            # Reset campi
            self.sku_ag.clear()
            self.numero_ag.setValue(1)

        except Exception as e:
            QMessageBox.critical(
                self,
                'Errore',
                f'Si è verificato un errore durante l\'aggiunta:\n{str(e)}'
            )

    def modifica_(self):
        ID_OP = self.id_Giacenza.text().strip()
        SKU_MG = self.sku_mg.text().strip()
        QTA_MG = self.numero_mg.value()  # Usiamo value() per lo SpinBox

        # Controllo campi vuoti
        if not ID_OP:
            QMessageBox.critical(
                self,
                'Errore',
                'Il campo ID Operazione deve essere compilato'
            )
            return

        if not SKU_MG:
            QMessageBox.critical(
                self,
                'Errore',
                'Il campo SKU deve essere compilato'
            )
            return

        # Controllo ID operazione valido
        try:
            id_op = int(ID_OP)
            if id_op <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.critical(
                self,
                'Errore',
                'ID Operazione deve essere un numero intero positivo'
            )
            self.id_Giacenza.clear()
            return

        # Verifica esistenza SKU
        lista_articoli = letturaDatabaseArticoli("Model/databaseArticoli.txt")
        sku_exists = any(art['sku'] == SKU_MG for art in lista_articoli)

        if not sku_exists:
            QMessageBox.critical(
                self,
                'Errore',
                f'Lo SKU "{SKU_MG}" non esiste nel database'
            )
            self.sku_mg.clear()
            return

        try:
            Opp = Operazione()
            result = Opp.modificaGiacenza(id_op, SKU_MG, QTA_MG, None)

            if result is True:
                QMessageBox.critical(
                    self,
                    'Errore',
                    "L'operazione selezionata non è una giacenza"
                )
            elif result == 'Errore':
                QMessageBox.critical(
                    self,
                    'Errore',
                    "Nessuna operazione trovata con l'ID specificato"
                )
            else:
                # Messaggio di successo
                QMessageBox.information(
                    self,
                    'Successo',
                    f'Giacenza modificata con successo!\n'
                    f'ID: {id_op}\n'
                    f'SKU: {SKU_MG}\n'
                    f'Nuova quantità: {QTA_MG}'
                )

                # Reset campi
                self.id_Giacenza.clear()
                self.sku_mg.clear()
                self.numero_mg.setValue(1)

        except Exception as e:
            QMessageBox.critical(
                self,
                'Errore',
                f'Si è verificato un errore durante la modifica:\n{str(e)}'
            )