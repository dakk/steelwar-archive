from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class SCamera:
	def __init__(self):
		self.pos_x = 0.0
		self.pos_y = 0.0
		self.pos_z = 0.0
		self.rot_x = 0.0
		self.rot_y = 0.0
		self.rot_z = 0.0

	def GetRotation(self):
		return [self.rot_x, self.rot_y, self.rot_z]

	def GetPosition(self):
		return [self.pos_x, self.pos_y, self.pos_z]

	def SetPosition(self, pos):
		self.pos_x, self.pos_y, self.pos_z = pos[0], pos[1], pos[2]

	def SetRotation(self, rot):
		self.rot_x, self.rot_y, self.rot_z = rot[0], rot[1], rot[2]
