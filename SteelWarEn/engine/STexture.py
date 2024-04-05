from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Image import *

class STexture:
	def __init__(self, path):
		image = open(path)
		self.x = image.size[0]
		self.y = image.size[1]
		self.Texture = image.tostring("raw", "RGBX", 0, -1)
		
		
