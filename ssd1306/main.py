from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
from hcsr04 import HCSR04

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(64, 48, i2c)
sensor = HCSR04(trigger_pin=3, echo_pin=2)
max_dist = 20

while True:
    oled.fill(0) # clear the display
    for jj in range(64): # loop through horizontal display resolution
        dist_pt = sensor.distance_cm()
        if dist_pt > max_dist: dist_pt =max_dist      
        plot_pt = (1-dist_pt/max_dist+0.0025)*46 # convert to OLED pixels
        if plot_pt > 47: plot_pt =47
        print(int(plot_pt))
        oled.text('.',jj,int(plot_pt)) # update x=jj with data point
    oled.show() 
    
     
    






