
from events import *
import preferences


DIRECTION_UP = 0
DIRECTION_DOWN = 1
DIRECTION_LEFT = 2
DIRECTION_RIGHT = 3

#------------------------------------------------------------------------------
class Game:
	"""..."""

	STATE_PREPARING = 0
	STATE_RUNNING = 1
	STATE_PAUSED = 2

	#----------------------------------------------------------------------
	def __init__(self, evManager):
		self.evManager = evManager
		self.evManager.RegisterListener( self )

		self.Reset()

	#----------------------------------------------------------------------
	def Reset( self ):
		self.state = Game.STATE_PREPARING
		
		self.players = [ ]
		self.maxPlayers = 3
		self.map = Map( self.evManager )

		cpuPlayer = ComputerPlayer(self.evManager)
		self.AddPlayer( cpuPlayer )

	#----------------------------------------------------------------------
	def Start(self):
		self.map.Build()
		self.state = Game.STATE_RUNNING
		ev = GameStartedEvent( self )
		self.evManager.Post( ev )

	#----------------------------------------------------------------------
	def AddPlayer(self, player):
		self.players.append( player )
		player.SetGame( self )
		ev = PlayerJoinEvent( player )
		self.evManager.Post( ev )


	#----------------------------------------------------------------------
 	def Notify(self, event):
		if isinstance( event, GameStartRequest ):
			if self.state == Game.STATE_PREPARING:
				self.Start()
			elif self.state == Game.STATE_RUNNING:
				self.Reset()
				self.Start()

		if isinstance( event, PlayerJoinRequest ):
			if len(self.players) < self.maxPlayers:
				player = Player( self.evManager )
				player.SetData( event.playerDict )
				for p in self.players:
					if p.name == player.name:
						#FAIL
						raise NotImplementedError, "Dup Player"
				self.AddPlayer( player )

		if isinstance( event, GUIChangeScreenRequest ):
			ev = GameSyncEvent( self )
			self.evManager.Post( ev )

#------------------------------------------------------------------------------
class Player:
	"""..."""
	def __init__(self, evManager ):
		self.evManager = evManager
		self.game = None
		self.name = ""
		self.evManager.RegisterListener( self )

		self.charactors = [ Customer(evManager) ]

		#self.placeableCharactorClasses = [ Charactor ]
		#self.startSector = None

	#----------------------------------------------------------------------
	def GetPlaceData( self ):
		charactor = self.charactors[0]
		map = self.game.map
		sector =  map.sectors[map.startSectorIndex]
		return [charactor, sector]

	#----------------------------------------------------------------------
	def GetMoveData( self ):
		return [self.charactors[0]]

	#----------------------------------------------------------------------
	def SetGame( self, game ):
		self.game = game

	#----------------------------------------------------------------------
	def SetData( self, playerDict ):
		self.name = playerDict['name']

	#----------------------------------------------------------------------
 	def Notify(self, event):
		pass
		#if isinstance( event, PlayerJoinEvent):
			#if event.player is self:

#------------------------------------------------------------------------------
class ComputerPlayer(Player):
	"""..."""
	def __init__(self, evManager ):
		self.evManager = evManager
		self.game = None
		self.name = "Computer"
		self.evManager.RegisterListener( self )

		self.charactors = [ Bartender(evManager) ]

	#----------------------------------------------------------------------
	def GetPlaceData( self ):
		charactor = self.charactors[0]
		map = self.game.map
		sector =  map.sectors[map.bartenderIndex]
		return [charactor, sector]


#------------------------------------------------------------------------------
class Charactor:
	"""..."""

	STATE_INACTIVE = 0
	STATE_ACTIVE = 1

	def __init__(self, evManager):
		self.evManager = evManager
		self.evManager.RegisterListener( self )

		self.sector = None
		self.state = Charactor.STATE_INACTIVE

		self.name = preferences.playerData['charactorName']

	#----------------------------------------------------------------------
 	def Move(self, direction):
		if self.state == Charactor.STATE_INACTIVE:
			return

		if self.sector.MovePossible( direction ):
			newSector = self.sector.neighbors[direction]
			self.sector = newSector
			ev = CharactorMoveEvent( self )
			self.evManager.Post( ev )

	#----------------------------------------------------------------------
 	def Place(self, sector):
		self.sector = sector
		self.state = Charactor.STATE_ACTIVE

		ev = CharactorPlaceEvent( self )
		self.evManager.Post( ev )

	#----------------------------------------------------------------------
 	def Notify(self, event):
		if isinstance( event, CharactorPlaceRequest ) \
		 and event.charactor is self:
			self.Place( event.sector )

		elif isinstance( event, CharactorMoveRequest ) \
		 and event.charactor is self:
			self.Move( event.direction )

#------------------------------------------------------------------------------
class Bartender(Charactor):
	"""..."""
	def __init__(self, evManager):
		self.evManager = evManager
		self.evManager.RegisterListener( self )

		self.sector = None
		self.state = Charactor.STATE_INACTIVE

		self.name = 'Bartender'

	#----------------------------------------------------------------------
	def AskForDrink( self, customer ):
		if customer.GetAge() > 18:
			ev = ServeDrinkEvent( customer )
			self.evManager.Post( ev )
		else:
			ev = DenyDrinkEvent( customer )
			self.evManager.Post( ev )

	#----------------------------------------------------------------------
 	def Notify(self, event):
		Charactor.Notify( self, event )

		if isinstance( event, CharactorDrinkOrderEvent ):
			self.AskForDrink( event.customer )
		if isinstance( event, MapBuiltEvent ):
			sect = event.map.sectors[event.map.bartenderIndex]
			self.Place( sect )

#------------------------------------------------------------------------------
class Customer(Charactor):
	"""..."""
	def __init__(self, evManager):
		Charactor.__init__(self, evManager)
		self.drinksReceived = 0

	#----------------------------------------------------------------------
 	def GetAge(self ):
		from random import Random
		rng = Random()
		return rng.randrange( 16,21 )

	#----------------------------------------------------------------------
 	def Notify(self, event):
		Charactor.Notify( self, event )

		if isinstance( event, ServeDrinkEvent ) \
		  and event.customer is self:
			self.drinksReceived += 1


#------------------------------------------------------------------------------
class Map:
	"""..."""

	STATE_PREPARING = 0
	STATE_BUILT = 1


	#----------------------------------------------------------------------
	def __init__(self, evManager):
		self.evManager = evManager
		self.evManager.RegisterListener( self )

		self.state = Map.STATE_PREPARING

		self.sectors = range(3)
		self.startSectorIndex = 0
		self.bartenderIndex = 2

	#----------------------------------------------------------------------
	def Build(self):
		for i in range(3):
			self.sectors[i] = Sector( self.evManager )

		self.state = Map.STATE_BUILT

		ev = MapBuiltEvent( self )
		self.evManager.Post( ev )

	#----------------------------------------------------------------------
 	def Notify(self, event):
		if isinstance( event, CharactorPlaceEvent ):
			sect = event.charactor.sector
			#self.startSectorIndex = self.sectors.index(sect)+1

#------------------------------------------------------------------------------
class Sector:
	"""..."""
	def __init__(self, evManager):
		self.evManager = evManager
		#self.evManager.RegisterListener( self )

		self.neighbors = range(4)

		self.neighbors[DIRECTION_UP] = None
		self.neighbors[DIRECTION_DOWN] = None
		self.neighbors[DIRECTION_LEFT] = None
		self.neighbors[DIRECTION_RIGHT] = None

	#----------------------------------------------------------------------
	def MovePossible(self, direction):
		if self.neighbors[direction]:
			return 1


if __name__ == "__main__":
	print "wasn't expecting that"
