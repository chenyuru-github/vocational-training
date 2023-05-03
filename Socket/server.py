# -*- coding: utf-8 -*-
"""
Created on Oct 29,2022
@author: joseph@艾思程式教育

Simple TCP server

"""
import socket
import sys

#-----------------------------
'''Handle the CTRL-C signal.'''
def close_socket(sig):
    print('Server Socket Closed')
    server_socket.close()
    sys.exit(1)

def install_handler():
    if 'win' in sys.platform :
        import win32api
        win32api.SetConsoleCtrlHandler(close_socket, True)
    elif 'linux' in sys.platform :
        print('you may install crtl-C signal handler for Linux')        

install_handler()
#--------------------------------------------

HOST = '127.0.0.1'
PORT = 65535

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen(5)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    try:
        conn, addr = server_socket.accept()
        print("Connection from: " + str(addr))
    except socket.error as e: 
        print('Abnormally terminate program')
        sys.exit(1)

    while True:
        try :
            indata = conn.recv(1024)
        except socket.error as e: 
            #print("Client Connection error: %s" % e)    
            print("Client (%s, %s) is offline" % addr)                     
            break
            
        if len(indata) == 0 or indata.decode()=='quit': # connection closed
            conn.close()
            print("Client (%s, %s) is offline" % addr)
            break
        
        print('recv: ' + indata.decode())
          
        #echo the message to client
        outdata = 'echo ' + indata.decode()
        conn.send(outdata.encode())




