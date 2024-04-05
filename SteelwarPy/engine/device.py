import direct.directbase.DirectStart
from pandac.PandaModules import *


class Device:
	def InitDevice(self,r,g,b):
		base.setBackgroundColor(r,g,b)
		base.disableMouse() 
		base.enableAllAudio()
		props = WindowProperties()
		props.setCursorHidden(True)
		base.win.requestProperties(props)

	def ScreenShoot(self):
		base.screenshot('screenshoot/steelwar')
