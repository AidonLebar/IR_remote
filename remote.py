import serial
from pynput.keyboard import Key, Controller

serial_path = '/dev/ttyUSB0'

def press(key):
    keyboard.press(key)
    keyboard.release(key)

#press a key with super modifier key - MAC
def super_press(key):
    keyboard.press(Key.cmd_r)
    press(key)
    keyboard.release(Key.cmd_r)

#press a key with ctrl held
def ctrl_press(key):
    keyboard.press(Key.ctrl)
    press(key)
    keyboard.release(Key.ctrl)

with serial.Serial(serial_path, 9600) as ser:
    keyboard = Controller()
    while(True):
        button = str(ser.readline(), 'ascii').strip()
        if(button == "OK"): #play/pause
            press(Key.space)
        if(button == "U"): #volume up
            keyboard.press(Key.ctrl_r)
            keyboard.press(Key.shift_r)
            press(Key.up)
            keyboard.release(Key.shift_r)
            keyboard.release(Key.ctrl_r)
        if(button == "D"): #volume down
            keyboard.press(Key.ctrl_r)
            keyboard.press(Key.shift_r)
            press(Key.down)
            keyboard.release(Key.shift_r)
            keyboard.release(Key.ctrl_r)
        if(button == "R"): #skip forward
            press(Key.right)
        if(button == "L"): #skip back
            press(Key.left)
        if(button == "1"): #netflix fullscreen
            press("f")
        if(button == "2"): #VLC fullscreen and minimal interface
            ctrl_press("h")
            press(Key.f11)
