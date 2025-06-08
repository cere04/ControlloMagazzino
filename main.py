import sys
from PyQt6 import QtWidgets
from View.loginView import Finestra1
from View.adminView import adminWindow


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     login = Finestra1()
#     login.show()
#     sys.exit(app.exec())

# class MainWindow(QtWidgets.QMainWindow, Finestra1):
#      def __init__(self, *args, obj=None, **kwargs):
#          super().__init__(*args, **kwargs)
#          self.setupUi(self)
# app = QtWidgets.QApplication(sys.argv)
# window = Finestra1()
# window.show()
# app.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()  # Crea una finestra principale
    ui = adminWindow()                    # Istanza della tua classe UI
    ui.setupUi(MainWindow)               # Setup della UI nella QMainWindow

    MainWindow.show()                    # Mostra la finestra
    sys.exit(app.exec())                 # Avvia l'app

#main crea login window, da login viene resitituto l'oggetto e poi viene mostrata la rispettiva view



# importante!!!!! inserire controllo per vendita maggiore della giacenza effettiva
#sistemare modificaVendita/Giacenza
# creare pagina responsabile commerciale, amministratore, creazione account
# implementare in comessoView il metodo modificaVendita e in magazziniereView il metodo modificaGiacenza