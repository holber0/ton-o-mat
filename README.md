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

## Pyton Settings
\
the Virtual env "env" is used in ths Repo. Use `pip -r requirements.txt` to install all requirements\
if not install:
 
 ```
pip install spidev
pip install mfrc522
 ```




