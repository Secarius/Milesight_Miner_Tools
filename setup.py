import distutils
import sys
import os
from cx_Freeze import setup, Executable

#Application information
name = 'Miner Controler'
version = '1.0.5'
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
    'include_files': ['assets/', 'config/'],
    'include_msvcr': True #Since it uses PySide, it cannot be started unless Microsoft's C runtime is included.
}

# bdist_Options to use with the msi command
bdist_msi_options = {
    'upgrade_code': upgrade_code,
    'add_to_path': False,
    'initial_target_dir': '[%s]\%s\%s' % (programfiles_dir, author, name)
}

options = {
    'build_exe': build_exe_options,
    'bdist_msi': bdist_msi_options
}

#exe information
base = 'Win32GUI' if sys.platform == 'win32' else None
icon = 'assets\helium.ico'

mainexe = Executable(
    'main.py',
    targetName = 'MinerTools.exe',
    base = base,
    icon = icon,
    shortcutName="Milesight MinerTools",
    shortcutDir="DesktopFolder"
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