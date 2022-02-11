from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QDialog, QMessageBox
from gui.mac_gui import Ui_MainWindow
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
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Window(QMainWindow, Ui_MainWindow):
    """A dummy docstring."""
    def __init__(self, parent=None):
        """A dummy docstring."""
        super().__init__(parent)
        self.setWindowIcon(QtGui.QIcon('assets/helium.ico'))
        self.setupUi(self)
            
def main():
    """A dummy docstring."""
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    win.updatecombo()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
 