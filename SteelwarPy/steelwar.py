# 
# Steelwar
#
# Author: Dak and Otacon from #NoCoPy team
# Description: FPS game about the second worldwar
# Language: python
# Game engine: Panda3d
#

from direct.showbase.DirectObject import DirectObject
from direct.task import Task

from engine.player import * 
from engine.map import *
from engine.gui import *
from engine.device import *

import sys

class Steelwar(DirectObject):						# Classe del gioco
	def __init__(self):								# Funzione di inizializzazione
		self.Device = Device()						# Crea l'oggetto device
		self.Map = Map(10)							# Crea l'oggetto mappa highdetail
		self.Player = Player()						# Crea l'oggetto player
		self.Gui = Gui()								# Crea l'oggetto ui
		self.Chat = Chat(15)							# Chat multilinea della ui

	def Main(self,map):								# Funzione principale del gioco
		self.Device.InitDevice(1,1,1)				# Inizializza il device con sfondo bianco
		self.Gui.InitGui()							# Inizializza la user interface
		if self.Map.DrawMap(map) != 0:			# Disegna la mappa e se c'e' qlk error, chiude steelwar
			print "Map error!"						
			sys.exit(0)
		else:
			
			self.Chat.AddLine("Map "+map+" loaded.")

		self.Player.InitPlayer(self.Map)			# Inizializza l'oggetto player
		self.Gui.Player = self.Player
		self.SetEvents()								# Avvia il gestore degli eventi

	
	def SetEvents(self):								# Funzione per gli eventi di input
		self.accept('escape', sys.exit, [0])			
		self.accept('d', self.Player.Event, ['d'])
		self.accept('d-up', self.Player.Event, ['du'])	
		self.accept('a', self.Player.Event, ['a'])	
		self.accept('a-up', self.Player.Event, ['au'])
		self.accept('w', self.Player.Event, ['w'])	
		self.accept('w-up', self.Player.Event, ['wu'])
		self.accept('s', self.Player.Event, ['s'])
		self.accept('s-up', self.Player.Event, ['su'])	

		self.accept('1', self.Player.Event, ['1'])
		self.accept('2', self.Player.Event, ['2'])
		self.accept('3', self.Player.Event, ['3'])
		self.accept('4', self.Player.Event, ['4'])
		self.accept('5', self.Player.Event, ['5'])
		
		#self.accept('mouse1', self.Player.PrintPos, ['m1'])
		
		self.accept("mouse1",self.Player.Event,['m1'])
		self.accept('mouse1-up', self.Player.Event, ['m1u'])
		self.accept('f1', self.Device.ScreenShoot, [])

		taskMgr.add(self.Player.GetFPSTask, 'FPSTask')
		taskMgr.add(self.Player.BulletsTask, 'BulletsTask')	
		taskMgr.add(self.Player.MouseTask, 'MouseTask')	
		taskMgr.add(self.Player.MoveTask, 'MoveTask')	
		taskMgr.add(self.Gui.UpdateTask, 'UpdateTask')




Steelwar = Steelwar()								# Inizializza il gioco
Steelwar.Main("mods/WorldWar2/DesertTry/")	# Avvia la funzione principale
run()														# Esegui il loop
