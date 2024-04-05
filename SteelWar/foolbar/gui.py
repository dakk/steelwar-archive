import pygame
from pygame.locals import *
import string

from gui_widgets import *
from events import *
from utils import load_png
import preferences

#------------------------------------------------------------------------------
class GUIController:
	"""..."""
	def __init__(self, evManager):
		self.evManager = evManager
		self.evManager.RegisterListener( self )


	#----------------------------------------------------------------------
	def HandlePyGameEvent(self, event):
		"""is given a pygame.event and is responsible for generating
		an event defined in the local events module, or doing nothing"""
		pass

	#----------------------------------------------------------------------
	def Notify(self, event):
		pass


#------------------------------------------------------------------------------
class SimpleGUIController(GUIController):
	"""..."""
	#----------------------------------------------------------------------
	def WantsEvent( self, event ):
		if event.type == KEYDOWN \
		  or event.type == MOUSEBUTTONUP \
		  or event.type == MOUSEMOTION:
			return 1

		return 0

	#----------------------------------------------------------------------
	def HandlePyGameEvent(self, event):
		ev = None

		if event.type == KEYDOWN \
		     and event.key == K_ESCAPE:
			ev = QuitEvent()

		elif event.type == KEYDOWN \
		     and event.key == K_UP:
			ev = GUIFocusPrevWidgetEvent()

		elif event.type == KEYDOWN \
		     and event.key == K_DOWN:
			ev = GUIFocusNextWidgetEvent()

		elif event.type == KEYDOWN \
		     and (event.key == K_RETURN \
		     or event.key == K_SPACE):
			ev = GUIPressEvent()

		elif event.type == KEYDOWN :
			character = str(event.unicode)
			if character and character in string.printable:
				ev = GUIKeyEvent(character)
			elif event.key == K_BACKSPACE:
				ev = GUIControlKeyEvent( event.key )


		elif event.type == MOUSEBUTTONUP:
			b = event.button
			if b == 1:
				ev = GUIClickEvent(event.pos)

		elif event.type == MOUSEMOTION:
			ev = GUIMouseMoveEvent(event.pos)


		if ev:
			self.evManager.Post( ev )


#------------------------------------------------------------------------------
class BlockingDialogController(GUIController):
	"""..."""
	def __init__(self, evManager ):
		self.evManager = evManager
		self.evManager.RegisterListener( self )


	#----------------------------------------------------------------------
	def WantsEvent( self, event ):
		return 1

	#----------------------------------------------------------------------
	def HandlePyGameEvent(self, event):
		ev = None


		if event.type == KEYDOWN \
		     and (event.key == K_RETURN \
		     or event.key == K_SPACE):
			ev = GUIPressEvent()


		elif event.type == MOUSEMOTION:
			ev = GUIMouseMoveEvent(event.pos)

		elif event.type == MOUSEBUTTONUP:
			b = event.button
			if b == 1:
				ev = GUIClickEvent(event.pos)

		if ev:
			self.evManager.Post( ev )


#------------------------------------------------------------------------------
class GUIView(WidgetContainer):
	"""..."""
	def __init__( self, evManager, renderGroup, rect):
		WidgetContainer.__init__( self, evManager, rect )

		self.renderGroup = renderGroup


#------------------------------------------------------------------------------
class BlockingDialogView(GUIView):
	"""..."""
	clipRect = pygame.Rect( (20,20,400,400) )

	#----------------------------------------------------------------------
	def __init__(self, evManager, renderGroup, rect):
		GUIView.__init__( self, evManager, renderGroup, rect)

		self.__msg = "Error"
		bgSprite = pygame.sprite.Sprite()
		bgSprite.image = load_png( 'dialog_background.png' )
		#bgSprite.rect = bgSprite.image.get_rect()
		bgSprite.rect = self.rect

		closeEvent = GUIDialogRemoveRequest( 'msgDialog' )
		closeButton = ButtonSprite( evManager, "Close", 
		                            container=self, 
		                            onClickEvent=closeEvent )
		self.background = bgSprite
		self.widgets = [ closeButton,
		            LabelSprite(evManager, self.__msg, container=self ),
		          ]


		#because this is a Dialog, it should be shown on the topmost
		#layer of the View.
		#the renderGroup here is expected to be a LayeredSpriteGroup
		self.renderGroup.add_top( self.background )
		for wid in self.widgets:
			self.renderGroup.add_top( wid )

		self.ArrangeWidgets()

	#----------------------------------------------------------------------
 	def SetMsg(self, msg):
		self.__msg = msg
		self.widgets[1].SetText(self.__msg)

	#----------------------------------------------------------------------
 	def ArrangeWidgets(self ):
		xyOffset = ( self.rect.x, self.rect.y )
		self.widgets[0].rect.topleft= vectorSum( xyOffset, (220,100) ) 
		self.widgets[1].rect.topleft= vectorSum( xyOffset, (20,20) ) 

	#----------------------------------------------------------------------
 	def kill(self ):
		GUIView.kill( self )
		self.background.kill()
		del self.background



if __name__ == "__main__":
	print "that was unexpected"
