import RPi.GPIO as GPIO
import time
from src.readToken import read_rfid_card

# GPIO-Pinnummern für Zeilen und Spalten
row_pins = [2, 3, 4, 17, 27]  # 5 Zeilen
col_pins = [5, 6,13, 19, 26, 21, 20, 16, 12, 25]  # 10 Spalten

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
                    time.sleep(0.1)  # Kurze Pause, um die LED anzuzünden

                    # Use Imported file to read CardID
                    card_id = read_rfid_card()
                    if card_id:
                        print("ID des gelesenen RFID-Chips:", card_id,
                              " in Row", row, " and in Collum", col)

                    # Spalte deaktivieren (LOW), um die LED auszuschalten
                    GPIO.output(col_pins[col], GPIO.LOW)

                # Zeile deaktivieren (LOW)
                GPIO.output(row_pins[row], GPIO.LOW)

    except KeyboardInterrupt:
        pass

    # Aufräumen und GPIO-Pins freigeben
    GPIO.cleanup()
