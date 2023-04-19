from ssd1306 import SSD1306_I2C
from machine import Pin, I2C, UART, ADC, PWM
import framebuf
import machine
import time
import math

ledPin = [Pin(14, Pin.OUT),Pin(15, Pin.OUT)]
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / 65535
i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)

for led in ledPin:
    led.off()

while True:
    reading = sensor_temp.read_u16()*conversion_factor
    temp = round(27 - (reading - 0.706) / 0.001721, 2)
    if temp > 21 :
        ledPin[0].on()
        ledPin[1].off()
    elif temp <= 21:
        ledPin[1].on()
        ledPin[0].off()
        
    oled.text(str(temp), 48, 30)
    oled.show()
    time.sleep(0.1)
    oled.fill(0)
