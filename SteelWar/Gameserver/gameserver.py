import shelve, socket, os, thread, time, sys


class gameserver:
	def __init__(self):
		self.game = 'Noname'
		self.prg = 'GameServer'
		self.ver = '0.1'
		self.autor = 'Dak'
		self.file = 'server.conf'
		self.logfile = 'server.log'
		self.host = ''
		self.demon = False
		self.os = sys.platform[0]
		
		self.currentmap = 'None'
		self.currentplayer = 0
		self.currentpoint1 = 0
		self.currentpoint2 = 0
		self.currentfps = 60
		self.currentcpu = 10
		self.currentusage = 5
		
		self.usr = {}
		
		
	def main(self):
		self.cancfile()
		self.arg()
		self.getconf()
		if self.demon == True: self.demonize()
		self.servercreate()
		if self.demon == False : thread.start_new(self.screen, ())
		thread.start_new(self.serverlisten, ())
		self.server_main()

			
	def cancfile(self):
		logfile = open(self.logfile,'w')
		logfile.writelines('\n')
		logfile.close()
			
		
	def arg(self):
		try:
			if sys.argv[1]=='demonize': self.demon = True
		except: pass
		
	def error(self, n):
		e1 = 'Errore: Impossibile connettersi alla porta desiderata'
		if n == 1 : 
			print e1
			self.logga(e1)
		self.con = False
		
			
		
	def screen(self):
		while self.con:
			self.clear()
			print self.prg + ' ' + self.ver 
			print self.game + ' (powered by Dak91, dakdak@hotmail.it)'
			print 'Name: "'+self.name+'"\t\t\tFPS: '+str(self.currentfps)
			print 'Ip: 127.0.0.1  Port: '+self.port+'\tMap: '+self.currentmap
			print 'Mod: '+self.mod+'\t\t\tTime: '+time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
			print 'Player: ' + str(len(self.usr)) + '/' + self.maxplayer + '\t\t\tLogfile: '+self.logfile
			print 'Point team1: ' + str(self.currentpoint1) + '/' + self.score + '\t\tPoint team2: ' + str(self.currentpoint2) + '/' + self.score
			print 'Cpu: '+str(self.currentcpu)+'%\t\t\tRam: '+str(self.currentusage)+'b'
			print '\n--------------------------------------------------------------------------------'
			print self.usr
			print '--------------------------------------------------------------------------------'
			#command = raw_input('> ')
			
			time.sleep(1)
		exit()
			
	def getconf(self):
		try:
			settingsfile = shelve.open(self.file, writeback=True)
			self.name = settingsfile['name']
			self.port = settingsfile['port']
			self.mod = settingsfile['mod']
			self.maxplayer = settingsfile['maxplayer']
			self.welcome = settingsfile['welcome']
			self.score = settingsfile['score']
			self.time = settingsfile['time']
			self.passadmin = settingsfile['passadmin']
			settingsfile.close()
		except:
			raw_input('Errore durante la lettura del database: il database potrebbe non esistere o contenere errori...')
			exit()
			
	def logga(self, string):
		logfile = open(self.logfile,'a')
		log = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()) + ' ' + string + '\n'
		logfile.writelines(log)
		logfile.close()
		
	def demonize(self):
		if os.fork():
			os._exit(0)
		os.setsid()
		if os.fork():
			os._exit(0)
		os.umask(077)
		null=os.open('/dev/null', os.O_RDWR)
		for i in range(3):
			try:
				os.dup2(null, i)
			except OSError, e:
				if e.errno != errno.EBADF:
					raise
		os.close(null)
		
	def clear(self):
		if self.os == 'l': os.system('clear')
		if self.os == 'w': os.system('cls')
		else: pass
		
	def servercreate(self):
		self.logga('Avvio server '+self.prg+' '+self.ver)
		self.gameserver_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.con = True
		try: 		
			self.gameserver_sock.bind((self.host, int(self.port)))
			self.logga('Server creato con successo alla porta: ' + self.port)
			self.gameserver_sock.listen(int(self.maxplayer))
			self.logga('Server in attesa di connessioni alla porta: ' + self.port)
			
		except:		self.error(1)
		
		
	
	def serverlisten(self):
		while self.con:
			conn, adr = self.gameserver_sock.accept()
			thread.start_new(self.clientcon, (conn,adr))
	
	def clientcon(self, conn, adr):
		self.logga('Nuovo utente entrato: '+str(adr))
		
		conn.send('\n+REQUEST_VERSION+\n')
		ver=conn.recv(1024)
		if ver[:-2] == self.ver: 
			conn.send('+VERSION_ACCEPT+\n')
			tmp = True
			
		else: 
			conn.send('+VERSION_REJECT+\n')
			conn.send('+DISCONNECT+\n')
			tmp = False
		
		
		if tmp == True:
			conn.send('\n+REQUEST_NICK+\n')
			nick = conn.recv(1024)
			nick = nick[:-2]
			if nick in self.usr: 
				conn.send('+NICK_REJECT+\n')
				conn.send('+DISCONNECT+\n')
				tmp = False
			else: 
				conn.send('+NICK_ACCEPT+\n')
				self.usr[nick] = conn
				self.logga('Player '+str(adr)+' e\' conosciuto come '+nick)
				self.currentplayer +=1
				
		if tmp == True:
			conn.send('\n+REQUEST_READY+\n')
			res = conn.recv(1024)
			if res[:-2] == '+I_M_READY+': pass
			else: tmp = False
			
		if tmp == True:
			
				
				

		
			
		
	def server_main(self):
		while self.con:
			a=0
	
gameserver = gameserver()
gameserver.main()