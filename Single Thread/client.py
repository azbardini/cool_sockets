import socket 
import logging
import signal

def sigint_handler(signum, frame):
    logging.debug('Socket closing connection.')
    client_socket.close()
    exit() 
signal.signal(signal.SIGINT, sigint_handler)

logging.basicConfig(level=logging.DEBUG)

ip = '143.54.12.243' 
port = 20101
addr = ((ip,port)) 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect(addr) 

logging.debug('Connection started to '+str(ip)+':'+str(port)) 
logging.debug('Waiting for connection.')

while True:
    mensagem = raw_input('Type a message: ') 
    client_socket.send(mensagem) 
logging.debug('Message sent!') 
client_socket.close()
