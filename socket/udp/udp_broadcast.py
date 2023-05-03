# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:51:31 2023

@author: joseph@艾鍗學院

UDP broadcast example
"""

import socket
import time
import random

localIP     = "127.0.0.1"

localPort   = 3500

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Enable broadcasting mode
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Bind to address and ip
server.bind((localIP, localPort))



while True:
    temperature=str(round(random.uniform(30,60),2))
    bytesToSend= str.encode(temperature)
    #the below has the same meaning
    #bytesToSend = b"temperature"
    server.sendto(bytesToSend, ('<broadcast>', 3500))
    #server.sendto(bytesToSend, some_address)
    
    print("message sent:{}".format(temperature))
    time.sleep(1)