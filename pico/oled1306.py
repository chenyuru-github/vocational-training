from machine import Pin, I2C, UART, ADC
from ssd1306 import SSD1306_I2C
import time

i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)

oled.invert(1)
for i in range(0,11,1):
    disp = str(i)
    oled.text(disp, 10, 12)
    oled.show()
    time.sleep(0.5)
    oled.fill(0)
oled.text('IT Training', 12,12)
oled.show()