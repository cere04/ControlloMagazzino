from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QFrame, QComboBox, QLineEdit, QMessageBox)
from PyQt5.QtGui import QFontDatabase, QColor, QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtChart import QChart, QChartView, QBarSeries, QBarSet, QPieSeries, QBarCategoryAxis, QValueAxis
from Controllers.operation_service import (filtraOperazioni, calcolaVenditeTotali, calcolaGiacenzaMedia)
from entities.operazione import (letturaDatabaseArticoli, letturaDatabaseOperazioni, Operazione)
from entities.articolo import Articolo
from entities.enums import GenereArticolo, TipologiaArticolo, TipoOperazione, Zone
from datetime import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.fileOperazioni = "Model/databaseOperazioni.txt "
        self.fileArticoli = "Model/databaseArticoli.txt "
        self.operazioni = letturaDatabaseOperazioni(self.fileOperazioni)
        self.articoli = letturaDatabaseArticoli(self.fileArticoli)

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Gestione Magazzino")
        self.setGeometry(100, 100, 1500, 900)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.create_header(main_layout)
        self.create_main_body(main_layout)
        self.apply_style()

    # def load_fonts(self):
    #     # Carica il font Poppins dal file (se disponibile)
    #     font_db = QFontDatabase()
    #     font_id = font_db.addApplicationFont("Poppins-Regular.ttf")  # Sostituisci con il percorso del tuo file font
    #     if font_id != -1:
    #         self.font_family = font_db.applicationFontFamilies(font_id)[0]
    #     else:
    #         # Fallback se il font non è caricato
    #         self.font_family = "Segoe UI"
    #         print("Font Poppins non trovato. Utilizzo font di fallback.")

    def create_header(self, main_layout):
        # Widget per l'header
        header = QWidget()
        header.setObjectName("header")
        header.setFixedHeight(64)
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(40, 0, 40, 0)

        # Pulsante login/account (stile moderno)
        self.auth_button = QPushButton("Accedi / Registrati")
        self.auth_button.setCursor(Qt.PointingHandCursor)
        self.auth_button.setFixedSize(180, 40)
        self.auth_button.setObjectName("authButton")

        # Aggiungi elementi all'header
        header_layout.addStretch()
        header_layout.addWidget(self.auth_button)
        # Aggiungi header al layout principale
        main_layout.addWidget(header)

    def create_main_body(self, main_layout):
        top_block = QWidget()
        top_block.setObjectName("topBlock")
        top_layout = QHBoxLayout(top_block)
        top_layout.setContentsMargins(20, 20, 20, 20)
        top_layout.setSpacing(0)

        # Sotto-blocco sinistro (rapporto 2:3) - Grafico a colonne
        left_sub_block = QFrame()
        left_sub_block.setFrameShape(QFrame.StyledPanel)
        left_sub_block.setObjectName("block1")
        left_sub_block_layout = QVBoxLayout(left_sub_block)

        # Container per i combo box allineati a destra
        combo_container = QWidget()
        combo_layout = QHBoxLayout(combo_container)
        combo_layout.setContentsMargins(0, 0, 0, 0)
        combo_layout.setSpacing(10)

        # Aggiungi stretch a sinistra per allineare i combo a destra
        combo_layout.addStretch()

        self.filterComboGenere = QComboBox()
        self.filterComboTipologia = QComboBox()
        self.filterComboZona = QComboBox()
        self.filterComboSku=QLineEdit()

        self.filterComboGenere.setFixedSize(150, 40)
        self.filterComboTipologia.setFixedSize(150, 40)
        self.filterComboZona.setFixedSize(150, 40)
        self.filterComboSku.setFixedSize(150, 40)
        self.filterComboGenere.setObjectName("filterGenere")
        self.filterComboTipologia.setObjectName("filterTipologia")
        self.filterComboZona.setObjectName("filterZona")
        self.filterComboSku.setObjectName("filterSku")

        # for genere in GenereArticolo:
        #     self.filterComboGenere.addItem(genere.name.capitalize(), genere.value)
        #
        # for tipologia in TipologiaArticolo:
        #     self.filterComboTipologia.addItem(tipologia.name.capitalize(), tipologia.value)
        #
        # for zona in Zone:
        #     self.filterComboZona.addItem(zona.name.capitalize(), zona.value)

        for combo, items, label in [
            (self.filterComboGenere, GenereArticolo, "Seleziona Genere"),
            (self.filterComboTipologia, TipologiaArticolo, "Seleziona Topologia"),
            (self.filterComboZona, Zone, "Seleziona Zona")
        ]:
            combo.addItem(label, None)  # Usa None come valore per "Tutti"
            for item in items:
                combo.addItem(item.name.capitalize(), item.value)
            combo.setCurrentIndex(0)

        combo_layout.addWidget(self.filterComboSku)
        combo_layout.addWidget(self.filterComboZona)
        combo_layout.addWidget(self.filterComboGenere)
        combo_layout.addWidget(self.filterComboTipologia)

        # Aggiungi il container dei combo al layout principale del blocco sinistro
        left_sub_block_layout.addWidget(combo_container, alignment=Qt.AlignRight)

        # Creazione grafico a colonne
        chart_col = self.create_bar_chart()
        chart_view_col = QChartView(chart_col)
        chart_view_col.setRenderHint(QPainter.Antialiasing)
        left_sub_block_layout.addWidget(chart_view_col)

        # Sotto-blocco destro (rapporto 1:3)
        right_sub_block = QFrame()
        right_sub_block.setFrameShape(QFrame.StyledPanel)
        right_sub_block.setObjectName("block2")
        right_sub_block_layout = QVBoxLayout(right_sub_block)
        right_sub_block_layout.addWidget(QLabel("Blocco 2"))

        # Creazione grafico a torta
        # chart_pie = self.create_pie_chart()
        # chart_view_pie = QChartView(chart_pie)
        # chart_view_pie.setRenderHint(QPainter.Antialiasing)
        # right_sub_block_layout.addWidget(chart_view_pie)

        top_layout.addWidget(left_sub_block, stretch=6)
        top_layout.addWidget(right_sub_block, stretch=4)

        # Blocco inferiore 50%
        bottom_block = QFrame()
        bottom_block.setFrameShape(QFrame.StyledPanel)
        bottom_block.setObjectName("block3")
        bottom_block_layout = QVBoxLayout(bottom_block)

        # Form per inserimento vendite
        form_widget = QWidget()
        form_layout = QVBoxLayout(form_widget)
        form_layout.setContentsMargins(20, 20, 20, 20)

        # Campo SKU
        sku_layout = QHBoxLayout()
        sku_label = QLabel("SKU Articolo:")
        self.sku_input = QLineEdit()
        sku_layout.addWidget(sku_label)
        sku_layout.addWidget(self.sku_input)
        form_layout.addLayout(sku_layout)

        # Campo Quantità
        quantita_layout = QHBoxLayout()
        quantita_label = QLabel("Quantità Venduta:")
        self.quantita_input = QLineEdit()
        quantita_layout.addWidget(quantita_label)
        quantita_layout.addWidget(self.quantita_input)
        form_layout.addLayout(quantita_layout)

        # Campo Paese
        paese_layout = QHBoxLayout()
        paese_label = QLabel("Paese:")
        self.paese_input = QLineEdit()
        paese_layout.addWidget(paese_label)
        paese_layout.addWidget(self.paese_input)
        form_layout.addLayout(paese_layout)

        # Pulsante Inserimento
        inserisci_btn = QPushButton("Inserisci Vendita")
        inserisci_btn.setCursor(Qt.PointingHandCursor)
        inserisci_btn.clicked.connect(self.inserisciDatiVendita)
        form_layout.addWidget(inserisci_btn)

        main_layout.addWidget(top_block, stretch=5)
        bottom_block_layout.addWidget(form_widget)
        main_layout.addWidget(bottom_block, stretch=5)

    def inserisciDatiVendita(self):
        sku = self.sku_input.text().strip()
        quantita = self.quantita_input.text().strip()
        paese = self.paese_input.text().strip()

        # Validazione input
        if not sku or not quantita or not paese:
            QMessageBox.critical(self, "Errore", "Compilare tutti i campi")
            return

        # Verifica esistenza SKU
        articolo_data = next((a for a in self.articoli if a['sku'] == sku), None)
        if not articolo_data:
            QMessageBox.critical(self, "Errore", "SKU non trovato")
            return

        # Conversione quantità
        try:
            quantita = int(quantita)
            if quantita <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.critical(self, "Errore", "Quantità non valida")
            return

        # Generazione ID autoincrement
        nuovo_id = max(op['idOperazione'] for op in self.operazioni) + 1 if self.operazioni else 1

        try:
            # Creazione oggetti
            # articolo = Articolo(
            #     sku=articolo_data['sku'],
            #     genere=articolo_data['genere'],
            #     tipologia=articolo_data['tipologia']
            # )

            # Creazione e salvataggio operazione
            operazione = Operazione(
                id=nuovo_id,
                tipo=TipoOperazione.VENDITA,
                quantitaVendita=quantita,
                quantitaGiacenza=quantita*-1,
                data=datetime.now(),
                articolo="922WE",
                paese=paese
            )
            operazione.aggiungiVendita(self.tipo, self.quantitaVendita)
            # Aggiornamento dati e UI
            self.operazioni = letturaDatabaseOperazioni(self.file_operazioni)
            self.sku_input.clear()
            self.quantita_input.clear()
            self.paese_input.clear()
            QMessageBox.information(self, "Successo", "Operazione salvata")

        except Exception as e:
            QMessageBox.critical(self, "Errore", f"Errore salvataggio000: {str(e)}")

    def _connect_filters(self):
        """Collega i segnali dei filtri all'aggiornamento del grafico"""
        self.filterComboGenere.currentIndexChanged.connect(self.update_chart)
        self.filterComboTipologia.currentIndexChanged.connect(self.update_chart)
        self.filterComboZona.currentIndexChanged.connect(self.update_chart)
        self.filterComboSku.textChanged.connect(self.update_chart)

    def update_chart(self):
        """Aggiorna il grafico con i filtri correnti"""
        new_chart = self.create_bar_chart()
        self.chart_view.setChart(new_chart)

    def create_bar_chart(self):

        operazioni=letturaDatabaseOperazioni("Model/databaseOperazioni.txt")
        articoli=letturaDatabaseArticoli("Model/databaseArticoli.txt")

        sku = self.filterComboSku.text().strip() or None
        genere = self.filterComboGenere.currentData()
        tipologia = self.filterComboTipologia.currentData()
        zona = self.filterComboZona.currentData()

        filtered_operazioni = filtraOperazioni(
            lista_operazioni=operazioni,
            lista_articoli=articoli,
            sku=sku,
            generi=genere,
            tipologie=tipologia,
            zone=zona
        )

        venditeMensili = calcolaVenditeTotali(filtered_operazioni)
        giacenzaMedia= calcolaVenditeTotali(filtered_operazioni)

        mesi = ['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu',
                  'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']

        # Creazione grafico
        chart = QChart()
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Crea due bar set (colonne) diversi
        bar_set1 = QBarSet("Vendite")  # Prima colonna (originale)
        bar_set2 = QBarSet("Altri Dati")  # Seconda colonna (nuova)
        bar_set1.append(venditeMensili)
        bar_set2.append(giacenzaMedia)

        # Personalizza i colori
        bar_set1.setBrush(QColor("#3498db"))  # Blu originale
        bar_set2.setBrush(QColor("#f1c40f"))  # Giallo nuova colonna

        # Crea la serie di barre e aggiungi entrambi i set
        series = QBarSeries()
        series.append(bar_set1)
        series.append(bar_set2)
        chart.addSeries(series)

        # Asse X
        axis_x = QBarCategoryAxis()
        axis_x.append(mesi)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        # Asse Y
        max_val = max(venditeMensili)
        axis_y = QValueAxis()
        axis_y.setRange(0, max_val + 5)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        # Stile del grafico
        chart.setBackgroundBrush(QColor("transparent"))
        chart.setTitleBrush(QColor("#2c3e50"))
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        return chart

    def apply_style(self):
        # Stile generale con Poppins
        self.setStyleSheet(f"""
            QWidget {{
                background-color: #f8f9fa;
                color: #212529;
                font-family: 'Segoe UI', sans-serif;
            }}

            /* Header */
            QWidget#header {{
                background-color: transparent;
                border-bottom: 1px solid #C8CBD9;
            }}

            /* Pulsante login */
            QPushButton#authButton {{
                background-color: #4a6fa5;
                color: white;
                border: none;
                border-radius: 20px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: 400;
            }}

            QPushButton#authButton:hover {{
                background-color: #3a5a8f;
            }}

            QPushButton#authButton:pressed {{
                background-color: #2a4a7f;
            }}
            
            /* Stile per QComboBox */
            QComboBox {{
                background-color: #ffffff;
                border: 1px solid #C8CBD9;
                border-radius: 4px;
                padding: 4px 0px 4px 8px;
                font-size: 14px;
                color: #212529;
                min-height: 30px;
            }}
            
            QComboBox:hover {{
                border-color: #a0a4b0;
            }}
    
            QComboBox:on {{  /* Quando il menu è aperto */
                border-color: #4a6fa5;
            }}
    
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: right center;
                width: 24px;
                border-left: 1px solid #C8CBD9;
            }}
    
            QComboBox::down-arrow {{
                image: url(images/arrow-down.svg);
                width: 12px;
                height: 12px;
            }}
    
            QComboBox QAbstractItemView {{
                border: 1px solid #C8CBD9;
                background: #ffffff;
                selection-background-color: #4a6fa5;
                selection-color: #ffffff;
                outline: 0;
                padding: 4px 0;
            }}
    
            QComboBox QAbstractItemView::item {{
                min-height: 30px;
                padding: 4px 12px;
            }}
    
            QComboBox QAbstractItemView::item:hover {{
                background-color: #e9f2fa;
            }}
    
            /* Stile per stato disabilitato */
            QComboBox:disabled {{
                background-color: #f1f3f5;
                color: #868e96;
                border-color: #dee2e6;
            }}

            QFrame {{
                border: none;
            }}

            QFrame#block1 {{
                border-right: 1px solid #C8CBD9;
                border-bottom: 1px solid #C8CBD9;
            }}

            QFrame#block2 {{
                border-bottom: 1px solid #C8CBD9;
            }}

            QLabel {{
                font-size: 16px;
                color: #333333;
            }}
            
            QLabel {{
                font-size: 16px;
                color: #333333;
            }}
        
            /* Stile sezione aggiungi vendita */
            QFrame#block3 {{
                background-color: #ffffff;
            }}
        
            QLineEdit {{
                background-color: #ffffff;
                border: 1px solid #C8CBD9;
                border-radius: 4px;
                padding: 4px 0px 4px 8px;
                font-size: 14px;
                color: #212529;
                min-height: 30px;
            }}
        
            QLineEdit:hover {{
                border-color: #a0a4b0;
            }}
        
            QLineEdit:focus {{
                border-color: #4a6fa5;
                background-color: #f8fbff;
            }}
        
            QPushButton[text="Inserisci Vendita"] {{
                background-color: #2ecc71;
                color: white;
                border: none;
                border-radius: 20px;
                padding: 12px 24px;
                font-size: 14px;
                font-weight: 500;
                margin-top: 16px;
            }}
        
            QPushButton[text="Inserisci Vendita"]:hover {{
                background-color: #27ae60;
            }}
        
            QPushButton[text="Inserisci Vendita"]:pressed {{
                background-color: #219a52;
            }}
        """)

    def ottieniLivelloAccesso(self):
        pass
