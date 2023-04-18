from machine import Pin, I2C, UART, ADC
import time

i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=100000)

print ('Scan i2c bus...')
devices = i2c.scan()

if len(devices) > 0:
    print ('i2c devices is found. count=',len(devices))
else:
    print ('Not Found i2c')

for device in devices:
    print ('Decimal address:',device,'| Hexa address:',hex(device))