import RPi.GPIO as GPIO
import time
import json
from readToken import read_rfid_card

DEBUG = True  # Set this to False when you want to disable debug output

#row_pins = [2, 3, 4, 17, 27]  # 5 Zeilen
#col_pins = [5, 6,13, 19, 26, 21, 20, 16, 12, 25]
#Get Config from File
with open('config.json', 'r') as json_file:
    config = json.load(json_file)

row_pins = config['GPIOMatrix']['row_pins']
col_pins = config['GPIOMatrix']['col_pins']


def dprint(*args):
    if DEBUG:
        print(f"DEBUG:", *args)


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
            for row in range(len(row_pins)):
                # Zeile aktivieren (HIGH)
                GPIO.output(row_pins[row], GPIO.HIGH)

                for col in range(len(col_pins)):
                    # Spalte aktivieren (HIGH), um die LED einzuschalten
                    GPIO.output(col_pins[col], GPIO.HIGH)
                    #time.sleep(0.1)  # Kurze Pause, um die LED anzuzünden

                    # Use Imported file to read CardID
                    card_id = read_rfid_card()
                    
                    if card_id:

                        dprint("ID des gelesenen RFID-Chips:", card_id,
                              " in Row", row, " and in Collum", col)
                        
                    # Spalte deaktivieren (LOW), um die LED auszuschalten
                    GPIO.output(col_pins[col], GPIO.LOW)

                # Zeile deaktivieren (LOW)
                GPIO.output(row_pins[row], GPIO.LOW)

    except KeyboardInterrupt:
        pass

    # Aufräumen und GPIO-Pins freigeben
    GPIO.cleanup()
