from zipfile import ZipFile
import sys
import subprocess

with ZipFile('miner-update.zip', 'r') as zipOjk:
    zipOjk.extractall()

subprocess.call(['MinerTools.exe'])
sys.exit()