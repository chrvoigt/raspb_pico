import time
import digitalio
import board
import adafruit_matrixkeypad


# Extended 4x4 matrix keypad
cols = [digitalio.DigitalInOut(x) for x in (board.GP0, board.GP1, board.GP2, board.GP3)]
rows = [digitalio.DigitalInOut(x) for x in (board.GP4, board.GP5, board.GP6, board.GP7)]
keys = ((1, 2, 3, "A"), (4, 5, 6, "B"), (7, 8, 9, "C"), ("*", 0, "#", "D"))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)
        led.value = True
        time.sleep(0.5)
    time.sleep(0.1)
    led.value = False