from zipfile import ZipFile
import sys
import subprocess
from asyncio import subprocess
from subprocess import Popen
import psutil
import pathlib
import time
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Miner Tools Updater'
        self.left = 500
        self.top = 500
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('assets/update.jpeg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        
        self.show()
        time.sleep(5)
        update_start()

def update_start():
    print("Update Started")
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

