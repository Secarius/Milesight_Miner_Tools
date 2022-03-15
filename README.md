# Milesight_Miner_Tools

## Build Programm

```bash
python setupwin.py bdist_msi
```

```bash
python setupwin.py build
```

```bash
pyinstaller --name="MinerToolsMac" --windowed --icon assets/helium.ico --onefile main-mac.py
```

## Generate GUI
```bash
pyrcc5 -o images_rc.py images.qrc

pyuic5 minertools_gui_main_window.ui > newgui.py 
```

## Font Changes

setPixelSize