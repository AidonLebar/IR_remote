import serial
from pynput.keyboard import Key, Controller
with serial.Serial('/dev/tty.usbserial-1410', 9600) as ser:
    keyboard = Controller()
    while(True):
        button = str(ser.readline(), 'ascii').strip()
        if(button == "OK"):
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        if(button == "U"):
            keyboard.press(Key.cmd_r)
            keyboard.press(Key.f12)
            keyboard.release(Key.f12)
            keyboard.release(Key.cmd_r)
        if(button == "D"):
            keyboard.press(Key.cmd_r)
            keyboard.press(Key.f11)
            keyboard.release(Key.f11)
            keyboard.release(Key.cmd_r)
