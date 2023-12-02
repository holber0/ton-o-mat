# ton-O-mat
 ton-O-mat is a Interatcive sound generator that allows Kids to learn the one scale
 
## Inititial Setup
Enable SPI Bus:
```
sudo nano /boot/config.txt
```
Add following at the end of the File:
```
device_tree_param=spi=on
dtoverlay=spi-bcm2708
```
\
use `sudo raspi-config` to Enable „Advanced Options“ > „SPI“ restart afterwards `sudo reboot now`

## fluidsynth

fluidsynth is need as a background Service prividing a Midi Port for Pyton
```
fluidsynth -a alsa -m alsa_seq -i -l -s -g 1.0 /usr/share/sounds/sf2/FluidR3_GM.sf2
```

## Pyton Settings
\
the Virtual env "env" is used in ths Repo. Use `pip -r requirements.txt` to install all requirements\
if not install:
 
 ```
pip3 install virtualenv
pip install spidev
pip install mfrc522
 ```

source the activate file to switch to the venv 
```
source env/bin/activate
```




