from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel,
    QMessageBox, QGroupBox, QFormLayout, QSpinBox, QComboBox
)
from entities.operazione import Operazione, letturaDatabaseArticoli


class FinestraC(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finestra dei Commessi")
        self.setGeometry(200, 200, 700, 300)

        layoutMain = QHBoxLayout()
        layoutMain.setSpacing(20)  # Added spacing between groups

        nuovaVenditaBox = QGroupBox("Nuova Vendita")
        nuovaVenditaLayout = QFormLayout()
        nuovaVenditaLayout.setSpacing(15)

        self.sku_av = QLineEdit()
        self.sku_av.setPlaceholderText("Inserisci SKU")

        # SpinBox per la quantità invece di QLineEdit
        self.numero_av = QSpinBox()
        self.numero_av.setMinimum(1)
        self.numero_av.setMaximum(10000)

        # ComboBox per il paese con i paesi specificati
        self.paese_av = QComboBox()
        self.paese_av.addItem("Italia")
        self.paese_av.addItem("Germania")
        self.paese_av.addItem("Francia")
        self.paese_av.addItem("Spagna")
        self.paese_av.setCurrentIndex(-1)  # Nessuna selezione iniziale

        nuovaVenditaLayout.addRow("SKU:", self.sku_av)
        nuovaVenditaLayout.addRow("Quantità:", self.numero_av)
        nuovaVenditaLayout.addRow("Paese:", self.paese_av)

        btn_aggiungi = QPushButton("Aggiungi Vendita")
        btn_aggiungi.clicked.connect(self.aggiunta)
        nuovaVenditaLayout.addWidget(btn_aggiungi)

        nuovaVenditaBox.setLayout(nuovaVenditaLayout)
        layoutMain.addWidget(nuovaVenditaBox)

        # ---------- SEZIONE MODIFICA VENDITA ----------
        modificaVenditaBox = QGroupBox("Modifica Vendita")
        modificaVenditaLayout = QFormLayout()
        modificaVenditaLayout.setSpacing(15)

        self.id_Vendita = QLineEdit()
        self.id_Vendita.setPlaceholderText("ID Vendita")

        self.sku_mv = QLineEdit()
        self.sku_mv.setPlaceholderText("SKU")

        # SpinBox per la quantità invece di QLineEdit
        self.numero_mv = QSpinBox()
        self.numero_mv.setMinimum(1)
        self.numero_mv.setMaximum(10000)

        # ComboBox per il paese con i paesi specificati
        self.paese_mv = QComboBox()
        self.paese_mv.addItem("Italia")
        self.paese_mv.addItem("Germania")
        self.paese_mv.addItem("Francia")
        self.paese_mv.addItem("Spagna")
        self.paese_mv.setCurrentIndex(-1)  # Nessuna selezione iniziale

        modificaVenditaLayout.addRow("ID Vendita:", self.id_Vendita)
        modificaVenditaLayout.addRow("SKU:", self.sku_mv)
        modificaVenditaLayout.addRow("Quantità:", self.numero_mv)
        modificaVenditaLayout.addRow("Paese:", self.paese_mv)

        btn_modifica = QPushButton("Modifica Vendita")
        btn_modifica.clicked.connect(self.modifica_v_)
        modificaVenditaLayout.addWidget(btn_modifica)

        modificaVenditaBox.setLayout(modificaVenditaLayout)
        layoutMain.addWidget(modificaVenditaBox)

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
            
            /* ComboBox styling */
            QComboBox {
                padding: 8px;
                border: 2px solid #cccccc;
                border-radius: 8px;
                font-size: 14px;
                color: black;
                background-color: white;
            }

            QComboBox:focus {
                border: 2px solid #3A81F1;
            }
            
            QComboBox QAbstractItemView {
                border: 2px solid #cccccc;
                border-radius: 8px;
                padding: 8px;
                background: white;
                selection-background-color: #0F4C81;
                selection-color: white;
            }
            
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: center right;
                width: 15px;
                background: none;
                margin-right: 4px;
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
            QLabel {
                font-weight: 500;
            }
        """)

    def aggiunta(self):
        SKU_AV = self.sku_av.text().strip()
        N_AV = self.numero_av.value()  # Ora usiamo value() per lo SpinBox
        P_AV = self.paese_av.currentText().strip()  # Ora usiamo currentText() per ComboBox

        # Controllo campi vuoti
        if not SKU_AV:
            QMessageBox.critical(
                self,
                'Errore',
                'Il campo SKU deve essere compilato'
            )
            return

        if P_AV == "":
            QMessageBox.critical(
                self,
                'Errore',
                'Seleziona un paese'
            )
            return

        # Verifica esistenza SKU
        lista_articoli = letturaDatabaseArticoli("Model/databaseArticoli.txt")
        sku_exists = any(art['sku'] == SKU_AV for art in lista_articoli)

        if not sku_exists:
            QMessageBox.critical(
                self,
                'Errore',
                f'Lo SKU "{SKU_AV}" non esiste nel database'
            )
            self.sku_av.clear()
            return

        try:
            O = Operazione()
            O.aggiungiVendita(SKU_AV, N_AV, P_AV)

            # Messaggio di successo
            QMessageBox.information(
                self,
                'Successo',
                f'Vendita aggiunta con successo!\n'
                f'SKU: {SKU_AV}\n'
                f'Quantità: {N_AV}\n'
                f'Paese: {P_AV}'
            )

            # Reset campi
            self.sku_av.clear()
            self.numero_av.setValue(1)
            self.paese_av.setCurrentIndex(-1)

        except Exception as e:
            QMessageBox.critical(
                self,
                'Errore',
                f'Si è verificato un errore durante l\'aggiunta:\n{str(e)}'
            )

    def modifica_v_(self):
        ID_OP = self.id_Vendita.text().strip()
        SKU_MV = self.sku_mv.text().strip()
        QTA_MV = self.numero_mv.value()  # Ora usiamo value() per lo SpinBox
        PAESE_MV = self.paese_mv.currentText().strip()  # Ora usiamo currentText() per ComboBox

        # Controllo campi vuoti
        if not ID_OP:
            QMessageBox.critical(
                self,
                'Errore',
                'Il campo ID Vendita deve essere compilato'
            )
            return

        if not SKU_MV:
            QMessageBox.critical(
                self,
                'Errore',
                'Il campo SKU deve essere compilato'
            )
            return

        if PAESE_MV == "":
            QMessageBox.critical(
                self,
                'Errore',
                'Seleziona un paese'
            )
            return

        # Controllo ID vendita valido
        try:
            id_vendita = int(ID_OP)
            if id_vendita <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.critical(
                self,
                'Errore',
                'ID Vendita deve essere un numero intero positivo'
            )
            self.id_Vendita.clear()
            return

        # Verifica esistenza SKU
        lista_articoli = letturaDatabaseArticoli("Model/databaseArticoli.txt")
        sku_exists = any(art['sku'] == SKU_MV for art in lista_articoli)

        if not sku_exists:
            QMessageBox.critical(
                self,
                'Errore',
                f'Lo SKU "{SKU_MV}" non esiste nel database'
            )
            self.sku_mv.clear()
            return

        try:
            OpP = Operazione()
            risultato = OpP.modificaVendita(id_vendita, SKU_MV, QTA_MV, PAESE_MV)

            if risultato is True:
                QMessageBox.critical(
                    self,
                    'Errore',
                    "L'operazione selezionata non è una vendita"
                )
            elif risultato == 'non trovato':
                QMessageBox.critical(
                    self,
                    'Errore',
                    "Nessuna vendita trovata con l'ID specificato"
                )
            else:
                # Messaggio di successo
                QMessageBox.information(
                    self,
                    'Successo',
                    f'Vendita modificata con successo!\n'
                    f'ID: {id_vendita}\n'
                    f'SKU: {SKU_MV}\n'
                    f'Quantità: {QTA_MV}\n'
                    f'Paese: {PAESE_MV}'
                )

                # Reset campi
                self.id_Vendita.clear()
                self.sku_mv.clear()
                self.numero_mv.setValue(1)
                self.paese_mv.setCurrentIndex(-1)

        except Exception as e:
            QMessageBox.critical(
                self,
                'Errore',
                f'Si è verificato un errore durante la modifica:\n{str(e)}'
            )