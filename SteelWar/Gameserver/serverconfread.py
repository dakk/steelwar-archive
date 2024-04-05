import shelve


class readserver:
	def __init__(self):
		self.game = 'Noname'
		self.prg = 'ServerReader'
		self.ver = '0.1'
		self.autor = 'Dak'
		self.file = 'server.conf'
		
	def main(self):
		print self.prg + self.ver
		print 'Creato da: ' + self.autor
		try:
			settingsfile = shelve.open(self.file, writeback=True)
			print 'Nome server: ' + settingsfile['name']
			print 'Porta: ' + settingsfile['port']
			print 'Mod: ' + settingsfile['mod']
			print 'Player massimi: ' + settingsfile['maxplayer']
			print 'Messaggio di entrata: ' + settingsfile['welcome']
			print 'Punteggio: ' + settingsfile['score']
			print 'Tempo: ' + settingsfile['time']
			print 'Password admin: ' + settingsfile['passadmin']
			settingsfile.close()
		except:		
			print 'Errore durante la lettura del database: il database potrebbe non esistere o contenere errori'
		self.did()
		
	def did(self):
		raw_input('Premere un tasto per uscire... ')

	
readserver = readserver()
readserver.main()