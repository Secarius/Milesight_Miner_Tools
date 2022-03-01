import sys
import os
from tkinter import messagebox
from zipfile import ZipFile
import subprocess
import time
import psutil
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QDialog, QMessageBox
from numpy import genfromtxt, loadtxt
from gui.minertools_gui_main_window import Ui_MainWindow
import src.ssh_comms
#*************************** BUTTON FUNCTIONS ***************************
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

class Window(QMainWindow, Ui_MainWindow):
    """A dummy docstring."""
    def __init__(self, parent=None):
        """A dummy docstring."""
        super().__init__(parent)
        self.setWindowIcon(QtGui.QIcon('assets/helium.ico'))
        self.setupUi(self)
            
def main():
    """A dummy docstring."""
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    win.updatecombo()
    win.check_update()
    win.howto()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
