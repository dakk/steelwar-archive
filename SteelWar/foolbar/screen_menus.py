import pygame
from pygame.locals import *
import string

from gui import *
from events import *
from utils import load_png
import preferences


#------------------------------------------------------------------------------
class MenuGUIView(GUIView):
	"""..."""
	def __init__( self, evManager, renderGroup, rect ):
		GUIView.__init__( self, evManager, renderGroup, rect)
		
		quitEvent = QuitEvent()
		optEvent = GUIChangeScreenRequest( 'options' )
		playEvent = GameStartRequest()

		b1= ButtonSprite( evManager, "Quit", container=self, 
		                  onClickEvent=quitEvent )
		b2= ButtonSprite( evManager, "Options", container=self,
		                  onClickEvent=optEvent )
		b3= ButtonSprite( evManager, "Start New Game", container=self,
		                  onClickEvent=playEvent )
		self.widgets = [ b1,b2,b3 ]

		self.renderGroup.add( self.widgets )

		self.ArrangeWidgets()

	#----------------------------------------------------------------------
 	def GetBackgroundBlit(self):
		bgImg = pygame.Surface( (self.rect.width, self.rect.height) )
		bgImg.fill( (0,0,50) )
		return [bgImg, self.rect]

	#----------------------------------------------------------------------
 	def Notify(self, event):
		GUIView.Notify( self, event )

		if isinstance( event, GameStartedEvent):
			ev = GUIChangeScreenRequest( 'main' )
			self.evManager.Post( ev )

#------------------------------------------------------------------------------
class OptionsGUIView(GUIView):
	"""..."""
	def __init__( self, evManager, renderGroup, rect ):
		GUIView.__init__( self, evManager, renderGroup, rect)

		self.xyOffset = ( self.rect.x, self.rect.y )

		menuEvent = GUIChangeScreenRequest( 'menu' )
		b1= ButtonSprite( evManager, "Menu", container=self,
		                  onClickEvent=menuEvent)
		pn= PlayerNameSprite( evManager, container=self)
		cn= CharactorNameSprite(evManager, container=self )

		self.widgets = [ b1, pn, cn ]
		self.renderGroup.add( self.widgets )

		self.ArrangeWidgets()

	#----------------------------------------------------------------------
 	def GetBackgroundBlit(self):
		bgImg = pygame.Surface( (self.rect.width, self.rect.height) )
		bgImg.fill( (50,0,0) )
		return [bgImg, self.rect]


			
#------------------------------------------------------------------------------
class PlayerNameSprite(TextEntrySprite):
	def __init__(self, evManager, container=None):
		TextEntrySprite.__init__( self, evManager, 
		                          "Player Name", container=container )
		self.widgets[1] = PlayerNameTextBoxSprite( evManager, 
		                                           200, 
		                                           container=container )

#------------------------------------------------------------------------------
class PlayerNameTextBoxSprite(TextBoxSprite):
	def __init__(self,evManager,width,container=None):
		TextBoxSprite.__init__(self,evManager,width,container=container)
		TextBoxSprite.SetText(self,preferences.playerData['name'])
	#----------------------------------------------------------------------
	def SetText(self, newText):
		self.text = newText
		preferences.playerData['name'] = self.text
		self.dirty = 1

#------------------------------------------------------------------------------
class CharactorNameSprite(TextEntrySprite):
	def __init__(self, evManager, container=None ):
		TextEntrySprite.__init__( self, evManager, 
		                          "Charactor Name", container=container)
		self.widgets[1] = CharactorNameTextBoxSprite( evManager, 
		                                           200, 
		                                           container=container )

#------------------------------------------------------------------------------
class CharactorNameTextBoxSprite(TextBoxSprite):
	def __init__(self,evManager,width, container=None):
		TextBoxSprite.__init__(self,evManager,width,container=container)
		TextBoxSprite.SetText(self,preferences.playerData['charactorName'])

	#----------------------------------------------------------------------
	def SetText(self, newText):
		self.text = newText
		preferences.playerData['charactorName'] = self.text
		self.dirty = 1



if __name__ == "__main__":
	print "that was unexpected"
