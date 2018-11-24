from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Controller import Controller

if __name__=="__main__":
    app=QApplication(sys.argv)

    window=QMainWindow()
    controller=Controller(window)
    window.show()
    sys.exit(app.exec())

