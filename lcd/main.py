from pico_lcd import I2cLcd
from machine import Pin, I2C
import utime as time
from hcsr04 import HCSR04


i2c = I2C(id=0,scl=Pin(1),sda=Pin(0),freq=100000)                             
lcd = I2cLcd(i2c, 0x27, 2, 16) # LCD 16x2

lcd.putstr('Hello World')

sensor = HCSR04(trigger_pin=3, echo_pin=2)
max_dist = 20

while True:
    dist = int(sensor.distance_cm())
    print(dist)
    lcd.clear()
    lcd.move_to(5,0)
    lcd.putstr(str(dist))
    lcd.move_to(8,0)
    lcd.putstr('cm')
    time.sleep(0.5)
    
