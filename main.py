import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from gui.minertools_gui_main_window import Ui_MainWindow
#*************************** BUTTON FUNCTIONS ***************************
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
os.environ["QT_SCALE_FACTOR"] = "0"
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"

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
