import machine
import time
import _thread
from machine import Pin
from time import sleep

btn0 = machine.Pin (11,Pin.IN,Pin.PULL_UP)
ledPin=[Pin(25, Pin.OUT),Pin(14, Pin.OUT),Pin(15, Pin.OUT)]
clockwise = True

def thread_0():
        while True:
            if btn0.value() == 0:
                print("Hello from thread")
                global clockwise
                clockwise = not clockwise
                break
            
_thread.start_new_thread(thread_0, ())

for i in ledPin :
    i.off() # init led
    
while True:
    if clockwise == False :
        for i in ledPin :
            i.toggle()
            sleep(1)
            i.toggle()
            if clockwise == True :
                _thread.start_new_thread(thread_0, ())
                break
    else:
        for i in ledPin[::-1] :    
            i.toggle()
            sleep(1)
            i.toggle()
            if clockwise == False :
                _thread.start_new_thread(thread_0, ())
                break