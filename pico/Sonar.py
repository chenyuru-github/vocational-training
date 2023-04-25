import time, math
from machine import Pin, PWM

pin_led = Pin(25, Pin.OUT)
trig = Pin(10, Pin.OUT)
echo = Pin(4, Pin.IN, Pin.PULL_DOWN)

buzzer = PWM(Pin(28))
ledPin=[Pin(14, Pin.OUT), Pin(15, Pin.OUT)]

def ping():
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    count = 0
    timeout = False
    start = time.ticks_us()
    
    while not echo.value(): #wait for HIGH
        start=time.ticks_us()
    while echo.value() : #wait for HIGH
        stop=time.ticks_us()
    duration = stop - start
    dist = ( duration *0.0343) /2
    return dist  
    
def bi(T):
    buzzer.duty_u16(68)
    time.sleep(0.5)
    buzzer.duty_u16(65535)
    time.sleep(T)
    
step_time = 1

while True:
    distance = round(ping())
    print("%s cm" % distance)
    if distance > 50 :
        buzzer.duty_u16(0)
        time.sleep(0.8)
    if (distance <= 55) and (distance > 40) :
        bi(0.6)       
    if (distance <= 40) and (distance > 25) :
        bi(0.4)
    if (distance <= 25) and (distance > 8) :
        bi(0.2)
    if (distance <= 8)  :
        buzzer.duty_u16(68)
