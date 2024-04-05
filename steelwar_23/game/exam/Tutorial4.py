#
# A Venom python application
# Irrlicht Tutorial 4: Movement http://irrlicht.sourceforge.net/tut004.html
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
        venom.SetWindowTitle( "Movement Example - Irrlicht Engine " )
        
        # Escape while quit the application
        venom.SetInputCallback( "keydown", "escape", self.Quit )
        
        print "Initialized."
        
    def Quit( self ):
        venom.Stop( )

    def NodeMove(self,m):
        # Move node up or down by changing Y
        # Get node position
        pos = venom.GetPosition(self.node1)
        if m==1:
            newpos = (pos[0], pos[1] + 2.0, pos[2])
        if m==0:
            newpos = (pos[0], pos[1] - 2.0, pos[2])
        # Set new node posistion
        venom.SetPosition(self.node1, newpos)

    def run( self ):
        
        # Add callback for keys W and S to do movemnt on node1
        venom.SetInputCallback( "keydown", "w", self.NodeMove, 1 )
        venom.SetInputCallback( "keydown", "s", self.NodeMove, 0 )
        print "Building scene..."
        
        #Add test node 1
        self.node1= venom.AddTestNode ( )
        venom.SetPosition( self.node1, (0,0,30) )
        venom.SetNodeTexture( self.node1, venom.LoadTexture( "../media/wall.bmp" ), 0 )
        #Add test node 2
        node2= venom.AddTestNode ( )
        venom.SetPosition( node2, (0,0,50) )
        venom.SetNodeTexture( node2, venom.LoadTexture( "../media/t351sml.jpg" ), 0 )
        #Creat the animation
        venom.CreateFlyCircleAnimator(node2, (0,0,30), 20);
    
        # Load model Sydney mesh
        self.node = venom.AddMeshNode( venom.LoadMesh( "../media/sydney.md2" ) )
        # Load texture
        venom.SetNodeTexture( self.node, venom.LoadTexture( "../media/sydney.bmp" ), 0 )
        
        # Set material flag
        venom.SetNodeMaterialFlag( self.node, venom.MAT_LIGHTING, 0 )
        # Set animation
        # 
        # venom.SetAnimationFrameLoop( self.node, 320, 360 ) can also be used for none MD2 mesh
        venom.SetMD2Animation( self.node, venom.MD2_RUN )
        venom.SetRotation ( self.node, (0,180,0))
        venom.CreateFlyStraightAnimator(self.node, (100,0,60), (-100,0,60), 10000)
        # Set animation speed
        venom.SetAnimationSpeed (self.node, 30)
        
        #Add FPS Camera
        cam = venom.AddFPSCamera( )
        # Set camera posistion and target(node1)
        venom.SetPosition( cam, (100,0,100) )
        venom.SetCameraTarget( cam, (0,0,30) )
        
        
      
        
        print "Running..."
        
    # Main game loop    
    def mainloop( self ):
        self.oldfps = 0

        while venom.ProcessEvents( ):
            self.fps = venom.GetFPS( )
            if self.fps != self.oldfps:
                self.oldfps = self.fps
                venom.SetWindowTitle( "Movement Example - Irrlicht Engine FPS: "+str(self.fps))
            venom.ProcessEventsAndRenderColor((0,200,200,200) )
            
        print "End"
            

            
            
            
    
if __name__ == "__main__":
    mygame = Game( )
    mygame.run( )
    mygame.mainloop( )
    
