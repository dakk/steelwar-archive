#
# A Venom python application
# Irrlicht Tutorial 1: HelloWorld http://irrlicht.sourceforge.net/tut001.html
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
        #venom.ShowMouse( 0 )
        venom.SetWindowTitle( "Hello World! - Irrlicht Engine Demo" )
        
        # Escape while quit the application
        venom.SetInputCallback( "keydown", "escape", self.Quit )
        print "Initialized."
        
    def Quit( self ):
        venom.Stop( )
        

    def run( self ):
        print "Building scene..."
            
        # Load model mesh
        node = venom.AddMeshNode( venom.LoadMesh( "../media/sydney.md2" ) )
        # Load texture
        venom.SetNodeTexture( node, venom.LoadTexture( "../media/sydney.bmp" ), 0 )
        
        # Set material flag
        venom.SetNodeMaterialFlag( node, venom.MAT_LIGHTING, 0 )
        # Set animation
        venom.SetMD2Animation( node, venom.MD2_STAND )
        
        #Add Camera        
        cam = venom.AddCamera( )
        # Set camera posistion
        venom.SetPosition( cam, (0,30,-40) )
        # Ser Camera target
        venom.SetCameraTarget( cam, (0,5,0) )
        
        #Add GUI text
        gtxt = venom.AddGUIElement( "textborder", 0, 100, (10,10,200,22) )
        venom.SetGUIElementText(gtxt, "Hello World! This is the Irrlicht with Python")
        
        print "Running..."
        
    # Main game loop    
    def mainloop( self ):
        self.oldfps = 0

        while venom.ProcessEvents( ):
            self.fps = venom.GetFPS( )
            if self.fps != self.oldfps:
                self.oldfps = self.fps
                venom.SetWindowTitle( "Hello World! - Irrlicht Engine Demo FPS: "+str(self.fps))
            venom.ProcessEventsAndRenderColor((0,200,200,200) )
            
        print "End"
            

            
            
            
    
if __name__ == "__main__":
    mygame = Game( )
    mygame.run( )
    mygame.mainloop( )
    
