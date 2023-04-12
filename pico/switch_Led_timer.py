import machine
import time
from machine import Pin, Timer
from time import sleep

btn0 = machine.Pin (11,Pin.IN,Pin.PULL_UP)
ledPin = [Pin(25, Pin.OUT),Pin(14, Pin.OUT),Pin(15, Pin.OUT)]
t = Timer()

def tick(t):
    ledPin[1].toggle()
    
t.init(period=500, mode=Timer.PERIODIC, callback=tick)

while True :
    ledPin[0].toggle()
    sleep(1)