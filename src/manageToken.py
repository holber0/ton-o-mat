import RPi.GPIO as GPIO
import time
import json
from readToken import read_rfid_card
from pydub import AudioSegment
from pydub.playback import play
import pygame



DEBUG = True  # Set this to False when you want to disable debug output

# row_pins = [2, 3, 4, 17, 27]  # 5 Zeilen
# col_pins = [5, 6,13, 19, 26, 21, 20, 16, 12, 25]
# Get Config from File
with open('config.json', 'r') as json_file:
    config = json.load(json_file)

row_pins = config['GPIOMatrix']['row_pins']
col_pins = config['GPIOMatrix']['col_pins']

BaseLength = config['SoundSetup']['BaseLength']
Ton1 = config['CardIDs']['Ton1']
Ton2 = config['CardIDs']['Ton2']
Ton4 = config['CardIDs']['Ton4']
Ton8 = config['CardIDs']['Ton8']
MasterKeys = config['CardIDs']['masterKeys']




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
    pygame.mixer.music.load(config['GPIORowToMP3'][str(row)][str(BaseLength)])
    pygame.mixer.music.play()

    # Allow the music to play
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Example usage
# Replace with the path to your MP3 file


    #song = AudioSegment.from_mp3(sound)

    

def CheckCardIDs(card_id):
    if card_id in MasterKeys:
        setuptones()
    if card_id in Ton1:
        #playSound(BaseLength, row)
        play_mp3(BaseLength, row)
    if card_id in Ton2:
        play_mp3(BaseLength/2, row)
    if card_id in Ton4:
        play_mp3(BaseLength/4, row)
    if card_id in Ton8:
        play_mp3(BaseLength/8, row)


# GPIO-Modus festlegen
GPIO.setmode(GPIO.BCM)
# Init: GPIO-Pins als Ausgänge für Zeilen und Spalten konfigurieren
for pin in row_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
for pin in col_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


if __name__ == "__main__":

    try:
        while True:
            for col in range(len(col_pins)):
                # Zeile aktivieren (HIGH)
                GPIO.output(col_pins[col], GPIO.HIGH)
                for row in range(len(row_pins)):
                    # Spalte aktivieren (HIGH), um die LED einzuschalten
                    GPIO.output(row_pins[row], GPIO.HIGH)
                    time.sleep(0.1)
                    card_id = read_rfid_card()
                    # Kurze Pause um die CardID zu lesen
                    if card_id:
                        dprint("ID des gelesenen RFID-Chips:", card_id,
                          " in Row", row, " and in Collum", col)     
                        
                        CheckCardIDs(card_id)
                                       
                      
                    

                    # Spalte deaktivieren (LOW), um die LED auszuschalten
                    GPIO.output(row_pins[row], GPIO.LOW)

                # Zeile deaktivieren (LOW)(col_pins[col]
                GPIO.output(col_pins[col], GPIO.LOW)

    except KeyboardInterrupt:
        pass

    # Aufräumen und GPIO-Pins freigeben
    GPIO.cleanup()