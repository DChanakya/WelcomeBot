
import sys
import time
#import pygame as pg
#import nltk
#import re
import socket
#import sys

buf=''
HOST = '192.168.43.136'  # this is your localhost
PORT = 8888
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('socket created')

# Bind socket to Host and Port
try:
    s.bind((HOST, PORT))
except socket.error as err:
    print('Bind Failed, Error Code: '+'Message: address alredy in use:')
    sys.exit()
s.listen(0)
print('Socket is now listening')

while 1:
   
    conn, addr=s.accept()
    
    print('Connect with ' + addr[0] + ':' + str(addr[1]))
    buf = conn.recv(64)
    buf = str(buf)
    print(buf)
    # stro=""
    # while(1):
    #     print(buf)
    #     conn, addr=s.accept()
    #     buf1 = conn.recv(64)
    #     stro = str(buf1)
    #     if("stop" in stro):
    #         break;
    f=open("buf.txt","w");
    f.write(buf)
    f.close()   
   
s.close()
