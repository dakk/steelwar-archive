# Steelwar

# Import Opengl Library
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Import all SteelWarEngine
from engine import *


class steelwar:
	def __init__(self):
		self.x = 800
		self.y = 600
		self.play = False#True

	def main(self):
		self.device = SDevice(self.x, self.y, False, "SteelWar")
		self.gui = SGui()
		
		self.font = self.gui.SFont("data/gui/VeraBd.ttf")
	
		c = SMesh("data/model/weapon/usa/thompson.3ds")
		print c#c.render()

		while self.play:
			self.device.Clear([0,0,0,0])

			self.font.WriteText("SteelWar Game Engine (Linux 64bit)",190,20)



			self.font.WriteText("FPS: "+str(self.device.GetFps()),890,600)

			self.device.DrawAll()
		


if __name__ == "__main__":
	steelwar = steelwar()
	steelwar.main()
