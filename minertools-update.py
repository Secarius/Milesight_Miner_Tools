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
        pixmap = QPixmap('updater/assets/update.jpeg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        
        self.show()
        time.sleep(5)
        update_start()

def update_start():
    updatepath = pathlib.Path().resolve()
    wait_until()
    with ZipFile('miner-update.zip', 'r') as zipOjk:
        zipOjk.extractall()
    updater = str(updatepath)
    Popen('%s\\MinerTools.exe' % updater)
    myfile="miner-update.zip"
    ## If file exists, delete it ##
    if os.path.isfile(myfile):
        os.remove(myfile)
    myfile="updater.zip"
    ## If file exists, delete it ##
    if os.path.isfile(myfile):
        os.remove(myfile)
    sys.exit()

def wait_until():
    while True:
        if ("MinerTools.exe" in (p.name() for p in psutil.process_iter())): 
            time.sleep(5)
        else:
            return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

