import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QColorDialog
import configparser
from gui.minertools_gui_editminer_dialog import Ui_Dialog as Settingsdiag

def write_file():
    settingsini.write(open(settingsspath, 'w'))

settingsini = configparser.ConfigParser()
dir_path = '%s\\MinerTools\\' % os.environ['APPDATA'] 
settingsspath = '%ssettings.ini' % dir_path
global highdpi
global showlogo
global snapurl 
global snaplatesturl 
global constxtcolor 
global consbackcolor 

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(465, 310)
        Dialog.setMinimumSize(QtCore.QSize(465, 310))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 310))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_settings = QtWidgets.QLabel(Dialog)
        self.label_settings.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_settings.setFont(font)
        self.label_settings.setStyleSheet("")
        self.label_settings.setAlignment(QtCore.Qt.AlignCenter)
        self.label_settings.setObjectName("label_settings")
        self.horizontalLayout.addWidget(self.label_settings)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.hzlayout_highdpi = QtWidgets.QHBoxLayout()
        self.hzlayout_highdpi.setObjectName("hzlayout_highdpi")
        self.label_highdpi = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_highdpi.setFont(font)
        self.label_highdpi.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_highdpi.setObjectName("label_highdpi")
        self.hzlayout_highdpi.addWidget(self.label_highdpi)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hzlayout_highdpi.addItem(spacerItem)
        self.checkbox_highdpi = QtWidgets.QCheckBox(Dialog)
        self.checkbox_highdpi.setMinimumSize(QtCore.QSize(13, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkbox_highdpi.setFont(font)
        self.checkbox_highdpi.setText("")
        self.checkbox_highdpi.setObjectName("checkbox_highdpi")
        self.hzlayout_highdpi.addWidget(self.checkbox_highdpi)
        self.verticalLayout.addLayout(self.hzlayout_highdpi)
        self.hzlayout_logo = QtWidgets.QHBoxLayout()
        self.hzlayout_logo.setObjectName("hzlayout_logo")
        self.label_logo = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_logo.setFont(font)
        self.label_logo.setObjectName("label_logo")
        self.hzlayout_logo.addWidget(self.label_logo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hzlayout_logo.addItem(spacerItem1)
        self.checkbox_logo = QtWidgets.QCheckBox(Dialog)
        self.checkbox_logo.setText("")
        self.checkbox_logo.setObjectName("checkbox_logo")
        self.hzlayout_logo.addWidget(self.checkbox_logo)
        self.verticalLayout.addLayout(self.hzlayout_logo)
        self.hzlayout_snapurl = QtWidgets.QHBoxLayout()
        self.hzlayout_snapurl.setObjectName("hzlayout_snapurl")
        self.label_snapurl = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_snapurl.setFont(font)
        self.label_snapurl.setObjectName("label_snapurl")
        self.hzlayout_snapurl.addWidget(self.label_snapurl)
        self.lineedit_snapurl = QtWidgets.QLineEdit(Dialog)
        self.lineedit_snapurl.setObjectName("lineedit_snapurl")
        self.hzlayout_snapurl.addWidget(self.lineedit_snapurl)
        self.verticalLayout.addLayout(self.hzlayout_snapurl)
        self.hzlayout_snaplatest = QtWidgets.QHBoxLayout()
        self.hzlayout_snaplatest.setObjectName("hzlayout_snaplatest")
        self.label_snaplatesturl = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_snaplatesturl.setFont(font)
        self.label_snaplatesturl.setObjectName("label_snaplatesturl")
        self.hzlayout_snaplatest.addWidget(self.label_snaplatesturl)
        self.lineedit_snaplatesturl = QtWidgets.QLineEdit(Dialog)
        self.lineedit_snaplatesturl.setObjectName("lineedit_snaplatesturl")
        self.hzlayout_snaplatest.addWidget(self.lineedit_snaplatesturl)
        self.verticalLayout.addLayout(self.hzlayout_snaplatest)
        self.hzlayout_textcolor = QtWidgets.QHBoxLayout()
        self.hzlayout_textcolor.setObjectName("hzlayout_textcolor")
        self.label_constxtcolor = QtWidgets.QLabel(Dialog)
        self.label_constxtcolor.setMaximumSize(QtCore.QSize(121, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_constxtcolor.setFont(font)
        self.label_constxtcolor.setObjectName("label_constxtcolor")
        self.hzlayout_textcolor.addWidget(self.label_constxtcolor)
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hzlayout_textcolor.addItem(spacerItem2)
        self.lineedit_txtcolor = QtWidgets.QLineEdit(Dialog)
        self.lineedit_txtcolor.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineedit_txtcolor.setObjectName("lineedit_txtcolor")
        self.hzlayout_textcolor.addWidget(self.lineedit_txtcolor)
        self.button_colorpickertxt = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_colorpickertxt.setFont(font)
        self.button_colorpickertxt.setObjectName("button_colorpickertxt")
        self.hzlayout_textcolor.addWidget(self.button_colorpickertxt)
        self.verticalLayout.addLayout(self.hzlayout_textcolor)
        self.hzlayout_consolecolor = QtWidgets.QHBoxLayout()
        self.hzlayout_consolecolor.setObjectName("hzlayout_consolecolor")
        self.label_consbackcolor = QtWidgets.QLabel(Dialog)
        self.label_consbackcolor.setMaximumSize(QtCore.QSize(154, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_consbackcolor.setFont(font)
        self.label_consbackcolor.setObjectName("label_consbackcolor")
        self.hzlayout_consolecolor.addWidget(self.label_consbackcolor)
        spacerItem3 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hzlayout_consolecolor.addItem(spacerItem3)
        self.lineedit_backcolor = QtWidgets.QLineEdit(Dialog)
        self.lineedit_backcolor.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineedit_backcolor.setObjectName("lineedit_backcolor")
        self.hzlayout_consolecolor.addWidget(self.lineedit_backcolor)
        self.button_colorpickerback = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_colorpickerback.setFont(font)
        self.button_colorpickerback.setObjectName("button_colorpickerback")
        self.hzlayout_consolecolor.addWidget(self.button_colorpickerback)
        self.verticalLayout.addLayout(self.hzlayout_consolecolor)
        self.hzlayout_editminer = QtWidgets.QHBoxLayout()
        self.hzlayout_editminer.setObjectName("hzlayout_editminer")
        self.button_editminer = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_editminer.setFont(font)
        self.button_editminer.setObjectName("button_editminer")
        self.hzlayout_editminer.addWidget(self.button_editminer)
        self.verticalLayout.addLayout(self.hzlayout_editminer)
        self.hzlayout_savecancel = QtWidgets.QHBoxLayout()
        self.hzlayout_savecancel.setObjectName("hzlayout_savecancel")
        self.button_save = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_save.setFont(font)
        self.button_save.setObjectName("button_save")
        self.hzlayout_savecancel.addWidget(self.button_save)
        spacerItem4 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hzlayout_savecancel.addItem(spacerItem4)
        self.button_cancel = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_cancel.setFont(font)
        self.button_cancel.setObjectName("button_cancel")
        self.hzlayout_savecancel.addWidget(self.button_cancel)
        self.verticalLayout.addLayout(self.hzlayout_savecancel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.label_settings.setText(_translate("Dialog", "Miner Tools Settings"))
        self.label_highdpi.setText(_translate("Dialog", "Start with High DPI Scaling:"))
        self.label_logo.setText(_translate("Dialog", "Show logo?:"))
        self.label_snapurl.setText(_translate("Dialog", "Snap Url:"))
        self.label_snaplatesturl.setText(_translate("Dialog", "Sap Url Latest:"))
        self.label_constxtcolor.setText(_translate("Dialog", "Console Text Color:"))
        self.button_colorpickertxt.setText(_translate("Dialog", "Color Picker"))
        self.label_consbackcolor.setText(_translate("Dialog", "Console Background Color:"))
        self.button_colorpickerback.setText(_translate("Dialog", "Color Picker"))
        self.button_editminer.setText(_translate("Dialog", "Edit Miner List"))
        self.button_save.setText(_translate("Dialog", "Save Changes"))
        self.button_cancel.setText(_translate("Dialog", "Cancel"))


# Define Button Actions
        self.button_colorpickertxt.clicked.connect(self.opentxtcolorColorDialog)
        self.button_colorpickerback.clicked.connect(self.openbackcolorColorDialog)
        self.button_cancel.clicked.connect(Dialog.reject)
        self.button_save.clicked.connect(self.saveconfig)
        self.readconfig()
        self.button_editminer.clicked.connect(self.open_editminer)
        self.lineedit_backcolor.setReadOnly(True)
        self.lineedit_txtcolor.setReadOnly(True)

# Define Functions
    def readconfig(self):
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
            settingsini.set('systemsettings', 'showlogo', '0')
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

        if highdpi == "1":
            self.checkbox_highdpi.setChecked(True)
        else:
            self.checkbox_highdpi.setChecked(False)
        if showlogo == "1":
            self.checkbox_logo.setChecked(True)
        else:
            self.checkbox_logo.setChecked(False)
        self.lineedit_snapurl.setText(snapurl)
        self.lineedit_snaplatesturl.setText(snaplatesturl)
        self.lineedit_txtcolor.setText(constxtcolor)
        self.lineedit_txtcolor.setStyleSheet("background-color:%s;" % constxtcolor)
        self.lineedit_backcolor.setText(consbackcolor)
        self.lineedit_backcolor.setStyleSheet("background-color:%s;" % consbackcolor)

    def saveconfig(self):
        settingsini.read(settingsspath)
        if self.checkbox_highdpi.checkState() == 2:
            highdpistatus = 1
        else:
            highdpistatus = 0
        if self.checkbox_logo.checkState() == 2:
            showlogostatus = 1
        else:
            showlogostatus = 0
        settingsini.set('systemsettings', 'highdpi', '%s' % highdpistatus)
        settingsini.set('systemsettings', 'snapurl', '%s' % self.lineedit_snapurl.text())
        settingsini.set('systemsettings', 'snaplatesturl', '%s' % self.lineedit_snaplatesturl.text())
        settingsini.set('systemsettings', 'constxtcolor', '%s' % self.lineedit_txtcolor.text())
        settingsini.set('systemsettings', 'consbackcolor', '%s' % self.lineedit_backcolor.text())
        settingsini.set('systemsettings','showlogo', '%s' % showlogostatus)
        write_file()
        self.button_cancel.click()

    def openbackcolorColorDialog(self):
        color = QColorDialog.getColor()
        self.lineedit_backcolor.setText(color.name())
        self.lineedit_backcolor.setStyleSheet("background-color:%s;" % (color.name()))

    def opentxtcolorColorDialog(self):
        color = QColorDialog.getColor()
        self.lineedit_txtcolor.setText(color.name())
        self.lineedit_txtcolor.setStyleSheet("background-color:%s;" % (color.name()))

    def open_editminer(self):
        editminerset = QtWidgets.QDialog()
        editminerset.ui = Settingsdiag()
        editminerset.ui.setupUi(editminerset)
        editminerset.setWindowFlags(QtCore.Qt.WindowType.CustomizeWindowHint)
        editminerset.setWindowFlags(editminerset.windowFlags() & ~QtCore.Qt.WindowType.WindowMinimizeButtonHint & QtCore.Qt.WindowType.WindowCloseButtonHint)
        editminerset.setWindowIcon(QtGui.QIcon('assets/helium.ico'))
        editminerset.exec_()
        editminerset.show()
        self.readconfig()