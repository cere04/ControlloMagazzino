from PyQt6.QtWidgets import QWidget


class FinestraRC(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.setWindowTitle("Finestra Responsabile Commerciale")
        self.setGeometry(200, 200, 300, 200)