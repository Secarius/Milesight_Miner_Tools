import os
from numpy import genfromtxt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

dir_path = '%s\\MinerTools\\' % os.environ['APPDATA']
optionspath = '%s\\options.config' % dir_path
try:
    minerconfig = genfromtxt(optionspath, skip_header=1, delimiter=",", dtype='unicode', loose=True, invalid_raise=False,comments=None,deletechars='')
except IOError:
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Could not load miner config")
    msg.setWindowTitle("Error")
    msg.setWindowIcon(QtGui.QIcon('assets/helium.ico'))
    msg.exec_()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(857, 179)
        Dialog.setMinimumSize(QtCore.QSize(857, 179))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 179))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.verticalLayout.addWidget(self.label_settings)
        self.hzlayout_selectminer = QtWidgets.QHBoxLayout()
        self.hzlayout_selectminer.setObjectName("hzlayout_selectminer")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(40, 0))
        self.label.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.hzlayout_selectminer.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.hzlayout_selectminer.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.hzlayout_selectminer.addItem(spacerItem)
        self.verticalLayout.addLayout(self.hzlayout_selectminer)
        self.hzlayout_label = QtWidgets.QHBoxLayout()
        self.hzlayout_label.setObjectName("hzlayout_label")
        self.label_name = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.hzlayout_label.addWidget(self.label_name)
        self.label_ip = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ip.setFont(font)
        self.label_ip.setObjectName("label_ip")
        self.hzlayout_label.addWidget(self.label_ip)
        self.label_username = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.hzlayout_label.addWidget(self.label_username)
        self.label_password = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.hzlayout_label.addWidget(self.label_password)
        self.label_sshport = QtWidgets.QLabel(Dialog)
        self.label_sshport.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_sshport.setFont(font)
        self.label_sshport.setObjectName("label_sshport")
        self.hzlayout_label.addWidget(self.label_sshport)
        self.verticalLayout.addLayout(self.hzlayout_label)
        self.hzlayout_input = QtWidgets.QHBoxLayout()
        self.hzlayout_input.setObjectName("hzlayout_input")
        self.lineedit_name = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineedit_name.setFont(font)
        self.lineedit_name.setObjectName("lineedit_name")
        self.hzlayout_input.addWidget(self.lineedit_name)
        self.lineedit_ip = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineedit_ip.setFont(font)
        self.lineedit_ip.setObjectName("lineedit_ip")
        self.hzlayout_input.addWidget(self.lineedit_ip)
        self.lineedit_username = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineedit_username.setFont(font)
        self.lineedit_username.setObjectName("lineedit_username")
        self.hzlayout_input.addWidget(self.lineedit_username)
        self.lineedit_password = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineedit_password.setFont(font)
        self.lineedit_password.setObjectName("lineedit_password")
        self.hzlayout_input.addWidget(self.lineedit_password)
        self.lineedit_port = QtWidgets.QLineEdit(Dialog)
        self.lineedit_port.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineedit_port.setFont(font)
        self.lineedit_port.setObjectName("lineedit_port")
        self.hzlayout_input.addWidget(self.lineedit_port)
        self.verticalLayout.addLayout(self.hzlayout_input)
        self.hzlayout_savecancel = QtWidgets.QHBoxLayout()
        self.hzlayout_savecancel.setObjectName("hzlayout_savecancel")
        self.button_save_changes = QtWidgets.QPushButton(Dialog)
        self.button_save_changes.setMinimumSize(QtCore.QSize(150, 0))
        self.button_save_changes.setMaximumSize(QtCore.QSize(246, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_save_changes.setFont(font)
        self.button_save_changes.setObjectName("button_save_changes")
        self.hzlayout_savecancel.addWidget(self.button_save_changes)
        self.button_add_as_new = QtWidgets.QPushButton(Dialog)
        self.button_add_as_new.setMinimumSize(QtCore.QSize(150, 0))
        self.button_add_as_new.setMaximumSize(QtCore.QSize(246, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_add_as_new.setFont(font)
        self.button_add_as_new.setObjectName("button_add_as_new")
        self.hzlayout_savecancel.addWidget(self.button_add_as_new)
        self.button_delete_miner = QtWidgets.QPushButton(Dialog)
        self.button_delete_miner.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_delete_miner.setFont(font)
        self.button_delete_miner.setObjectName("button_delete_miner")
        self.hzlayout_savecancel.addWidget(self.button_delete_miner)
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hzlayout_savecancel.addItem(spacerItem1)
        self.button_close = QtWidgets.QPushButton(Dialog)
        self.button_close.setMinimumSize(QtCore.QSize(246, 0))
        self.button_close.setMaximumSize(QtCore.QSize(246, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_close.setFont(font)
        self.button_close.setObjectName("button_close")
        self.hzlayout_savecancel.addWidget(self.button_close)
        self.verticalLayout.addLayout(self.hzlayout_savecancel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Configure Miners"))
        self.label_settings.setText(_translate("Dialog", "Miner Tools Settings - Configure Miners"))
        self.label.setText(_translate("Dialog", "Select:"))
        self.label_name.setText(_translate("Dialog", "Miner Name:"))
        self.label_ip.setText(_translate("Dialog", "IP Adress or DNS:"))
        self.label_username.setText(_translate("Dialog", "Username:"))
        self.label_password.setText(_translate("Dialog", "Password:"))
        self.label_sshport.setText(_translate("Dialog", "SSH Port:"))
        self.button_save_changes.setText(_translate("Dialog", "Save Miner Changes"))
        self.button_add_as_new.setText(_translate("Dialog", "Add as new Miner"))
        self.button_delete_miner.setText(_translate("Dialog", "Delete selected Miner"))
        self.button_close.setText(_translate("Dialog", "Close"))

        self.updatecombo()
        self.button_close.clicked.connect(Dialog.reject)
        self.button_save_changes.clicked.connect(self.safe_changes)
        self.button_add_as_new.clicked.connect(self.add_new)
        self.comboBox.currentIndexChanged.connect(self.readcombo)
        self.button_delete_miner.clicked.connect(self.delete_selected)

    def updatecombo(self):
        global minerconfig
        try:
            f = open(optionspath)
        except IOError:
            f = open(optionspath,"w+")
            f.write("#MinerName,IP,User,Password,Port\n")
            f.close
        finally:
            f.close()
        try:
            minerconfig = genfromtxt(optionspath, skip_header=1, delimiter=",", dtype='unicode', loose=True, invalid_raise=False,comments=None,deletechars='')
        except IOError:
                reply = QtWidgets.QMessageBox.question(self, 'Message',
                "There is error with the configfile\nIts located in: %appdata%\MinerTools", QtWidgets.QMessageBox.Ok)
        self.comboBox.clear()
        if len(minerconfig.shape) > 1:
            for x in range(len(minerconfig)):
                self.comboBox.addItem(minerconfig[x][0])
        else:
            if len(minerconfig.shape) == 1 and not minerconfig.shape == (0,):
                self.comboBox.addItem(minerconfig[0])
            else:
                return
        combopos = self.comboBox.currentIndex()
        if len(minerconfig.shape) == 1 and not minerconfig.shape == (0,):
            minername = minerconfig[0]
            addr = minerconfig[1]
            user = minerconfig[2]
            passwd = minerconfig[3]
            port = minerconfig[4]
        else:
            minername = minerconfig[combopos][0]
            addr = minerconfig[combopos][1]
            user = minerconfig[combopos][2]
            passwd = minerconfig[combopos][3]
            port = minerconfig[combopos][4]
        self.lineedit_name.setText(minername)
        self.lineedit_ip.setText(addr)
        self.lineedit_username.setText(user)
        self.lineedit_password.setText(passwd)
        self.lineedit_port.setText(port)

    def readcombo(self):
        combopos = self.comboBox.currentIndex()
        if len(minerconfig.shape) == 1 and not minerconfig.shape == (0,):
            minername = minerconfig[0]
            addr = minerconfig[1]
            user = minerconfig[2]
            passwd = minerconfig[3]
            port = minerconfig[4]
        else:
            minername = minerconfig[combopos][0]
            addr = minerconfig[combopos][1]
            user = minerconfig[combopos][2]
            passwd = minerconfig[combopos][3]
            port = minerconfig[combopos][4]
        self.lineedit_name.setText(minername)
        self.lineedit_ip.setText(addr)
        self.lineedit_username.setText(user)
        self.lineedit_password.setText(passwd)
        self.lineedit_port.setText(port)

    def safe_changes(self):
        if self.lineedit_name.text() != "" and self.lineedit_ip.text() != "" and self.lineedit_username.text() != "" and self.lineedit_password.text() != "":
            if self.lineedit_port.text() == "":
                self.lineedit_port.setText("22")
            combopos = self.comboBox.currentIndex()
            with open(optionspath, 'r') as file:
                data = file.readlines()
                file.close()
            changelinepos = combopos+1
            data[changelinepos] = ("%s,%s,%s,%s,%s\n" % (self.lineedit_name.text(),self.lineedit_ip.text(),self.lineedit_username.text(),self.lineedit_password.text(),self.lineedit_port.text()))
            with open(optionspath,'w') as file:
                file.writelines(data)
                file.close()
            global minerconfig
            minerconfig = genfromtxt(optionspath, skip_header=1, delimiter=",", dtype='unicode', loose=True, invalid_raise=False,comments=None,deletechars='')
            self.updatecombo()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Miner change saved!")
            msg.setWindowTitle("Information")
            msg.setWindowIcon(QtGui.QIcon('assets/helium.ico'))
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("One or more input flieds are empty!")
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QtGui.QIcon('assets/helium.ico'))
            msg.exec_()

    
    def add_new(self):
        if self.lineedit_name.text() != "" and self.lineedit_ip.text() != "" and self.lineedit_username.text() != "" and self.lineedit_password.text() != "":
            if self.lineedit_port.text() == "":
                self.lineedit_port.setText("22")
            minersconfig = open(optionspath, 'a')
            minersconfig.write("%s,%s,%s,%s,%s\n" % (self.lineedit_name.text(),self.lineedit_ip.text(),self.lineedit_username.text(),self.lineedit_password.text(),self.lineedit_port.text()))
            minersconfig.close()
            self.updatecombo()
            global minerconfig
            minerconfig = genfromtxt(optionspath, skip_header=1, delimiter=",", dtype='unicode', loose=True, invalid_raise=False,comments=None,deletechars='')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("New Miner Added!")
            msg.setWindowTitle("Information")
            msg.setWindowIcon(QtGui.QIcon('assets/helium.ico'))
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("One or more input flieds are empty!")
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QtGui.QIcon('assets/helium.ico'))
            msg.exec_()

    def delete_selected(self):
        combopos = self.comboBox.currentIndex()
        changelinepos = combopos+1
        lines = []
        with open(optionspath, 'r') as file:
            lines = file.readlines()
            file.close()
        with open(optionspath, 'w') as file:
            for number, line in enumerate(lines):
                if number != changelinepos:
                    file.write(line)
            file.close()
        self.updatecombo()
        global minerconfig
        minerconfig = genfromtxt(optionspath, skip_header=1, delimiter=",", dtype='unicode', loose=True, invalid_raise=False,comments=None,deletechars='')
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Miner has been deleted!")
        msg.setWindowTitle("Information")
        msg.setWindowIcon(QtGui.QIcon('assets/helium.ico'))
        msg.exec_()
