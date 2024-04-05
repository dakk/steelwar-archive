#! /usr/bin/python

from events import *
from utils import *
from gui import *
from model import *
from layeredgroup import LayeredSpriteGroup

from screen_bar import MainBarScreenController, MainBarScreen
from screen_main_panel import MainGUIController, MainGUIView
from screen_menus import MenuGUIView, OptionsGUIView

import pygame
from pygame.locals import *
from weakref import WeakKeyDictionary

#------------------------------------------------------------------------------
class EventManager:
	"""this object is responsible for coordinating most communication
	between the Model, View, and Controller."""
	def __init__(self ):
		self.listeners = WeakKeyDictionary()
		self.eventQueue= []

	#----------------------------------------------------------------------
	def Debug( self, ev):
		return
		if not isinstance( ev, GUIMouseMoveEvent ):
			print "   Message: " + ev.name

	#----------------------------------------------------------------------
	def RegisterListener( self, listener ):
		#if not hasattr( listener, "Notify" ): raise blah blah...
		self.listeners[ listener ] = 1

	#----------------------------------------------------------------------
	def UnregisterListener( self, listener ):
		if listener in self.listeners.keys():
			del self.listeners[ listener ]
		
	#----------------------------------------------------------------------
	def Post( self, event ):
		from copy import copy
		if not isinstance(event, TickEvent): 
			self.eventQueue.append( event )
		else:
			events = copy( self.eventQueue )
			self.eventQueue = []
			while len(events) > 0:
				ev = events.pop(0)
				self.Debug( ev )

				for listener in self.listeners.keys():
					listener.Notify( ev )

			#at the end, notify listeners of the Tick event
			for listener in self.listeners.keys():
				listener.Notify( event )


#------------------------------------------------------------------------------
class CPUSpinnerController:
	"""..."""
	def __init__(self, evManager):
		self.evManager = evManager
		self.evManager.RegisterListener( self )

		self.keepGoing = 1

	#----------------------------------------------------------------------
	def Run(self):
		if not self.keepGoing:
			raise Exception('dead spinner')
		while self.keepGoing:
			event = TickEvent()
			self.evManager.Post( event )

	#----------------------------------------------------------------------
 	def Notify(self, event):
		if isinstance( event, QuitEvent ):
			#this will stop the while loop from running
			self.keepGoing = 0


#------------------------------------------------------------------------------
class PygameMasterController:
	"""..."""
	def __init__(self, evManager):
		self.evManager = evManager
		self.evManager.RegisterListener( self )

		#subcontrollers is an ordered list, the first controller in the
		# list is the first to be offered an event
		self.subcontrollers = []

		self.guiClasses = { 'menu': [SimpleGUIController],
		                    'options': [SimpleGUIController],
		                    'main': [MainGUIController, MainBarScreenController],
		                  }
		self.dialogClasses = { 'msgDialog': BlockingDialogController,
		                     }
		self.SwitchController( 'menu' )

	#----------------------------------------------------------------------
	def SwitchController(self, key):

		if not self.guiClasses.has_key( key ):
			raise NotImplementedError

		self.subcontrollers = []

		for contClass in self.guiClasses[key]:
			newController = contClass(self.evManager)
			self.subcontrollers.append( newController )

	#----------------------------------------------------------------------
	def DialogAdd(self, key):
		#print "Adding Dialog Controllers", key

		if not self.dialogClasses.has_key( key ):
			raise NotImplementedError

		contClass = self.dialogClasses[key]
		newController = contClass(self.evManager)

		self.subcontrollers.insert(0, newController)

	#----------------------------------------------------------------------
	def DialogRemove(self, key):

		if not self.dialogClasses.has_key( key ):
			raise NotImplementedError

		contClass = self.dialogClasses[key]

		if self.subcontrollers[0].__class__ is not contClass:
			print self.subcontrollers
			raise Exception('removing dialog controller not there')

		self.subcontrollers.pop(0)

		#TODO: I've commented this out for now, but leave here as its
		#      an example of what might be done for multiple dialogs
		#i = 0
		#length = len( self.subcontrollers )
		#while i < length:
			#cont = self.subcontrollers[0]
			#if cont.__class__ in self.guiClasses[key]:
				#self.subcontrollers.remove( cont )
			#i += 1


	#----------------------------------------------------------------------
	def Notify(self, incomingEvent):

		if isinstance( incomingEvent, TickEvent ):
			#Handle Input Events
			for event in pygame.event.get():
				ev = None
				if event.type == QUIT:
					ev = QuitEvent()
					self.evManager.Post( ev )

				elif event.type == KEYDOWN \
				  or event.type == MOUSEBUTTONUP \
				  or event.type == MOUSEMOTION:
					for cont in self.subcontrollers:
						if cont.WantsEvent( event ):
							cont.HandlePyGameEvent(event)
							break

		elif isinstance( incomingEvent, GUIChangeScreenRequest ):
			self.SwitchController( incomingEvent.key )

		elif isinstance( incomingEvent, GUIDialogAddRequest ):
			self.DialogAdd( incomingEvent.key )

		elif isinstance( incomingEvent, GUIDialogRemoveRequest ):
			self.DialogRemove( incomingEvent.key )


#------------------------------------------------------------------------------
class PygameMasterView(EventManager):
	"""..."""
	def __init__(self, evManager):
		EventManager.__init__(self)
		self.normalListeners = self.listeners
		self.dialogListeners = WeakKeyDictionary()

		self.evManager = evManager
		self.evManager.RegisterListener( self )

		pygame.init()
		self.window = pygame.display.set_mode( (440,480) )
		pygame.display.set_caption( 'Fool The Bar' )
		self.background = pygame.Surface( self.window.get_size() )
		self.background.fill( (0,0,0) )

		self.window.blit( self.background, (0,0) )
		pygame.display.flip()

		self.dialog = None

		self.subviews = []
		self.spriteGroup = LayeredSpriteGroup()

		self.guiClasses = { 'menu': [MenuGUIView],
		                    'options': [OptionsGUIView],
		                    'main': [MainBarScreen, MainGUIView],
		                  }
		self.dialogClasses = { 'msgDialog': BlockingDialogView,
		                     }

		#the subviews that make up the current screen.  In order from
		# bottom to top
		#self.subviews = []
		self.SwitchView( 'menu' )


	#----------------------------------------------------------------------
 	def Debug(self, ev):
		return
		if not isinstance( ev, GUIMouseMoveEvent ):
			print '     Message: ', ev.name

	#----------------------------------------------------------------------
 	def Post(self, event):
		self.evManager.Post( event )

	#----------------------------------------------------------------------
 	def SwitchView(self, key):

		if self.dialog:
			raise Exception('cannot switch view while dialog up')

		if not self.guiClasses.has_key( key ):
			raise NotImplementedError('master view doesnt have key')

		for view in self.subviews:
			view.kill()
		self.subviews = []

		self.spriteGroup.empty()

		rect = pygame.Rect( (0,0), self.window.get_size() )

		#construct the new master View
		for viewClass in self.guiClasses[key]:
			if hasattr( viewClass, 'clipRect' ):
				rect = viewClass.clipRect
			view = viewClass(self, self.spriteGroup, rect)
			bgBlit = view.GetBackgroundBlit()
			self.background.blit( bgBlit[0], bgBlit[1] )
			self.subviews.append( view )

		#initial blit & flip of the newly constructed background
		self.window.blit( self.background, (0,0) )
		pygame.display.flip()

	#----------------------------------------------------------------------
	def DialogAdd(self, key, msg="Error"):

		if self.dialog:
			raise Exception('only one dialog at a time')

		if not self.dialogClasses.has_key( key ):
			raise NotImplementedError('master view doesnt have key')

		#the normal listeners will not be sent any events.  instead,
		#we will just send events to the listeners associated with the
		#new dialog.
		self.listeners = self.dialogListeners


		rect = pygame.Rect( (0,0), self.window.get_size() )

		dialogClass = self.dialogClasses[key]
		if hasattr( dialogClass, 'clipRect' ):
			rect = dialogClass.clipRect
		self.dialog = dialogClass(self, self.spriteGroup, rect )
		if hasattr( self.dialog, 'SetMsg' ):
			self.dialog.SetMsg( msg )

		self.subviews.append( self.dialog )

	#----------------------------------------------------------------------
	def DialogRemove(self, key):

		if not self.dialogClasses.has_key( key ):
			raise NotImplementedError

		if self.dialog.__class__ is not self.dialogClasses[key]:
			raise Exception( 'that dialog is not open' )

		#after the dialog is removed, the normal listeners should start
		#receiving events again.
		self.listeners = self.normalListeners

		#TODO: I've commented this out for now, but leave here as its
		#      an example of what might be done for multiple dialogs
		#i = 0
		#length = len( self.subviews )
		#while i < length:
			#view = self.subviews[i]
			#if view.__class__ in self.dialogClasses[key]:
				#view.Kill()
				#self.subviews.remove( view )
				#length -= 1
				#continue
			#i += 1

		self.dialog.kill()
		self.subviews.remove( self.dialog )
		self.dialog = None


	#----------------------------------------------------------------------
	def HandleTick(self):
		#Clear, Update, and Draw Everything
		self.spriteGroup.clear( self.window, self.background )

		self.spriteGroup.update()

		dirtyRects = self.spriteGroup.draw( self.window )
		
		pygame.display.update( dirtyRects )


	#----------------------------------------------------------------------
 	def Notify(self, event):
		if isinstance( event, GUIChangeScreenRequest ):
			self.SwitchView( event.key )

		elif isinstance( event, TickEvent ):
			self.HandleTick()

		elif isinstance( event, GUIDialogAddRequest ):
			self.DialogAdd( event.key, event.msg )

		elif isinstance( event, ExceptionEvent):
			ev = GUIDialogAddRequest( 'msgDialog', event.msg )
			self.evManager.Post( ev )

		elif isinstance( event, GUIDialogRemoveRequest ):
			self.DialogRemove( event.key )

		#at the end, handle the event like an EventManager should
		EventManager.Post( self, event )


#------------------------------------------------------------------------------
def main():
	"""..."""
	evManager = EventManager()

	spinner = CPUSpinnerController( evManager )
	pygameView = PygameMasterView( evManager )
	pygameCont = PygameMasterController( evManager )
	game = Game( evManager )
	
	while 1:
		try:
			spinner.Run()
		except NotImplementedError, msg:
			text = "Not Implemented: "+ str(msg)
			ev = ExceptionEvent( text )
			evManager.Post( ev )
		else:
			break;

if __name__ == "__main__":
	main()
