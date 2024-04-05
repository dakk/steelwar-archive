from thread import *
import socket, thread

def clientcon(conn, adr):
		print "hola";
		ver=conn.recv(1024)
		print ver

gameserver_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gameserver_sock.bind(("127.0.0.1", 5115))
gameserver_sock.listen(10)

while 1:
	conn, adr = gameserver_sock.accept()
	thread.start_new(clientcon, (conn,adr))

