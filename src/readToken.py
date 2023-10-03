import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def read_rfid_card():

    # Erstellen Sie eine Instanz der SimpleMFRC522-Klasse
    reader = SimpleMFRC522()

    try:
        # Lesen Sie die RFID-Karte
        id = reader.read_id_no_block()
        return id
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    card_id = read_rfid_card()
    print(card_id)
