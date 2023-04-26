from machine import Pin
import machine
import utime

x=0
wifi_ready=0
uart = machine.UART(1,tx=Pin(8),rx=Pin(9),baudrate=115200)
led = Pin(25,Pin.OUT)

#=======MQTT/Line notify========
reset='RESET'
ssid = 'SSID,ZONE_Ru'   #
password = 'PSWD,46(477uG'   #
mqtt_server = 'BROKER,mqttgo.io'
topic_sub = 'TOPIC,subto/qwer/zxcv'
topic_pub1= 'TOPIC1,pubto/qwer/hjkl'  
ready='ready'

def sendCMD_waitResp(cmd, uart=uart, timeout=1000):
    print(cmd)
    uart.write(cmd+'\r\n')
    waitResp()
   
def waitResp(uart=uart, timeout=1000):
    global data,wifi_ready
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prvMills)<timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    if resp != b'' :
        resp = str(resp)
        print(resp)
        if (resp.find('connect'))>=0:
            wifi_ready=1
            
sendCMD_waitResp(reset)
utime.sleep(0.5)
sendCMD_waitResp(ssid)
utime.sleep(0.1)
sendCMD_waitResp(password)
utime.sleep(0.1)
sendCMD_waitResp(mqtt_server)
utime.sleep(0.1)
sendCMD_waitResp(topic_sub)
utime.sleep(0.1)
sendCMD_waitResp(topic_pub1)
utime.sleep(0.1)
sendCMD_waitResp(ready)

while (not wifi_ready) :
    utime.sleep(0.3)
    led.value(1)
    print('.')
    utime.sleep(0.3)
    led.value(0)
    print('.')
    waitResp()    
print('start')
utime.sleep(1)
while True :
    waitResp()
    x+=1
    y=str(x)
    sendCMD_waitResp('PB1,'+y)
    utime.sleep(1)