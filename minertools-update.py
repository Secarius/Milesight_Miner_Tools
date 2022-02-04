from zipfile import ZipFile
import sys
import subprocess
from asyncio import subprocess
from subprocess import Popen
import psutil
import pathlib
import time
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Updateing ...")
        MainWindow.resize(250, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # create label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 25, 200, 200))
        self.label.setMinimumSize(QtCore.QSize(200, 200))
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        self.label.setObjectName("label")

        # add label to main window
        MainWindow.setCentralWidget(self.centralwidget)

        # set qmovie as label
        self.movie = QMovie("assets/updating.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        updatepath = pathlib.Path().resolve()
        print(updatepath)
        wait_until()
        print("unzipping .......................")
        with ZipFile('miner-update.zip', 'r') as zipOjk:
            zipOjk.extractall()
        updater = str(updatepath)
        print(updater + "\\MinerTools.exe")
        Popen('%s\\MinerTools.exe' % updater)
        myfile="miner-update.zip"
        ## If file exists, delete it ##
        if os.path.isfile(myfile):
            os.remove(myfile)
        else:    ## Show an error ##
            print("Error: %s file not found" % myfile)
        myfile="updater.zip"
        ## If file exists, delete it ##
        if os.path.isfile(myfile):
            os.remove(myfile)
        else:    ## Show an error ##
            print("Error: %s file not found" % myfile)
        sys.exit()

def wait_until():
    while True:
        if ("MinerTools.exe" in (p.name() for p in psutil.process_iter())): 
            time.sleep(5)
            print("läuft")
        else:
            print("läuft nicht")
            return False



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

