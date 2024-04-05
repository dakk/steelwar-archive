#
# A Venom python application
# Basic terrain example
#
#
# Copyright (C) 2004-2005 Martin Stenhård
# This file is part of the "Venom for Irrlicht".
# For conditions of distribution and use, see copyright notice in README.TXT

import venom
import sys


class Game:
	def __init__( self ):
		print "Initializing..."
	
		if sys.platform == "win32" : 
			driver = "directx9"
		elif sys.platform == "linux2" :
			driver = "opengl"
		else :
			print "None suported platfrom", sys.platform
			sys.exit(2)
			
		if not venom.Initialize( driver , 800, 600, 24, 0 ):
			print "Could not initialize."
			sys.exit(2)
		#Disable mouse cursor
		venom.ShowMouse( 0 )
		venom.SetWindowTitle( "Venom terrain test" )
		
		#Load skybox
		if not venom.AddArchive( "../media/bright.pk3" ):
			print "Could not load skybox!" 	
			
		# Escape while quit the application
		venom.SetInputCallback( "keydown", "escape", self.Quit )
		print "Initialized."

		

	def Quit( self ):
		venom.Stop( )

	def run( self ):
		print "Building scene..."
		
		terrain = venom.AddTerrainNode ( "../media/terrain-heightmap.bmp" )
		venom.SetNodeMaterialFlag( terrain, venom.MAT_LIGHTING, 0 )
		venom.SetScale ( terrain, ( 40, 4, 40))
		texture = venom.LoadTexture( "../media/terrain-texture.jpg" )
		venom.SetNodeTexture( terrain, texture,0 )
		
		
		t1 = venom.LoadTexture( "top.jpg" )
		t2 = venom.LoadTexture( "bottom.jpg" )
		t3 = venom.LoadTexture( "left.jpg" )
		t4 = venom.LoadTexture( "right.jpg" )
		t5 = venom.LoadTexture( "front.jpg" )
		t6 = venom.LoadTexture( "back.jpg" )
		Skybox = venom.AddSkyboxNode( t1, t2, t3, t4, t5, t6 )
		
		
		node = venom.AddFPSCamera( )
		venom.SetPosition( node, (200.0, 700.0, 600.0) )
		
	def mainloop( self ):
		self.oldfps = 0

		while venom.ProcessEvents( ):
			self.fps = venom.GetFPS( )
			if self.fps != self.oldfps:
				self.oldfps = self.fps
				venom.SetWindowTitle( "Venom terrain test FPS: "+str(self.fps))
			venom.ProcessEventsAndRender( )
		print "End"
			

						
	
if __name__ == "__main__":
	mygame = Game( )
	mygame.run( )
	mygame.mainloop( )
	
