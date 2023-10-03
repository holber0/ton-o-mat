from readToken import read_rfid_card
import time
import RPi.GPIO as GPIO

READER1_GPIO = 5  # Wählen Sie einen verfügbaren GPIO-Pin für Lesegerät 1
READER2_GPIO = 6  # Wählen Sie einen verfügbaren GPIO-Pin für Lesegerät 2

GPIO.cleanup()


def switchGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(READER1_GPIO, GPIO.OUT)
    GPIO.setup(READER2_GPIO, GPIO.OUT)
    if GPIO.input(READER1_GPIO) == GPIO.HIGH:
        GPIO.output(READER1_GPIO, GPIO.LOW)
        GPIO.output(READER2_GPIO, GPIO.HIGH)
    else:
        GPIO.output(READER1_GPIO, GPIO.HIGH) 
        GPIO.output(READER2_GPIO, GPIO.LOW)
        
if __name__ == "__main__":
    while True:
        card_id = read_rfid_card()
        if card_id: 
            print("ID des gelesenen RFID-Chips:", card_id)
        switchGPIO()
        time.sleep(0.5)
    # Führen Sie hier weitere Aktionen mit der card_id durch
