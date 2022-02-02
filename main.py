from msilib.schema import ComboBox
import os,sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from gui.minertools_gui_main_window import Ui_MainWindow
from tkinter import messagebox
from numpy import genfromtxt, loadtxt
import os
import src.ssh_comms

#*************************** BUTTON FUNCTIONS ***************************
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowIcon(QtGui.QIcon('assets/helium.ico'))
        self.setupUi(self)
            
def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    win.updatecombo()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
