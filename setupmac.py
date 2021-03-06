import distutils
import sys
import os
from cx_Freeze import setup, Executable

#Application information
name = 'Miner Controler'
version = '1.1.7'
author = 'Milesight'
author_email = 'sample@example.xxx'
url = 'http://example.xxx'
description = 'Milesight Tool Collection'

#Specify the GUID here (basically it should not be changed)
upgrade_code = '{06637B9A-C07C-37DA-B531-782F798FE871}'
#For 64-bit Windows, switch the installation folder
# ProgramFiles(64)Folder seems to be replaced with the actual directory on the msi side
programfiles_dir = 'ProgramFiles64Folder' if distutils.util.get_platform() == 'win-amd64' else 'ProgramFilesFolder'

#Options to use with the build command on Windows+
build_exe_options = {
    'packages': ['os'],
    # 'excludes': [''], #Exclude tkinter as it is not used
    # 'includes': [''],
    'include_files': ['assets/'],
    'include_msvcr': True #Since it uses PySide, it cannot be started unless Microsoft's C runtime is included.
}

# bdist_Options to use with the msi command
bdist_msi_options = {
    'upgrade_code': upgrade_code,
    'add_to_path': False,
    'initial_target_dir': '[%s]\%s\%s' % (programfiles_dir, author, name),
    'install_icon': 'assets/helium.ico'
}

bdist_mac_options = {
    'iconfile': 'assets/helium.ico',
    'bundle_name': 'Miner Tools'
}

options = {
    'bdist_mac': bdist_mac_options
}

#exe information
base = 'Win32GUI' if sys.platform == 'win32' else None
icon = 'assets/helium.ico'

mainexe = Executable(
    'main-mac.py',
    target_name = 'MinerTools.app',
    base = base,
    icon = icon,
    shortcut_name ="Milesight MinerTools",
    shortcut_dir ="DesktopFolder"
)

setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    url=url,
    description=description,
    options=options,
    executables=[mainexe]
)