from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

class SDevice:
	def __init__(self, x, y, full, title):
		self.x, self.y, self.full = x, y, full
		glutInit(())
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE |GLUT_DEPTH)
		glutInitWindowSize(self.x, self.y)
		glutInitWindowPosition(0, 0)
		glutCreateWindow(title)

		if self.full: glutFullScreen()


		self.time_start = 0
		self.time_end = 0


	def SetTitle(self, title):
		glutCreateWindow(title)

	def Clear(self, color):
		self.time_startb = time.time()
		glClearColor(color[0], color[1], color[2], color[3])
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	def DrawAll(self):
		glutSwapBuffers()
		self.time_start = self.time_startb
		self.time_end = time.time()

	def GetFps(self):
		if self.time_end == 0 or self.time_start == 0: return 0
		else: return int(1.0/float(self.time_end - self.time_start))
		
