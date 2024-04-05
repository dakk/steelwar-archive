import shelve


class createserver:
	def __init__(self):
		self.game = 'Noname'
		self.prg = 'ServerEditor'
		self.ver = '0.1'
		self.autor = 'Dak'
		self.file = 'server.conf'
		
	def main(self):
		print self.prg + self.ver
		print 'Creato da: ' + self.autor
		self.name = raw_input('Nome server: ')
		self.port = raw_input('Porta server: ')
		self.mod = raw_input('Mod: ')
		self.maxplayer = raw_input('Player massimi: ')
		self.welcome = raw_input('Messaggo di benvenuto: ')
		self.score = raw_input('Punteggio: ')
		self.time = raw_input('Tempo (minuti): ')
		self.passadmin = raw_input('Password admin: ')
		self.reg()
		self.did()
		
	def reg(self):
		try:
			settingsfile = shelve.open(self.file, writeback=True)
			settingsfile['name'] = self.name
			settingsfile['port'] = self.port
			settingsfile['mod'] = self.mod
			settingsfile['maxplayer'] = self.maxplayer
			settingsfile['welcome'] = self.welcome
			settingsfile['score'] = self.score
			settingsfile['time'] = self.time
			settingsfile['passadmin'] = self.passadmin
			settingsfile.close()
			print 'Server creato con successo'
		except:
			print 'Errore durante la creazione del file di configurazione'
			
	def did(self):
		raw_input('Premere un tasto per uscire... ')

	
createserver = createserver()
createserver.main()