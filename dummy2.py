import serial
import time

# Define the serial connection
arduino = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)  # Adjust port if necessary

# Function to send pin number command to Arduino to turn it ON
def turn_on_pin_on_arduino(pin_number):
    arduino.write(f"{pin_number}\n".encode())  # Send command to turn on specified pin
    print(f"Turned ON pin {pin_number}")

# Function to send pin number command to Arduino to turn it OFF
def turn_off_pin_on_arduino(pin_number):
    arduino.write(f"{pin_number}\n".encode())  # Send command to turn off specified pin
    print(f"Turned OFF pin {pin_number}")

# Example: Send commands to turn pin number 13 on and off repeatedly
pin_number_to_control = 13

while True:
    turn_on_pin_on_arduino(pin_number_to_control)
    time.sleep(1)  # Wait for 2 seconds
    turn_off_pin_on_arduino(pin_number_to_control)
    time.sleep(1)  # Wait for 2 seconds before turning on again
