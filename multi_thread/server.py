#!/usr/bin/python 
import socket
import logging
import time
import signal
import threading

#Basic multi-threaded TCP socket server.

logging.basicConfig(level=logging.DEBUG)

host = ''
port = 20222
addr = (host, port)

def connection_handler(con_number):
    logging.debug('Starting new listener: '+str(con_number))
    con, client = serv_socket.accept()
    t = threading.Thread(target=message_handler,args=(con_number,con))
    t.start()  
    con_number += 1
    logging.debug('Connection received.')
    t2 = threading.Thread(target=connection_handler, args=(con_number,))
    t2.start()

def message_handler(con_number,con):
    logging.debug('ID '+ str(con_number)+': Waiting for messages...')
    while True:
        recebe = con.recv(1024) 
        if not recebe:
            logging.debug('ID '+str(con_number)+': Socket closing connection')
            serv_socket.close()
            break
        if len(recebe) > 0:
            logging.debug (str('ID '+str(con_number)+' Message: '+recebe.decode()))
            with open('data.txt', 'a') as data:
                data.write(str(recebe.decode())+"\n")
    return 0

con_number = 0
logging.debug('Thread '+ str(con_number)+ ': Waiting for new connections.')
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 20)
serv_socket.bind(addr)
serv_socket.listen(10)
t = threading.Thread(target=connection_handler, args=(con_number,))  
t.start()
