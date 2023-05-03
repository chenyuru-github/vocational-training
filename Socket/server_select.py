# -*- coding: utf-8 -*-
"""
Created on Oct 29,2022
@author: joseph@艾思程式教育

 Create TCP server with select
"""


import socket, select
import sys
import utility

#-----------------------------
'''Handle the CTRL-C signal.'''
def close_socket(sig):
    print('Server Socket Closed')
    server_socket.close()

def install_handler():
    if 'win' in sys.platform :
        import win32api
        win32api.SetConsoleCtrlHandler(close_socket, True)
    elif 'linux' in sys.platform :
        print('you may install crtl-C signal handler for Linux')        

install_handler()
#--------------------------------------------

def handle_client_exit(sock):
    print("Client (%s, %s) is offline" % MessageQueue[sock]['sock_info'])
    sock.close()
    CONNECTION_LIST.remove(sock)
    del MessageQueue[sock]
    
    


CONNECTION_LIST = []	# list of socket clients
RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
PORT = 7000
    
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(10)

# Add server socket to the list of readable connections
CONNECTION_LIST.append(server_socket)

print("Chat server started at {}:{} ...." .format(utility.get_ip(),str(PORT)))
MessageQueue={}

while 1:
    # Get the list sockets which are ready to be read through select
    try:
        read_sockets,write_sockets,error_sockets = \
        select.select(CONNECTION_LIST,CONNECTION_LIST,[])

    except socket.error as e: 
        print("Client Connection error: %s" % e) 
        print('Abnormally terminate program')
        sys.exit(1)
        
    #print('accpet return ')
    for sock in read_sockets:
        
        #New connection
        if sock == server_socket:
            # Handle the case in which there is a new connection recieved through server_socket
            
            sockfd, addr = server_socket.accept()
            CONNECTION_LIST.append(sockfd)
            MessageQueue[sockfd]={'sock_info':addr,'buf':[]}
            print("(%s, %s) connected" % addr)
            
        #Some incoming message from a client
        else:
            # Data recieved from client, process it
            try:
                #In Windows, sometimes when a TCP program closes abruptly,
                # a "Connection reset by peer" exception will be thrown
                data = sock.recv(RECV_BUFFER)
                # echo back the client message
                if data:
                   
                    if data.decode()=='quit':
                        handle_client_exit(sock)
                        continue
                     
                    print('{}:{}'.format(MessageQueue[sock]['sock_info'],data.decode()))

            # client disconnected, so remove from socket list
            except:
                handle_client_exit(sock)

                continue
    
server_socket.close()