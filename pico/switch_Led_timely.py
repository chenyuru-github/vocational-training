import machine
import time
from machine import Pin, Timer
from time import sleep

btn0 = machine.Pin (11,Pin.IN,Pin.PULL_UP)

ledPin = [Pin(25, Pin.OUT),Pin(14, Pin.OUT),Pin(15, Pin.OUT)]

clockwise = True

def int_handler(pin):
    print("Interrupt Detected!")
    global clockwise
    clockwise = not clockwise

btn0.irq(handler=None) # init handle
btn0.irq(trigger=Pin.IRQ_FALLING, handler=int_handler)

for i in ledPin :
    i.off() # init led
    
while True :
    if clockwise == 0 :
        for i in ledPin :
            i.toggle()
            sleep(0.5)
            i.toggle()
            if clockwise == 1 :
                break
    else:
        for i in ledPin[::-1] :    
            i.toggle()
            sleep(0.5)
            i.toggle()
            if clockwise == 0 :
                break