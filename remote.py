import serial
from pynput.keyboard import Key, Controller

serial_path = '/dev/ttyUSB0'

def press(key):
    keyboard.press(key)
    keyboard.release(key)

#press a key with super modifier key
def super_press(key):
    keyboard.press(Key.cmd_r)
    keyboard.press(key)
    keyboard.release(key)
    keyboard.release(Key.cmd_r)

with serial.Serial(serial_path, 9600) as ser:
    keyboard = Controller()
    while(True):
        button = str(ser.readline(), 'ascii').strip()
        if(button == "OK"):
            press(Key.space)
        if(button == "U"):
            super_press(Key.f12)
        if(button == "D"):
            super_press(Key.f11)
