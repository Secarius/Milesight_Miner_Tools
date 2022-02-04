# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minertools_gui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#####################################################################
import psutil
from zipfile import ZipFile
import sys
import subprocess
from asyncio import subprocess
from subprocess import Popen
from fnmatch import fnmatch
from pprint import pprint
import requests
import json
import urllib.request
from urllib import request
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
import os
from email.mime import image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
import threading
import ipaddress
import socket
import os, sys
from numpy import empty, equal, genfromtxt
from packaging import version
import pathlib
#####################################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from assets import images_rc
from src import ssh_comms
from paramiko import SSHClient, AutoAddPolicy
import psutil
import time

version_build = "1.1.0"
dir_path = '%s\\MinerTools\\' % os.environ['APPDATA'] 
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
optionspath = '%s\\options.config' % dir_path
try:
    f = open(optionspath)
except IOError:
    print("File not accessible")
    f = open(optionspath,"w+")
    f.write("#MinerName,IP,User,Password,Port")
    f.close
finally:
    f.close()
minerconfig = genfromtxt(optionspath, comments="#", delimiter=",", dtype='unicode')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1202, 792)
        MainWindow.resize(1202, 792)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_status = QtWidgets.QPushButton(self.centralwidget)
        self.button_status.setGeometry(QtCore.QRect(5, 662, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_status.setFont(font)
        self.button_status.setObjectName("button_status")
        self.button_info = QtWidgets.QPushButton(self.centralwidget)
        self.button_info.setGeometry(QtCore.QRect(125, 662, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_info.setFont(font)
        self.button_info.setObjectName("button_info")
        self.button_compare_height = QtWidgets.QPushButton(self.centralwidget)
        self.button_compare_height.setGeometry(QtCore.QRect(245, 662, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_compare_height.setFont(font)
        self.button_compare_height.setObjectName("button_compare_height")
        self.button_peer_book = QtWidgets.QPushButton(self.centralwidget)
        self.button_peer_book.setGeometry(QtCore.QRect(365, 662, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_peer_book.setFont(font)
        self.button_peer_book.setObjectName("button_peer_book")
        self.button_restart_miner = QtWidgets.QPushButton(self.centralwidget)
        self.button_restart_miner.setGeometry(QtCore.QRect(485, 662, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_restart_miner.setFont(font)
        self.button_restart_miner.setObjectName("button_restart_miner")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(725, 662, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_7.setFont(font)
        self.button_7.setObjectName("button_7")
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(605, 662, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_6.setFont(font)
        self.button_6.setObjectName("button_6")
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(845, 662, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_8.setFont(font)
        self.button_8.setObjectName("button_8")
        self.button_fast_sync = QtWidgets.QPushButton(self.centralwidget)
        self.button_fast_sync.setGeometry(QtCore.QRect(965, 661, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_fast_sync.setFont(font)
        self.button_fast_sync.setObjectName("button_fast_sync")
        self.button_quagga_restart = QtWidgets.QPushButton(self.centralwidget)
        self.button_quagga_restart.setGeometry(QtCore.QRect(1085, 661, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_quagga_restart.setFont(font)
        self.button_quagga_restart.setObjectName("button_quagga_restart")
        self.button_send_command = QtWidgets.QPushButton(self.centralwidget)
        self.button_send_command.setGeometry(QtCore.QRect(1085, 710, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_send_command.setFont(font)
        self.button_send_command.setObjectName("button_send_command")
        self.line_command = QtWidgets.QLineEdit(self.centralwidget)
        self.line_command.setGeometry(QtCore.QRect(6, 710, 1070, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.line_command.setFont(font)
        self.line_command.setObjectName("line_command")
        self.combo_select_miner = QtWidgets.QComboBox(self.centralwidget)
        self.combo_select_miner.setGeometry(QtCore.QRect(104, 3, 210, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_select_miner.setFont(font)
        self.combo_select_miner.setObjectName("combo_select_miner")
        self.label_select_miner = QtWidgets.QLabel(self.centralwidget)
        self.label_select_miner.setGeometry(QtCore.QRect(4, 1, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_select_miner.setFont(font)
        self.label_select_miner.setObjectName("label_select_miner")
        self.logo_milesight = QtWidgets.QPushButton(self.centralwidget)
        self.logo_milesight.setGeometry(QtCore.QRect(1100, 0, 101, 31))
        self.logo_milesight.setAutoFillBackground(False)
        self.logo_milesight.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logo/milesight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logo_milesight.setIcon(icon)
        self.logo_milesight.setIconSize(QtCore.QSize(100, 200))
        self.logo_milesight.setCheckable(False)
        self.logo_milesight.setFlat(True)
        self.logo_milesight.setObjectName("logo_milesight")
        self.label_version = QtWidgets.QLabel(self.centralwidget)
        self.label_version.setGeometry(QtCore.QRect(1006, 8, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_version.setFont(font)
        self.label_version.setObjectName("label_version")
        self.label_version_numer = QtWidgets.QLabel(self.centralwidget)
        self.label_version_numer.setGeometry(QtCore.QRect(1060, 8, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_version_numer.setFont(font)
        self.label_version_numer.setObjectName("label_version_numer")
        self.button_config_edit = QtWidgets.QPushButton(self.centralwidget)
        self.button_config_edit.setGeometry(QtCore.QRect(320, 2, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_config_edit.setFont(font)
        self.button_config_edit.setObjectName("button_config_edit")
        self.button_config_reload = QtWidgets.QPushButton(self.centralwidget)
        self.button_config_reload.setGeometry(QtCore.QRect(435, 2, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_config_reload.setFont(font)
        self.button_config_reload.setObjectName("button_config_reload")
        self.button_check_update = QtWidgets.QPushButton(self.centralwidget)
        self.button_check_update.setGeometry(QtCore.QRect(885, 2, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_check_update.setFont(font)
        self.button_check_update.setObjectName("button_check_update")
        self.text_console = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_console.setGeometry(QtCore.QRect(6, 34, 1190, 621))
        self.text_console = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_console.setGeometry(QtCore.QRect(6, 34, 1190, 621))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.text_console.setFont(font)
        self.text_console.setObjectName("text_console")
        self.text_console.setStyleSheet("background-color:#212121;color:#A4E87F;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1202, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Import_Config = QtWidgets.QAction(MainWindow)
        self.action_Import_Config.setObjectName("action_Edit_Config")
        self.action_Edit_Config = QtWidgets.QAction(MainWindow)
        self.action_Edit_Config.setObjectName("action_Edit_Config")
        self.action_Export_Config = QtWidgets.QAction(MainWindow)
        self.action_Export_Config.setObjectName("action_Export_Config")
        self.menuFile.addAction(self.action_Edit_Config)
        self.menuFile.addAction(self.action_Import_Config)
        self.menuFile.addAction(self.action_Export_Config)
        self.menuFile.addAction(self.action_Exit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
##################################################################
# Button Actions
        self.action_Edit_Config.triggered.connect(self.edit_config)
        self.action_Export_Config.triggered.connect(self.export_config)
        self.action_Import_Config.triggered.connect(self.import_config)
        self.action_Exit.triggered.connect(self.exit_window)

        self.savepath = 'log.txt'
        self.s = ssh_comms.ssh_comms()

        self.button_config_reload.clicked.connect(self.updatecombo)
        self.button_config_edit.clicked.connect(self.edit_config)

#        self.button_send_command.clicked.connect(self.run_funk)
        self.button_send_command.clicked.connect(self.run_command_func)
        self.button_status.clicked.connect(self.status_but_func)
        self.button_info.clicked.connect(self.miner_info_func)
        self.button_peer_book.clicked.connect(self.run_peer_book_func)
        self.button_compare_height.clicked.connect(self.run_height_compare_func)
        self.button_6.clicked.connect(self.status_but_func)
        self.button_7.clicked.connect(self.status_but_func)
        self.button_8.clicked.connect(self.status_but_func)
        self.button_fast_sync.clicked.connect(self.update_but_func)
        self.button_quagga_restart.clicked.connect(self.quagga_but_func)
        self.button_check_update.clicked.connect(self.get_url_paths)

    def check_update_func(self):
        print()

    def get_url_paths(self):
        r = requests.get("https://api.github.com/repos/Secarius/Milesight_Miner_Tools/git/trees/main?recursive=1")
        data = r.json()
        url = [item['path'] for item in data['tree']]
        updatepackage = [string for string in url if 'minertools' in string]
        zippackage = [string for string in updatepackage if '.zip' in string]
        zippackage = zippackage[0]
        online_version = zippackage.replace(".zip", "")
        online_version = online_version.replace("installer/minertools_", "")
        if (version.parse(version_build) < version.parse(online_version)):
            updateurl = "https://github.com/Secarius/Milesight_Miner_Tools/raw/main/%s" % zippackage
            reply = QtWidgets.QMessageBox.question(self, 'Message',
                "Do you want to update?", QtWidgets.QMessageBox.Yes | 
                QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                urllib.request.urlretrieve(updateurl,"miner-update.zip")
                urllib.request.urlretrieve("https://github.com/Secarius/Milesight_Miner_Tools/raw/main/installer/updater.zip","updater.zip")
                with ZipFile('updater.zip', 'r') as zipOjk:
                    zipOjk.extractall()
                updatepath = pathlib.Path().resolve()
                updater = str(updatepath)
                print(updater + "\\updater\miner-update.exe")
                Popen("%s\\updater\miner-update.exe" % updater)
                sys.exit()
        else:
            pprint("no update available")

    def updatecombo(self):
        try:
            f = open(optionspath)
        except IOError:
            print("File not accessible")
            f = open(optionspath,"w+")
            f.write("#MinerName,IP,User,Password,Port")
            f.close
        finally:
            f.close()
        minerconfig = genfromtxt(optionspath, comments="#", delimiter=",", dtype='unicode')
        self.combo_select_miner.clear()
        if len(minerconfig.shape) > 1:
            for x in range(len(minerconfig)):
                self.combo_select_miner.addItem(minerconfig[x][0])
        else:
            if len(minerconfig.shape) == 1 and not minerconfig.shape == (0,):
                self.combo_select_miner.addItem(minerconfig[0])
            else:
                self.throw_custom_error(title='Error', message='Config is empty!')

    def run_funk(self):
        print(self.line_command.text())
        
    def edit_config(self):
        os.system('notepad.exe ' + optionspath)
        self.updatecombo()

    def export_config(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        if not name[0] == '':
            with open(optionspath) as f:
                with open(name[0], "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
        self.updatecombo()

    def import_config(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if not name[0] == '':
            with open(name[0]) as f:
                with open(optionspath, "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
        self.updatecombo()

    def exit_window(self):
        qApp.quit()

# SSH Commands
    def run_sync_commands(self):
        self.update_fbdata('Syncing . . . This might take a minute . . .\n')
        self.log = ''
        height = '** ERROR WHILE EXECUTING CURL CMD **'
        cmds = ['docker exec miner miner repair sync_pause',
                'docker exec miner miner repair sync_cancel',
                'curl https://helium-snapshots.nebra.com/latest.json',
                'cd /mnt/mmcblk0p1/miner_data/snap && rm snap-*',
                'cd /mnt/mmcblk0p1/miner_data/snap && wget https://helium-snapshots.nebra.com/snap-',
                'docker exec miner miner snapshot load /var/data/snap/snap- &',
                'docker exec miner miner repair sync_state',
                'docker exec miner miner repair sync_resume']
        do_sync_resume = False
        for idx, cmd in enumerate(cmds):
            if idx == 7 and do_sync_resume: # sync resume
                chk = True
                while chk:
                    self.update_fbdata(f'${cmd}\n')
                    out, stderr = self.s.exec_cmd(cmd=cmd)
                    self.update_fbdata(out)
                    if stderr != '': self.update_fbdata(f'STDERR: {stderr}')
                    self.log += f'#{cmd}\n{out}'
                    if stderr != '': self.log += f'STDERR: {stderr}'
                    chk = 'failed' in out
            else:
                if idx == 4: # wget
                    cmd += height
                elif idx == 5: # snapshot load
                    cmd = f"{cmd.split(' &')[0]}{height}{cmd.split('snap-')[1]}"
                self.update_fbdata(f'${cmd}\n')
                out, stderr = self.s.exec_cmd(cmd=cmd)
                self.update_fbdata(out)
                if stderr != '':
                    if idx == 4: stderr = '\n'.join(stderr.split('\n')[:13])+'\n'+' '*30+'..........\n'+'\n'.join(stderr.split('\n')[-10:])
                    self.update_fbdata(f'STDERR: {stderr}')
                if idx == 2: # curl
                    height = out.split('height": ')[1].split(',')[0]
                elif idx == 6: # sync_state
                    do_sync_resume = 'sync active' not in out

                self.log += f'#{cmd}\n{out}'
                if stderr != '': self.log += f'STDERR: {stderr}'
        self.update_fbdata('*** DONE ***\n')
        self.save()
        self.s.disconnect()

    #*************************** BUTTON FUNCTIONS ***************************
    def update_but_func(self):
        if not self.s.is_alive():
            if self.conn_sequence() == None:
                return
            self.tmpthread = threading.Thread(target=self.run_sync_commands)
            self.tmpthread.daemon = True
            self.tmpthread.start()
        else:
            self.throw_custom_error(title='Error', message='Another function already in progress. Please be patient.')

    def quagga_but_func(self):
        if not self.s.is_alive():
            if self.conn_sequence() == None:
                return
            self.tmpthread = threading.Thread(target=self.run_quagga_cmd)
            self.tmpthread.daemon = True
            self.tmpthread.start()
        else:
            self.throw_custom_error(title='Error', message='Another function already in progress. Please be patient.')
    
    def status_but_func(self):
        if not self.s.is_alive():
            if self.conn_sequence() == None:
                return
            self.tmpthread = threading.Thread(target=self.run_status_cmd)
            self.tmpthread.daemon = True
            self.tmpthread.start()
        else:
            self.throw_custom_error(title='Error', message='Another function already in progress. Please be patient.')

    def miner_info_func(self):
        if not self.s.is_alive():
            if self.conn_sequence() == None:
                return
            self.tmpthread = threading.Thread(target=self.run_miner_info_cmd)
            self.tmpthread.daemon = True
            self.tmpthread.start()
        else:
            self.throw_custom_error(title='Error', message='Another function already in progress. Please be patient.')

    def run_peer_book_func(self):
        if not self.s.is_alive():
            if self.conn_sequence() == None:
                return
            self.tmpthread = threading.Thread(target=self.run_peer_book_cmd)
            self.tmpthread.daemon = True
            self.tmpthread.start()
        else:
            self.throw_custom_error(title='Error', message='Another function already in progress. Please be patient.')

    def run_command_func(self):
        if not self.s.is_alive():
            if self.conn_sequence() == None:
                return
            self.tmpthread = threading.Thread(target=self.run_line_command_cmd)
            self.tmpthread.daemon = True
            self.tmpthread.start()
        else:
            self.throw_custom_error(title='Error', message='Another function already in progress. Please be patient.')

    def run_height_compare_func(self):
        if not self.s.is_alive():
            if self.conn_sequence() == None:
                return
            self.tmpthread = threading.Thread(target=self.run_height_compare)
            self.tmpthread.daemon = True
            self.tmpthread.start()
        else:
            self.throw_custom_error(title='Error', message='Another function already in progress. Please be patient.')
    #*************************** BUTTON FUNCTIONS ***************************

    def run_quagga_cmd(self):
        cmd = '/etc/init.d/quagga restart'
        self.update_fbdata(f'${cmd}\n')
        out, stderr = self.s.exec_cmd(cmd=cmd)
        self.update_fbdata(out)
        if stderr != '': self.update_fbdata(f'STDERR: {stderr}')
        self.update_fbdata(f'*** DONE ***\n')
        self.s.disconnect()


    def run_status_cmd(self):
        cmd = 'docker exec miner miner info p2p_status'
        self.update_fbdata(f'${cmd}\n')
        out, stderr = self.s.exec_cmd(cmd=cmd)
        self.update_fbdata(out)
        if stderr != '': self.update_fbdata(f'STDERR: {stderr}')
        self.update_fbdata(f'*** DONE ***\n')
        self.s.disconnect()

    def run_miner_info_cmd(self):
        cmd = 'docker exec miner miner info summary'
        self.update_fbdata(f'${cmd}\n')
        out, stderr = self.s.exec_cmd(cmd=cmd)
        self.update_fbdata(out)
        if stderr != '': self.update_fbdata(f'STDERR: {stderr}')
        self.update_fbdata(f'*** DONE ***\n')
        self.s.disconnect()

    def run_peer_book_cmd(self):
        cmd = 'docker exec miner miner peer book -s'
        self.update_fbdata(f'${cmd}\n')
        out, stderr = self.s.exec_cmd(cmd=cmd)
        self.update_fbdata(out)
        if stderr != '': self.update_fbdata(f'STDERR: {stderr}')
        self.update_fbdata(f'*** DONE ***\n')
        self.s.disconnect()

    def run_line_command_cmd(self):
        cmd = self.line_command.text()
        self.update_fbdata(f'${cmd}\n')
        out, stderr = self.s.exec_cmd(cmd=cmd)
        self.update_fbdata(out)
        if stderr != '': self.update_fbdata(f'STDERR: {stderr}')
        self.update_fbdata(f'*** DONE ***\n')
        self.s.disconnect()

    def run_height_compare(self):
        cmd = 'echo "Current Miner height: " && docker exec miner miner info height | sed \'s/^.\{7\}//\' && echo "Cur. Blockchain height:" && curl -k https://api.helium.io/v1/blocks/height 2> /dev/null | sed \'s/^.\{18\}//\' | sed \'s/.\{2\}$//\' && echo'
        #self.update_fbdata(f'${cmd}\n')
        out, stderr = self.s.exec_cmd(cmd=cmd)
        self.update_fbdata(out)
        if stderr != '': self.update_fbdata(f'STDERR: {stderr}')
        self.update_fbdata(f'*** DONE ***\n')
        self.s.disconnect()
# Connect Sequence
    def conn_sequence(self):
        combopos = self.combo_select_miner.currentIndex()
        if len(minerconfig.shape) == 1 and not minerconfig.shape == (0,):
            addr = minerconfig[1]
            user = minerconfig[2]
            passwd = minerconfig[3]
            port = minerconfig[4]
        else:
            addr = minerconfig[combopos][1]
            user = minerconfig[combopos][2]
            passwd = minerconfig[combopos][3]
            port = minerconfig[combopos][4]
        if addr[-1] == 'X':
            self.throw_custom_error(title='Error', message='Enter device IP address.')
            return None
        if not self.validate_ip_address(addr):
            self.throw_custom_error(title='Error', message='Invalid IP address.')
            return None
        if any([x==None for x in [user, passwd]]):
            self.throw_custom_error(title='Error', message='Error reading options.config file.')
            return None
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        if sock.connect_ex((addr, int(port))) != 0:
            sock.close()
            self.throw_trouble_connecting_error()
            return None
        sock.close()
        self.s.set_config(addr=addr, user=user, port=port, password=passwd)
        connection = self.s.connect()
        self.clear_fbdata()
        if not self.s.is_alive() or connection == None:
            self.update_fbdata('Connection Error.\nCheck username and password in options.config in files/ folder.')
            return None
        return True

    def update_fbdata(self, d):
        self.text_console.insertPlainText(d)
    
    def clear_fbdata(self):
        self.text_console.clear()

    def validate_ip_address(self, address):
        try:
            ip = ipaddress.ip_address(address)
            return True
        except ValueError:
            return False

    def save(self):
        try:
            with open(self.savepath, 'w') as f:
                f.write(self.log)
        except Exception as e:
            self.throw_custom_error('ERROR', 'Error trying to save log file.')
            print(f'e : {e}')
#*************************** BUTTON FUNCTIONS ***************************

#**************************** THROW ERROR ****************************
    def throw_trouble_connecting_error(self):
        messagebox.showwarning(title='ERROR', message='Having trouble connecting to device.')

    def throw_custom_error(self, title, message):
        messagebox.showwarning(title=title, message=message)
#**************************** THROW ERROR ****************************

##################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_status.setText(_translate("MainWindow", "Status"))
        self.button_info.setText(_translate("MainWindow", "Info"))
        self.button_compare_height.setText(_translate("MainWindow", "Compare Height"))
        self.button_peer_book.setText(_translate("MainWindow", "Peer Book"))
        self.button_restart_miner.setText(_translate("MainWindow", "Restart Miner"))
        self.button_7.setText(_translate("MainWindow", "PushButton"))
        self.button_6.setText(_translate("MainWindow", "PushButton"))
        self.button_8.setText(_translate("MainWindow", "PushButton"))
        self.button_fast_sync.setText(_translate("MainWindow", "Fast Sync"))
        self.button_quagga_restart.setText(_translate("MainWindow", "Quagga Restart"))
        self.button_send_command.setText(_translate("MainWindow", "Send Command"))
        self.line_command.setText(_translate("MainWindow", "docker exec miner miner info height && curl -k https://api.helium.io/v1/blocks/height"))
        self.label_select_miner.setText(_translate("MainWindow", "Select Miner:"))
        self.label_version.setText(_translate("MainWindow", "Version:"))
        self.label_version_numer.setText(_translate("MainWindow", version_build))
        self.button_config_edit.setText(_translate("MainWindow", "Edit Config"))
        self.button_config_reload.setText(_translate("MainWindow", "Reload Config"))
        self.button_check_update.setText(_translate("MainWindow", "Check Update"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_Exit.setText(_translate("MainWindow", "Exit"))
        self.action_Edit_Config.setText(_translate("MainWindow", "Edit Config"))
        self.action_Export_Config.setText(_translate("MainWindow", "Export Config"))
        self.action_Import_Config.setText(_translate("MainWindow", "Import Config"))
