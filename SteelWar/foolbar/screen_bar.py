from events import *
from utils import *
from model import *

import pygame
from pygame.locals import *


#------------------------------------------------------------------------------
class MainBarScreenController:
	"""..."""

	MODE_SELECT = 0
	MODE_ACTION = 1

	def __init__(self, evManager):
		self.evManager = evManager
		self.evManager.RegisterListener( self )

		self.rectOfInterest = pygame.Rect( (0,0,440,380) )

		self.mode = MainBarScreenController.MODE_SELECT

	#----------------------------------------------------------------------
	def WantsEvent( self, event ):
		if event.type == MOUSEBUTTONUP \
		  or event.type == MOUSEMOTION \
		  and self.rectOfInterest.collidepoint( event.pos ):
			return 1

		return 0

	#----------------------------------------------------------------------
	def HandlePyGameEvent(self, event):
		ev = None

		if event.type == MOUSEBUTTONUP:
			b = event.button
			if b == 1:
				selMode = MainBarScreenController.MODE_SELECT
				actMode = MainBarScreenController.MODE_ACTION
				if self.mode == selMode:
					ev = BarScreenSelectEvent(event.pos)
				elif self.mode == actMode:
					ev = BarScreenActionEvent(event.pos)

		if ev:
			self.evManager.Post( ev )

	#----------------------------------------------------------------------
	def Notify(self, event):
		pass


#------------------------------------------------------------------------------
class MainBarScreen:
	"""..."""
	STATE_PREPARING = 0
	STATE_ACTIVE = 1

	def __init__(self, evManager, renderGroup, rect ):

		self.evManager = evManager
		self.evManager.RegisterListener( self )

		self.renderGroup = renderGroup
		self.spriteGroup = pygame.sprite.Group()

		self.rect = rect
		self.xyOffset = (self.rect.x, self.rect.y)

		self.state = MainBarScreen.STATE_PREPARING

	#----------------------------------------------------------------------
 	def GetBackgroundBlit(self):
		bgImg = load_png( 'main_bar_background.png')
		return [ bgImg, self.rect ]
	#----------------------------------------------------------------------
 	def kill(self ):
		for sprite in self.spriteGroup.sprites():
			sprite.kill()
		self.spriteGroup.empty()


	#----------------------------------------------------------------------
 	def ShowCharactor(self, charactor):
		if self.state != MainBarScreen.STATE_ACTIVE:
			return

		sector = charactor.sector
		if not sector:
			print "Charactor is not in a sector.  cannot show"
			return

		charactorSprite = self.GetCharactorSprite( charactor )
		sectorSprite = self.GetSectorSprite( sector )
		charactorSprite.rect.center = sectorSprite.rect.center

	#----------------------------------------------------------------------
	def GetCharactorSprite(self, charactor):
		for s in self.spriteGroup.sprites():
			if isinstance(s, CharactorSprite) \
			  and s.charactor is charactor:
				return s

		sprite = CharactorSprite(self.evManager, charactor)
		sprite.rect.move_ip( self.xyOffset )
		self.spriteGroup.add( sprite )
		self.renderGroup.add( sprite )
		return sprite

	#----------------------------------------------------------------------
	def GetSectorSprite(self, sector):
		for s in self.spriteGroup.sprites():
			if isinstance(s, SectorSprite) and s.sector == sector:
				return s
		raise Exception( "Could not get sector sprite for", sector )

	#----------------------------------------------------------------------
 	def ShowMap(self, map):

		if self.state != MainBarScreen.STATE_PREPARING:
			raise Exception( 'barscreen: probably an error' )

		rects = [ pygame.Rect( (50,200, 28,28 ) ),
		          pygame.Rect( (200,200,28,28 ) ),
		          pygame.Rect( (320,62,28,28 ) ),
		        ]

		i = 0
		for sector in map.sectors:
			sprite = SectorSprite( sector )
			#sprite.rect.move_ip( self.xyOffset )
			self.spriteGroup.add( sprite )
			self.renderGroup.add( sprite )
			sprite.rect = rects[i]
			sprite = None
			i += 1


		self.state = MainBarScreen.STATE_ACTIVE


	#----------------------------------------------------------------------
 	def Notify(self, event):
		if isinstance( event, CharactorPlaceEvent ):
			self.ShowCharactor( event.charactor )

		elif isinstance( event, GameSyncEvent ):
			game = event.game
			self.ShowMap( game.map )
			for player in game.players:
				for charactor in player.charactors:
					self.ShowCharactor( charactor )


#------------------------------------------------------------------------------
class SectorSprite(pygame.sprite.Sprite):
	def __init__(self, sector):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface( (28,28) )
		self.image.fill( (0,255,0,128) )
		self.rect = self.image.get_rect()

		self.sector = sector


#------------------------------------------------------------------------------
class CharactorSprite(pygame.sprite.Sprite):
	def __init__(self, evManager, charactor ):
		pygame.sprite.Sprite.__init__(self)

		self.zAxis = 1

		self.evManager = evManager
		self.evManager.RegisterListener( self )

		self.charactor = charactor

		className = charactor.__class__.__name__
		try:
			self.image = load_png( 'charactor'+className+'.png' )
		except:
			self.image = load_png( 'charactor.png' )

		self.rect  = self.image.get_rect()

		self.origImage = self.image
		self.selectedImg = pygame.Surface( (self.rect.width, 
		                                    self.rect.height),
		                                   flags = SRCALPHA )
		highlight = pygame.Surface( (self.rect.width, 
		                             self.rect.height),
		                            flags = SRCALPHA )
		highlight.fill( (0,0,255,128) )
		self.selectedImg.blit( highlight, (0,0) )
		self.selectedImg.blit( self.image, (0,0) )

		self.selected = 0

	#----------------------------------------------------------------------
	def SetSelected(self, val):
		self.selected = val
		if val == 0:
			self.image = self.origImage
		else:
			self.image = self.selectedImg

	#----------------------------------------------------------------------
	def update(self):
		#self.rect  = self.image.get_rect()
		pass

	#----------------------------------------------------------------------
	def Connect(self, eventDict):
		for key,event in eventDict.iteritems():
			try:
				self.__setattr__( key, event )
			except AttributeError:
				print "Couldn't connect the ", key
				pass

	#----------------------------------------------------------------------
	def Select(self):
		self.SetSelected(1)
		ev = GUICharactorSelectedEvent( self.charactor )
		self.evManager.Post( ev )

	#----------------------------------------------------------------------
 	def Notify(self, event):
		if isinstance( event, BarScreenSelectEvent ) \
		  and self.rect.collidepoint( event.pos ):
			self.Select()

		elif isinstance( event, BarScreenSelectEvent ) \
		  and self.selected:
			self.SetSelected( 0 )
			ev = GUICharactorUnSelectedEvent(self.charactor)
			self.evManager.Post( ev )




if __name__ == "__main__":
	print "that was unexpected"
