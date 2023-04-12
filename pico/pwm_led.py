from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(25))

pwm.freq(60)

while True:
    for duty in range(1000, 60000, 100):
        pwm.duty_u16(duty)
        sleep(0.001)
    sleep(0.1)
    for duty in range(60000, 1000, -100):
        pwm.duty_u16(duty)
        sleep(0.001)
    sleep(0.1)
