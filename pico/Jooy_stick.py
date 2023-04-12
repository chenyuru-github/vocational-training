import machine
import time
import math

from machine import Pin, PWM
from time import sleep

servoPinL = PWM(Pin(16))
servoPinL.freq(50)
servoPinR = PWM(Pin(17))
servoPinR.freq(50)

def servoL(degrees):
    if degrees > 180:degrees=180
    if degrees < 0:degrees=0
    maxDuty=7000
    minDuty=1000
    
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    servoPinL.duty_u16(int(newDuty))
    
def servoR(degrees):
    if degrees > 180:degrees=180
    if degrees < 0:degrees=0
    maxDuty=7000
    minDuty=1000
    
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    servoPinR.duty_u16(int(newDuty))

j_x=machine.ADC(2)
j_y=machine.ADC(0)
conversion_factor = 180 / 65535 # u16 to degree

while True:
    read_x = j_x.read_u16() * conversion_factor
    read_y = j_y.read_u16() * conversion_factor
    print('{}{:5}{}{:5}'.format('X =',read_x,' Y =',read_y))
    sleep(0.1)
    if abs(read_x - 90) > 20: servoR(read_x)
    else: servoL(read_y)
