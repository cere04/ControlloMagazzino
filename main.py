import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QStackedWidget, QFrame)
from PyQt5.QtGui import QPixmap, QFont, QFontDatabase, QColor, QPainter
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtChart import QChart, QChartView, QBarSeries, QBarSet, QPieSeries, QBarCategoryAxis, QValueAxis

from services.operation_service import (filtraOperazioni, letturaDatabaseOperazioni, letturaDatabaseArticoli, calcolaVenditeTotali)

file_operazioni = "databaseOperazioni.txt "
file_articoli = "databaseArticoli.txt "

operazioni = letturaDatabaseOperazioni(file_operazioni)
articoli = letturaDatabaseArticoli(file_articoli)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Carica il font Poppins
        self.load_fonts()

        # Configurazione finestra principale
        self.setWindowTitle("Gestione Magazzino")
        self.setGeometry(100, 100, 1200, 800)

        # Creazione widget centrale e layout principale
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Creazione header
        self.create_header(main_layout)

        # Creazione corpo principale
        self.create_main_body(main_layout)

        # Applica stile
        self.apply_style()

    def load_fonts(self):
        # Carica il font Poppins dal file (se disponibile)
        font_db = QFontDatabase()
        font_id = font_db.addApplicationFont("Poppins-Regular.ttf")  # Sostituisci con il percorso del tuo file font
        if font_id != -1:
            self.font_family = font_db.applicationFontFamilies(font_id)[0]
        else:
            # Fallback se il font non è caricato
            self.font_family = "Segoe UI"
            print("Font Poppins non trovato. Utilizzo font di fallback.")

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

        # Creazione grafico a colonne
        chart_col = self.create_bar_chart()
        chart_view_col = QChartView(chart_col)
        chart_view_col.setRenderHint(QPainter.Antialiasing)
        left_sub_block_layout.addWidget(chart_view_col)

        # Sotto-blocco destro (rapporto 1:3) - Grafico a torta
        right_sub_block = QFrame()
        right_sub_block.setFrameShape(QFrame.StyledPanel)
        right_sub_block.setObjectName("block2")
        right_sub_block_layout = QVBoxLayout(right_sub_block)

        # Creazione grafico a torta
        chart_pie = self.create_pie_chart()
        chart_view_pie = QChartView(chart_pie)
        chart_view_pie.setRenderHint(QPainter.Antialiasing)
        right_sub_block_layout.addWidget(chart_view_pie)

        top_layout.addWidget(left_sub_block, stretch=6)
        top_layout.addWidget(right_sub_block, stretch=4)

        # Blocco inferiore (40% dello spazio)
        bottom_block = QFrame()
        bottom_block.setFrameShape(QFrame.StyledPanel)
        bottom_block.setObjectName("block3")
        bottom_block_layout = QVBoxLayout(bottom_block)
        bottom_block_layout.addWidget(QLabel("Blocco 3"))

        main_layout.addWidget(top_block, stretch=5)  # 50% dello spazio
        main_layout.addWidget(bottom_block, stretch=5)  # 50% dello spazio

    def create_bar_chart(self):

        vendite_mensili = calcolaVenditeTotali(operazioni)

        mesi = ['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu',
                  'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']

        # Creazione serie di dati
        series = QBarSeries()
        bar_set = QBarSet("Vendite")
        bar_set.setColor(QColor("#4a6fa5"))  # Colore coerente con il tema

        for vendite in vendite_mensili:
            bar_set.append(vendite)

        series.append(bar_set)

        # Creazione grafico
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Vendite mensili")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Asse X
        axis_x = QBarCategoryAxis()
        axis_x.append(mesi)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        # Asse Y
        axis_y = QValueAxis()
        axis_y.setRange(0, max(vendite_mensili) + 5)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        # Stile del grafico
        chart.setBackgroundBrush(QColor("#ffffff"))
        chart.setTitleBrush(QColor("#2c3e50"))
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        return chart

    def create_pie_chart(self):
        values = [1,2,3,4,5,6,7,8,9,10,11,12]
        months = ['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu',
                  'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']

        # Creazione serie di dati
        series = QPieSeries()
        colors = [
            "#4a6fa5", "#3a5a8f", "#2a4a7f", "#1a3a6f",
            "#5a8fc5", "#4a7fb5", "#3a6fa5", "#2a5f95",
            "#1a4f85", "#0a3f75", "#5a9fd5", "#4a8fc5"
        ]

        for month, value, color in zip(months, values, colors):
            slice_ = series.append(f"{month}: {value}", value)
            slice_.setColor(QColor(color))
            slice_.setLabelVisible(False)

        # Creazione grafico
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Distribuzione vendite")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Stile del grafico
        chart.setBackgroundBrush(QColor("#ffffff"))
        chart.setTitleBrush(QColor("#2c3e50"))
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignRight)

        return chart

    def apply_style(self):
        # Stile generale con Poppins
        self.setStyleSheet(f"""
            QWidget {{
                background-color: #f8f9fa;
                color: #212529;
                font-family: '{self.font_family}', sans-serif;
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
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Verifica se il modulo QtChart è disponibile
    # try:
    #     from PyQt5.QtChart import QChart, QChartView
    # except ImportError:
    #     print("Errore: Il modulo PyQt5.QtChart non è installato.")
    #     print("Installalo con: pip install PyQtChart")
    #     sys.exit(1)

    font = QFont("Segoe UI")
    font.setPointSize(10)
    app.setFont(font)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())




# print("\nSeleziona filtri (separa numeri con virgola, 0 per nessuno):")
# print("1-SKU, 2-Genere, 3-Tipologia, 4-Paese")
# scelte = input("Scelte: ")
# scelte = {s.strip() for s in scelte.split(',')} if scelte else set()
#
# sku_vals = generi_vals = tipologia_vals = zone_vals = None
#
# if '1' in scelte:
#     sku_vals = input("Inserisci SKU (,) : ").split(',')
# if '2' in scelte:
#     generi_vals = input("Inserisci generi: ").split(',')
# if '3' in scelte:
#     tipologia_vals = input("Inserisci tipologie: ").split(',')
# if '4' in scelte:
#     zone_vals = input("Inserisci paesi/aree: ").split(',')
#
# risultati = filtraOperazioni(
#     lista_operazioni=operazioni,
#     lista_articoli=articoli,
#     sku=sku_vals,
#     generi=generi_vals,
#     tipologie=tipologia_vals,
#     zone=zone_vals
# )

# print(risultati)




# from utils import (
#     letturaDatabaseOperazioni,
#     letturaDatabaseArticoli,
#     filtraOperazioni
# )
#
# file_operazioni = input("../databaseOperazioni.txt): ")
# file_articoli = input("../databaseArticoli.txt): ")
#
# operazioni = letturaDatabaseOperazioni(file_operazioni)
# articoli = letturaDatabaseArticoli(file_articoli)
#
# print("\nSeleziona filtri (separa numeri con virgola, 0 per nessuno):")
# print("1-SKU, 2-Genere, 3-Tipologia, 4-Paese")
# scelte = input("Scelte: ")
# scelte = {s.strip() for s in scelte.split(',')} if scelte else set()
#
# sku_vals = generi_vals = tipologia_vals = zone_vals = None
#
# if '1' in scelte:
#     sku_vals = input("Inserisci SKU (,) : ").split(',')
# if '2' in scelte:
#     generi_vals = input("Inserisci generi: ").split(',')
# if '3' in scelte:
#     tipologia_vals = input("Inserisci tipologie: ").split(',')
# if '4' in scelte:
#     zone_vals = input("Inserisci paesi/aree: ").split(',')
#
# risultati = filtraOperazioni(
#     lista_operazioni=operazioni,
#     lista_articoli=articoli,
#     sku=sku_vals,
#     generi=generi_vals,
#     tipologie=tipologia_vals,
#     zone=zone_vals
# )