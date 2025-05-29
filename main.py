import sys
from PyQt6 import QtWidgets
from View.loginView import Finestra1

# class MainWindow(QtWidgets.QMainWindow, Finestra1):
#     def __init__(self, *args, obj=None, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
window = Finestra1()
window.show()
app.exec()

#main crea login window, da login viene resitituto l'oggetto e poi viene mostrata la rispettiva view


# creare pagina responsabile commerciale, amministratore, creazione account
# implementare in comessoView il metodo modificaVendita e in magazziniereView il metodo modificaGiacenza