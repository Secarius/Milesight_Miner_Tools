# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minertools_gui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1136, 737)
        MainWindow.setMinimumSize(QtCore.QSize(1136, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(5, 1, 5, 5)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_menu_layout = QtWidgets.QHBoxLayout()
        self.top_menu_layout.setSpacing(1)
        self.top_menu_layout.setObjectName("top_menu_layout")
        self.label_select_miner = QtWidgets.QLabel(self.centralwidget)
        self.label_select_miner.setMinimumSize(QtCore.QSize(100, 0))
        self.label_select_miner.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPixelSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_select_miner.setFont(font)
        self.label_select_miner.setWhatsThis("")
        self.label_select_miner.setObjectName("label_select_miner")
        self.top_menu_layout.addWidget(self.label_select_miner)
        self.combo_select_miner = QtWidgets.QComboBox(self.centralwidget)
        self.combo_select_miner.setMinimumSize(QtCore.QSize(190, 0))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.combo_select_miner.setFont(font)
        self.combo_select_miner.setWhatsThis("")
        self.combo_select_miner.setObjectName("combo_select_miner")
        self.top_menu_layout.addWidget(self.combo_select_miner)
        self.button_open_in_browser = QtWidgets.QPushButton(self.centralwidget)
        self.button_open_in_browser.setMinimumSize(QtCore.QSize(115, 26))
        self.button_open_in_browser.setMaximumSize(QtCore.QSize(115, 26))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_open_in_browser.setFont(font)
        self.button_open_in_browser.setWhatsThis("")
        self.button_open_in_browser.setObjectName("button_open_in_browser")
        self.top_menu_layout.addWidget(self.button_open_in_browser)
        self.button_helium_explorer = QtWidgets.QPushButton(self.centralwidget)
        self.button_helium_explorer.setMinimumSize(QtCore.QSize(117, 26))
        self.button_helium_explorer.setMaximumSize(QtCore.QSize(117, 26))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_helium_explorer.setFont(font)
        self.button_helium_explorer.setWhatsThis("")
        self.button_helium_explorer.setObjectName("button_helium_explorer")
        self.top_menu_layout.addWidget(self.button_helium_explorer)
        self.button_settings = QtWidgets.QPushButton(self.centralwidget)
        self.button_settings.setMinimumSize(QtCore.QSize(110, 26))
        self.button_settings.setMaximumSize(QtCore.QSize(110, 26))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_settings.setFont(font)
        self.button_settings.setWhatsThis("")
        self.button_settings.setObjectName("button_settings")
        self.top_menu_layout.addWidget(self.button_settings)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.top_menu_layout.addItem(spacerItem)
        self.button_check_update = QtWidgets.QPushButton(self.centralwidget)
        self.button_check_update.setMinimumSize(QtCore.QSize(102, 26))
        self.button_check_update.setMaximumSize(QtCore.QSize(102, 26))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_check_update.setFont(font)
        self.button_check_update.setWhatsThis("")
        self.button_check_update.setObjectName("button_check_update")
        self.top_menu_layout.addWidget(self.button_check_update)
        self.label_version = QtWidgets.QLabel(self.centralwidget)
        self.label_version.setMinimumSize(QtCore.QSize(50, 26))
        self.label_version.setMaximumSize(QtCore.QSize(48, 26))
        font = QtGui.QFont()
        font.setPixelSize(13)
        self.label_version.setFont(font)
        self.label_version.setWhatsThis("")
        self.label_version.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_version.setObjectName("label_version")
        self.top_menu_layout.addWidget(self.label_version)
        self.label_version_numer = QtWidgets.QLabel(self.centralwidget)
        self.label_version_numer.setMinimumSize(QtCore.QSize(35, 26))
        self.label_version_numer.setMaximumSize(QtCore.QSize(42, 26))
        font = QtGui.QFont()
        font.setPixelSize(13)
        self.label_version_numer.setFont(font)
        self.label_version_numer.setWhatsThis("")
        self.label_version_numer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_version_numer.setTextFormat(QtCore.Qt.PlainText)
        self.label_version_numer.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_version_numer.setObjectName("label_version_numer")
        self.top_menu_layout.addWidget(self.label_version_numer)
        self.button_donate = QtWidgets.QPushButton(self.centralwidget)
        self.button_donate.setMinimumSize(QtCore.QSize(56, 26))
        self.button_donate.setMaximumSize(QtCore.QSize(56, 16777215))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.button_donate.setFont(font)
        self.button_donate.setObjectName("button_donate")
        self.top_menu_layout.addWidget(self.button_donate)
        self.logo_milesight = QtWidgets.QPushButton(self.centralwidget)
        self.logo_milesight.setMinimumSize(QtCore.QSize(100, 26))
        self.logo_milesight.setMaximumSize(QtCore.QSize(100, 26))
        self.logo_milesight.setWhatsThis("")
        self.logo_milesight.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logo_milesight.setAutoFillBackground(False)
        self.logo_milesight.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logo/milesight-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logo_milesight.setIcon(icon)
        self.logo_milesight.setIconSize(QtCore.QSize(100, 200))
        self.logo_milesight.setCheckable(False)
        self.logo_milesight.setFlat(True)
        self.logo_milesight.setObjectName("logo_milesight")
        self.top_menu_layout.addWidget(self.logo_milesight)
        self.verticalLayout.addLayout(self.top_menu_layout)
        self.text_console = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_console.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_console.sizePolicy().hasHeightForWidth())
        self.text_console.setSizePolicy(sizePolicy)
        self.text_console.setMinimumSize(QtCore.QSize(0, 0))
        self.text_console.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.text_console.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPixelSize(15)
        font.setFamily("Courier New")
        self.text_console.setFont(font)
        self.text_console.setWhatsThis("")
        self.text_console.setStyleSheet("background-color:%s;color:%s;%sbackground-repeat:no-repeat;background-position:center right;" % (consbackcolor,constxtcolor,logopath))
        self.text_console.setPlaceholderText("")
        self.text_console.setObjectName("text_console")
        self.verticalLayout.addWidget(self.text_console)
        self.bottom_functions_layout = QtWidgets.QHBoxLayout()
        self.bottom_functions_layout.setSpacing(1)
        self.bottom_functions_layout.setObjectName("bottom_functions_layout")
        self.button_status = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_status.sizePolicy().hasHeightForWidth())
        self.button_status.setSizePolicy(sizePolicy)
        self.button_status.setMinimumSize(QtCore.QSize(50, 30))
        self.button_status.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_status.setFont(font)
        self.button_status.setWhatsThis("")
        self.button_status.setObjectName("button_status")
        self.bottom_functions_layout.addWidget(self.button_status)
        self.button_ping = QtWidgets.QPushButton(self.centralwidget)
        self.button_ping.setMinimumSize(QtCore.QSize(40, 30))
        self.button_ping.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_ping.setFont(font)
        self.button_ping.setWhatsThis("")
        self.button_ping.setObjectName("button_ping")
        self.bottom_functions_layout.addWidget(self.button_ping)
        self.button_sync_status = QtWidgets.QPushButton(self.centralwidget)
        self.button_sync_status.setMinimumSize(QtCore.QSize(87, 30))
        self.button_sync_status.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_sync_status.setFont(font)
        self.button_sync_status.setWhatsThis("")
        self.button_sync_status.setObjectName("button_sync_status")
        self.bottom_functions_layout.addWidget(self.button_sync_status)
        self.button_peer_book = QtWidgets.QPushButton(self.centralwidget)
        self.button_peer_book.setMinimumSize(QtCore.QSize(77, 30))
        self.button_peer_book.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_peer_book.setFont(font)
        self.button_peer_book.setWhatsThis("")
        self.button_peer_book.setObjectName("button_peer_book")
        self.bottom_functions_layout.addWidget(self.button_peer_book)
        self.button_console_log = QtWidgets.QPushButton(self.centralwidget)
        self.button_console_log.setMinimumSize(QtCore.QSize(88, 30))
        self.button_console_log.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_console_log.setFont(font)
        self.button_console_log.setWhatsThis("")
        self.button_console_log.setObjectName("button_console_log")
        self.bottom_functions_layout.addWidget(self.button_console_log)
        self.button_process_logs = QtWidgets.QPushButton(self.centralwidget)
        self.button_process_logs.setMinimumSize(QtCore.QSize(95, 30))
        self.button_process_logs.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_process_logs.setFont(font)
        self.button_process_logs.setWhatsThis("")
        self.button_process_logs.setObjectName("button_process_logs")
        self.bottom_functions_layout.addWidget(self.button_process_logs)
        self.button_disk_usage = QtWidgets.QPushButton(self.centralwidget)
        self.button_disk_usage.setMinimumSize(QtCore.QSize(80, 30))
        self.button_disk_usage.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_disk_usage.setFont(font)
        self.button_disk_usage.setWhatsThis("")
        self.button_disk_usage.setObjectName("button_disk_usage")
        self.bottom_functions_layout.addWidget(self.button_disk_usage)
        self.button_fast_sync = QtWidgets.QPushButton(self.centralwidget)
        self.button_fast_sync.setMinimumSize(QtCore.QSize(75, 30))
        self.button_fast_sync.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_fast_sync.setFont(font)
        self.button_fast_sync.setWhatsThis("")
        self.button_fast_sync.setObjectName("button_fast_sync")
        self.bottom_functions_layout.addWidget(self.button_fast_sync)
        self.button_restart_lora = QtWidgets.QPushButton(self.centralwidget)
        self.button_restart_lora.setMinimumSize(QtCore.QSize(99, 30))
        self.button_restart_lora.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_restart_lora.setFont(font)
        self.button_restart_lora.setWhatsThis("")
        self.button_restart_lora.setObjectName("button_restart_lora")
        self.bottom_functions_layout.addWidget(self.button_restart_lora)
        self.button_resume_sync = QtWidgets.QPushButton(self.centralwidget)
        self.button_resume_sync.setMinimumSize(QtCore.QSize(97, 30))
        self.button_resume_sync.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_resume_sync.setFont(font)
        self.button_resume_sync.setWhatsThis("")
        self.button_resume_sync.setObjectName("button_resume_sync")
        self.bottom_functions_layout.addWidget(self.button_resume_sync)
        self.button_restart_docker = QtWidgets.QPushButton(self.centralwidget)
        self.button_restart_docker.setMinimumSize(QtCore.QSize(110, 30))
        self.button_restart_docker.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_restart_docker.setFont(font)
        self.button_restart_docker.setWhatsThis("")
        self.button_restart_docker.setObjectName("button_restart_docker")
        self.bottom_functions_layout.addWidget(self.button_restart_docker)
        self.button_quagga_restart = QtWidgets.QPushButton(self.centralwidget)
        self.button_quagga_restart.setMinimumSize(QtCore.QSize(112, 30))
        self.button_quagga_restart.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_quagga_restart.setFont(font)
        self.button_quagga_restart.setWhatsThis("")
        self.button_quagga_restart.setObjectName("button_quagga_restart")
        self.bottom_functions_layout.addWidget(self.button_quagga_restart)
        self.button_restart_miner = QtWidgets.QPushButton(self.centralwidget)
        self.button_restart_miner.setMinimumSize(QtCore.QSize(100, 30))
        self.button_restart_miner.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.button_restart_miner.setFont(font)
        self.button_restart_miner.setWhatsThis("")
        self.button_restart_miner.setObjectName("button_restart_miner")
        self.bottom_functions_layout.addWidget(self.button_restart_miner)
        self.verticalLayout.addLayout(self.bottom_functions_layout)
        self.bottom_send_command_layout = QtWidgets.QHBoxLayout()
        self.bottom_send_command_layout.setSpacing(1)
        self.bottom_send_command_layout.setObjectName("bottom_send_command_layout")
        self.lineedit_line_command = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_line_command.setMinimumSize(QtCore.QSize(0, 30))
        self.lineedit_line_command.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPixelSize(13)
        self.lineedit_line_command.setFont(font)
        self.lineedit_line_command.setWhatsThis("")
        self.lineedit_line_command.setObjectName("lineedit_line_command")
        self.bottom_send_command_layout.addWidget(self.lineedit_line_command)
        self.button_send_command = QtWidgets.QPushButton(self.centralwidget)
        self.button_send_command.setMinimumSize(QtCore.QSize(115, 30))
        self.button_send_command.setMaximumSize(QtCore.QSize(115, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.button_send_command.setFont(font)
        self.button_send_command.setWhatsThis("")
        self.button_send_command.setObjectName("button_send_command")
        self.bottom_send_command_layout.addWidget(self.button_send_command)
        self.button_tweak = QtWidgets.QPushButton(self.centralwidget)
        self.button_tweak.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.button_tweak.setFont(font)
        self.button_tweak.setObjectName("button_tweak")
        self.bottom_send_command_layout.addWidget(self.button_tweak)
        self.button_prog1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_prog1.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.button_prog1.setFont(font)
        self.button_prog1.setObjectName("button_prog1")
        self.bottom_send_command_layout.addWidget(self.button_prog1)
        self.button_prog2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_prog2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.button_prog2.setFont(font)
        self.button_prog2.setObjectName("button_prog2")
        self.bottom_send_command_layout.addWidget(self.button_prog2)
        self.button_prog3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_prog3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.button_prog3.setFont(font)
        self.button_prog3.setObjectName("button_prog3")
        self.bottom_send_command_layout.addWidget(self.button_prog3)
        self.verticalLayout.addLayout(self.bottom_send_command_layout)
        self.verticalLayout.setStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1136, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_edit_config = QtWidgets.QAction(MainWindow)
        self.action_edit_config.setObjectName("action_edit_config")
        self.action_import_config = QtWidgets.QAction(MainWindow)
        self.action_import_config.setObjectName("action_import_config")
        self.action_export_config = QtWidgets.QAction(MainWindow)
        self.action_export_config.setObjectName("action_export_config")
        self.action_edit_snap_url = QtWidgets.QAction(MainWindow)
        self.action_edit_snap_url.setObjectName("action_edit_snap_url")
        self.menuFile.addAction(self.action_edit_config)
        self.menuFile.addAction(self.action_import_config)
        self.menuFile.addAction(self.action_export_config)
        self.menuFile.addAction(self.action_edit_snap_url)
        self.menuFile.addAction(self.action_exit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Miner Tools"))
        self.label_select_miner.setText(_translate("MainWindow", "Select Miner:"))
        self.button_open_in_browser.setText(_translate("MainWindow", "Open in Browser"))
        self.button_helium_explorer.setText(_translate("MainWindow", "Helium Explorer"))
        self.button_settings.setText(_translate("MainWindow", "Settings"))
        self.button_check_update.setText(_translate("MainWindow", "Check Update"))
        self.label_version.setText(_translate("MainWindow", "Version:"))
        self.label_version_numer.setText(_translate("MainWindow", version_build))
        self.button_donate.setText(_translate("MainWindow", "Donate"))
        self.button_status.setText(_translate("MainWindow", "Status"))
        self.button_ping.setText(_translate("MainWindow", "PING"))
        self.button_sync_status.setText(_translate("MainWindow", "Sync Status"))
        self.button_peer_book.setText(_translate("MainWindow", "Peer Book"))
        self.button_console_log.setText(_translate("MainWindow", "Console Log"))
        self.button_process_logs.setText(_translate("MainWindow", "Process Logs"))
        self.button_disk_usage.setText(_translate("MainWindow", "Disk Usage"))
        self.button_fast_sync.setText(_translate("MainWindow", "Fast Sync"))
        self.button_restart_lora.setText(_translate("MainWindow", "Restart LoRa"))
        self.button_resume_sync.setText(_translate("MainWindow", "Resume Sync"))
        self.button_restart_docker.setText(_translate("MainWindow", "Restart Docker"))
        self.button_quagga_restart.setText(_translate("MainWindow", "Quagga Restart"))
        self.button_restart_miner.setText(_translate("MainWindow", "Restart Miner"))
        self.lineedit_line_command.setText(_translate("MainWindow", "uptime"))
        self.button_send_command.setText(_translate("MainWindow", "Send Command"))
        self.button_tweak.setText(_translate("MainWindow", "Tweak Peerbook"))
        self.button_prog1.setText(_translate("MainWindow", "Programmable1"))
        self.button_prog2.setText(_translate("MainWindow", "Programmable2"))
        self.button_prog3.setText(_translate("MainWindow", "Programmable3"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))
        self.action_edit_config.setText(_translate("MainWindow", "Edit Config"))
        self.action_import_config.setText(_translate("MainWindow", "Import Config"))
        self.action_export_config.setText(_translate("MainWindow", "Export Config"))
        self.action_edit_snap_url.setText(_translate("MainWindow", "Edit Snap URL"))
import images_rc