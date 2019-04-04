import serial
from pynput.keyboard import Key, Controller

serial_path = '/dev/ttyUSB0'

def press(key):
    keyboard.press(key)
    keyboard.release(key)

#press a key with super modifier key
def super_press(key):
    keyboard.press(Key.cmd_r)
    press(key)
    keyboard.release(Key.cmd_r)

with serial.Serial(serial_path, 9600) as ser:
    keyboard = Controller()
    while(True):
        button = str(ser.readline(), 'ascii').strip()
        if(button == "OK"): #play/pause
            press(Key.space)
        if(button == "U"): #volume up
            keyboard.press(Key.ctrl_r)
            keyboard.press(Key.shift_r)
            keyboard.press(Key.up)
            keyboard.release(Key.up)
            keyboard.release(Key.shift_r)
            keyboard.release(Key.ctrl_r)
        if(button == "D"): #volume down
            keyboard.press(Key.ctrl_r)
            keyboard.press(Key.shift_r)
            keyboard.press(Key.down)
            keyboard.release(Key.down)
            keyboard.release(Key.shift_r)
            keyboard.release(Key.ctrl_r)
        if(button == "R"): #skip forward
            keyboard.press(Key.right)
            keyboard.release(Key.right)
        if(button == "L"): #skip back
            keyboard.press(Key.left)
            keyboard.release(Key.left)
