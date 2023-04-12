from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(25))

pwm.freq(40)

while True:
    for duty in range(1000,20000,1):
        pwm.duty_u16(duty)
        sleep(0.001)
    sleep(0.3)
    for duty in range(20000, 1000, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)
    sleep(0.3)