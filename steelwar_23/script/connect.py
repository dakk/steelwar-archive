import os
import socket
import time

fol = open('./../etc/tmpdata', 'r')
server = fol.readline()
port = fol.readline()
nick = fol.readline()
passs = fol.readline()

print server,port,nick,passs

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server, int(port)))

sock.send('0.1')

rec = sock.recv(1024)
rec = rec[:-2]
mapp = rec[1:]

sock.send(nick)
sock.send(passs)

sock.send('+JA+')
