#!/usr/bin/python 
import socket
import logging
import time
import signal

#Basic single threaded TCP socket server.

logging.basicConfig(level=logging.DEBUG)

host = ''
port = 20101
addr = (host, port)

recebe = ''
while True:
    logging.debug('Listening to PORT '+str(port))
    logging.debug('Waiting for connection.')
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_socket.bind(addr)
    serv_socket.listen(10)
    con, client = serv_socket.accept()
    logging.debug('Accepting connections.')
    logging.debug('Waiting for messages.')
    while True:
        recebe = con.recv(4096)
        if not recebe:
            logging.debug('Socket closing connection\n\n')
            serv_socket.close()
            break
        if len(recebe) > 0:
            logging.debug (str('Received message: '+recebe.decode()))
            with open('data.txt', 'a') as data:
                data.write(str(recebe)+"\n")

