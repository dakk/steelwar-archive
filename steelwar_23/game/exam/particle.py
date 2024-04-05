#
# A Venom python application
# Basic quake3 map load with a FPS camera
# and with Particel system
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
            
        if not venom.Initialize( driver, 640, 480, 24, 0 ):
            print "Could not initialize."
            sys.exit(2)
        #Disable mouse cursor
        venom.ShowMouse( 0 )
        venom.SetWindowTitle( "Venom maptest" )
        
        # Loding map archive
        if not venom.AddArchive( "../media/maps/castle.pk3"):
            print "Could not load leve archive!"
            sys.exit( 2 )

        # Escape while quit the application
        venom.SetInputCallback( "keydown", "escape", self.Quit )
        print "Initialized."
        
    def Quit( self ):
        venom.Stop( )
        

    def run( self ):
        print "Building scene..."
            
        # Load and initialize map/polygon selector
        map = venom.LoadMesh( "map.bsp" )
        mapNode = venom.AddOctTreeNode( map )
        selector = venom.CreateOctTreeSelector( mapNode, map )
        venom.SetSelector( mapNode, selector )
        venom.SetNodeID( mapNode, 1 )

        # Position map
        venom.SetPosition( mapNode, ( -1300.0, -144.0, -1249.0 ) )
        
        
        #Paricel system
        part = venom.AddParticleNode (  )
        venom.SetPosition( part, (40,10,140))
        venom.SetScale( part, (2,2,2))
        venom.SetParticleSize(part, (20,10))
        venom.AddParticleBoxEmitter( part,(-7,0,-7,7,1,7), (0,0.03,0), (80,100), (800,200) )
        venom.AddFadeOutParticleAffector( part )
        venom.SetNodeTexture( part, venom.LoadTexture( "../media/particle.bmp" ), 0 )
        venom.SetNodeMaterialFlag( part, venom.MAT_LIGHTING, 0 )
        venom.SetNodeMaterialType( part, venom.MAT_TRANSPARENT_VERTEX_ALPHA )
        



                
        node = venom.AddFPSCamera( )
        
        
        print "Running..."
        
        
    def mainloop( self ):
        self.oldfps = 0

        while venom.ProcessEvents( ):
            self.fps = venom.GetFPS( )
            if self.fps != self.oldfps:
                self.oldfps = self.fps
                venom.SetWindowTitle( "Venom maptest FPS: "+str(self.fps))
            venom.ProcessEventsAndRender( )
        print "End"
            

            
            
            
    
if __name__ == "__main__":
    mygame = Game( )
    mygame.run( )
    mygame.mainloop( )
    
