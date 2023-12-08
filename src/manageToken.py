import RPi.GPIO as GPIO
import time
import json
from readToken import read_rfid_card
from pydub import AudioSegment
from pydub.playback import play
import pygame
import serial


DEBUG = True  # Set this to False when you want to disable debug output

# row_pins = [2, 3, 4, 17, 27]  # 5 Zeilen
# col_pins = [5, 6,13, 19, 26, 21, 20, 16, 12, 25]
# Get Config from File
with open('config.json', 'r') as json_file:
    config = json.load(json_file)

#row_pins = config['GPIOMatrix']['row_pins']
#col_pins = config['GPIOMatrix']['col_pins']

BaseLength = config['SoundSetup']['BaseLength']
Ton1 = config['CardIDs']['Ton1']
Ton2 = config['CardIDs']['Ton2']
Ton4 = config['CardIDs']['Ton4']
Ton8 = config['CardIDs']['Ton8']
MasterKeys = config['CardIDs']['masterKeys']

Row0 = config['PinLayout']['0']
Row1 = config['PinLayout']['1']
Row2 = config['PinLayout']['2']
Row3 = config['PinLayout']['3']
Row4 = config['PinLayout']['4']

arduino = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)  # Anpassen des COM-Ports
time.sleep(2)  # Eine kurze Wartezeit für die Stabilität der Verbindung



def dprint(*args):
    if DEBUG:
        print(f"DEBUG:", *args)

def setuptones():
    dprint("MasterKey read:", card_id)


def playSound(BaseLength, row):
    dprint(card_id, "in SoundMatrix", BaseLength, row, "play song")
    song = AudioSegment.from_mp3(config['GPIORowToMP3'][str(row)][str(BaseLength)])
    if song:
        dprint("SongLoaded")
    play(song)


def play_mp3(BaseLength, row):
    pygame.mixer.init()
    f = open(config['GPIORowToMP3'][str(row)][str(int(BaseLength))])
    pygame.mixer.music.load(f)
    pygame.mixer.music.play()

    # Allow the music to play
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    f.close()

def CheckCardIDs(card_id):
    if card_id in MasterKeys:
        setuptones()
    if card_id in Ton1:
        #playSound(BaseLength, row)
        play_mp3(BaseLength, row[0])
    if card_id in Ton2:
        play_mp3(BaseLength/2, row[0])
    if card_id in Ton4:
        play_mp3(BaseLength/4, row[0])
    if card_id in Ton8:
        play_mp3(BaseLength/8, row[0])


def find_keys_with_value_in_lists(config_dict, value):
    matching_keys = []
    for key, value_list in config_dict.items():
        if value in value_list:
            matching_keys.append(key)
    return matching_keys


if __name__ == "__main__":

    try:
        while True:
            received_data = int(arduino.readline().decode().strip())
            dprint(f"Empfangener Pin: {received_data}")
            row = find_keys_with_value_in_lists(config['PinLayout'], received_data)
            card_id = read_rfid_card()
            if card_id:
                        dprint("ID des gelesenen RFID-Chips:", card_id,
                          " in Row", row[0])     
                        CheckCardIDs(card_id)
            #time.sleep(0.1) 
            arduino.write(b"OK\n")
            
                
            
            
    except KeyboardInterrupt:
        pass

    # Aufräumen und GPIO-Pins freigeben
    GPIO.cleanup()