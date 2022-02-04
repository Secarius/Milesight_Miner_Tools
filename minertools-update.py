from zipfile import ZipFile
import sys
import subprocess
from asyncio import subprocess
from subprocess import Popen
import psutil
import pathlib
import time
import os

def wait_until():
    while True:
        if ("MinerTools.exe" in (p.name() for p in psutil.process_iter())): 
            time.sleep(5)
            print("läuft")
        else:
            print("läuft nicht")
            return False

updatepath = pathlib.Path().resolve()
print(updatepath)
f = open("startupdate.txt","w+")
f.write(str(updatepath))
f.close
wait_until()
print("unzipping .......................")
with ZipFile('miner-update.zip', 'r') as zipOjk:
    zipOjk.extractall()
f = open("endupdate.txt","w+")
f.write("geupdated")
f.close
updater = str(updatepath)
print(updater + "\\MinerTools.exe")
Popen('%s\\MinerTools.exe' % updater)
myfile="miner-update.zip"
## If file exists, delete it ##
if os.path.isfile(myfile):
    os.remove(myfile)
else:    ## Show an error ##
    print("Error: %s file not found" % myfile)
myfile="updater.zip"
## If file exists, delete it ##
if os.path.isfile(myfile):
    os.remove(myfile)
else:    ## Show an error ##
    print("Error: %s file not found" % myfile)
sys.exit()