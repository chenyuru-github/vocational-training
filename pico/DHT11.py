from machine import Pin
import utime as time
from lib.dht import DHT11

pin = Pin(28, Pin.OUT, Pin.PULL_UP)
sensor = DHT11(pin)
while True:
    time.sleep(0.5)
    t = (sensor.temperature)
    h = round(sensor.humidity)
    print("Temperature: {}".format(t))
    print("Humidity: {}".format(h))
    time.sleep(1)