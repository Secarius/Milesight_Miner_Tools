from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QDialog, QMessageBox
from gui.minertools_gui_main_window import Ui_MainWindow
from tkinter import messagebox
from numpy import genfromtxt, loadtxt
import os
import src.ssh_comms
from zipfile import ZipFile
import sys
import subprocess
import psutil
import time
#*************************** BUTTON FUNCTIONS ***************************
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
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
