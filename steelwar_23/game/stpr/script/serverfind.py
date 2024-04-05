import socket
port = 1945
server = open('server.lst','r')
host = server.readlines()
linea=1
server = { }
servern = 0
while s:
	try: 
	 s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
	 s.connect((host, port))
	 host[linea+1]
	 
	 if linea=eof:
	  s=False
	 server[servern] = host

	 servern = severn + 1
	 s.close()
	 
 	except: 
	 linea = linea+1
 	 s.close()	
	 if linea=eof:
	 s=False 
	 continue
	 
servern = len(server)
1 = server[n]