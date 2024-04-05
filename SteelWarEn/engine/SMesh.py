from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Dice3DS import dom3ds
from Dice3DS.example import gltexture, glmodel

class SMesh:
	def __init__(self, file):
		#self.a = dom3ds.read_3ds_file(file)
		texcache = {}
		def load_texture(texfilename):
			if texcache.has_key(texfilename):
				return texcache[texfilename]
			tex = gltexture.Texture(texfilename,*texture_options)
			texcache[texfilename] = tex
			return tex
	
		dom = dom3ds.read_3ds_file(file)
		self.a =  gltexture.modelclass(dom,load_texture)
	
	#def render(self):
	#	glmodel.GLMesh(self.a).render()
