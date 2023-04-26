from machine import Pin
from machine import I2C
from machine import PWM
from time import sleep_ms
from tcs34725 import TCS34725

sensor = I2C(0, sda=Pin(12), scl=Pin(13))
tcs =TCS34725(sensor)

while True:
    print(tcs.read('dec'))
    print(tcs.read('raw'))
    sleep_ms(1000)