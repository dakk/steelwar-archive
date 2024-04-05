import neheGL.glFreeType
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


class SGui:
	class SFont:
		def __init__(self,font_file):
			self.font = neheGL.glFreeType.font_data(font_file, 16)


		def WriteText(self,text,x,y):
			glPushMatrix()
			glLoadIdentity()
			# Spin the text, rotation around z axe == will appears as a 2d rotation of the text on our screen
			#glRotatef(self.cnt1, 0, 0, 1)
			#glScalef(1, 0.8 + 0.3* math.cos(1/5), 1)
			glTranslatef(-180, 0, 0)
			self.font.glPrint(x,600-y, text)
			glPopMatrix()

	#class 

	
