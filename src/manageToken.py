from read2 import read_rfid_card
import time

if __name__ == "__main__":
    while True:
        card_id = read_rfid_card()
        print("ID des gelesenen RFID-Chips:", card_id)
        time.sleep(0.5)
    # Führen Sie hier weitere Aktionen mit der card_id durch
