import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import configparser
from gui.minertools_gui_main_window import Ui_MainWindow

settingsini = configparser.ConfigParser()
dir_path = '%s\\MinerTools\\' % os.environ['APPDATA'] 
settingsspath = '%s\\settings.ini' % dir_path

def write_file():
    settingsini.write(open(settingsspath, 'w'))

if not os.path.exists(settingsspath):
    settingsini['systemsettings'] = {'highdpi': '1', 'showlogo': '1', 'snapurl': 'http://snapshots-wtf.sensecapmx.cloud/snap-', 
    'snaplatesturl': 'http://snapshots-wtf.sensecapmx.cloud/latest-snap.json', 'constxtcolor': '#A4E87F', 'consbackcolor': '#212121',
    'pui_value': '600000', 'mic_value': '60', 'ogc_value': '20', 'ncm_value': '16', 'progbut1_name': 'Programmable1', 'progbut1_cmd': 'uptime', 
    'progbut2_name': 'Programmable2', 'progbut2_cmd': 'uptime', 'progbut3_name': 'Programmable3', 'progbut3_cmd': 'uptime'}
    write_file()
else:
    settingsini.read(settingsspath)
try:
    highdpi = settingsini.get('systemsettings', 'highdpi')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'highdpi', '1')
    highdpi = "1"
    write_file()
try:
    showlogo = settingsini.get('systemsettings', 'showlogo')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'showlogo', '1')
    write_file()
try:
    snapurl = settingsini.get('systemsettings', 'snapurl')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'snapurl', 'http://snapshots-wtf.sensecapmx.cloud/snap-')
    write_file()
try:
    snaplatesturl = settingsini.get('systemsettings', 'snaplatesturl')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'snaplatesturl', 'http://snapshots-wtf.sensecapmx.cloud/latest-snap.json')
    write_file()
try:
    constxtcolor = settingsini.get('systemsettings', 'constxtcolor')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'constxtcolor', '#A4E87F')
    write_file()
try:
    consbackcolor = settingsini.get('systemsettings', 'consbackcolor')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'consbackcolor', '#212121')
    write_file()
try:
    pui_value = settingsini.get('systemsettings', 'pui_value')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'pui_value', '600000')
    write_file()
try:
    mic_value = settingsini.get('systemsettings', 'mic_value')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'mic_value', '60')
    write_file()
try:
    ogc_value = settingsini.get('systemsettings', 'ogc_value')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'ogc_value', '20')
    write_file()
try:
    ncm_value = settingsini.get('systemsettings', 'ncm_value')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'ncm_value', '16')
    write_file()
try:
    progbut1_cmd = settingsini.get('systemsettings', 'progbut1_cmd')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'progbut1_cmd', 'uptime')
    write_file()
try:
    progbut1_name = settingsini.get('systemsettings', 'progbut1_name')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'progbut1_name', 'Programmable1')
    write_file()
try:
    progbut2_cmd = settingsini.get('systemsettings', 'progbut2_cmd')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'progbut2_cmd', 'uptime')
    write_file()
try:
    progbut2_name = settingsini.get('systemsettings', 'progbut2_name')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'progbut2_name', 'Programmable2')
    write_file()
try:
    progbut3_cmd = settingsini.get('systemsettings', 'progbut3_cmd')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'progbut3_cmd', 'uptime')
    write_file()
try:
    progbut3_name = settingsini.get('systemsettings', 'progbut3_name')
except configparser.NoOptionError:
    settingsini.set('systemsettings', 'progbut3_name', 'Programmable3')
    write_file()

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
os.environ["QT_SCALE_FACTOR"] = highdpi
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = highdpi

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
