#
# A Venom python application
# Irrlicht Tutorial 5: User Interface http://irrlicht.sourceforge.net/tut005.html
# 

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
        venom.SetWindowTitle( "Irrlicht Engine - User Inferface Demo" )
        
  

        # Escape while quit the application
        venom.SetInputCallback( "keydown", "escape", self.Quit )
        print "Initialized."
        
    def Quit( self ):
        #Quit Venom
        venom.Stop( )
        
    def NewWin (self):
        #Open a new Window
        venom.AddListBoxItem (self.listBox, "Window created")
        self.cnt = self.cnt + 30 
        win = venom.AddGUIElement( "window", 0, 101, ( 100 + self.cnt , 100 + self.cnt, 200, 100 ) )
        venom.SetGUIElementText(win, "Test window")
        text = venom.AddGUIElement("textborder", win, 102, (35,35,140,15) )
        venom.SetGUIElementText(text, "Please close me")
    
    def FileOpen (self):
        #Open file Dialog
        venom.AddListBoxItem (self.listBox, "File Open")
        fileopen = venom.AddGUIElement("addFileDialog",0,101, (0,0,0,0) )
        venom.SetGUIElementText(fileopen, "Please choose a file.")
        
    def scrollbar(self, id):
        #Read scrollbar pos and set GUI Transparency
        venom.SetGUISkinColorTransparency(venom.GetGUIScrollBarPos(self.sBar))

    def run( self ):
        self.cnt = 0
        print "Building scene..."
            
        #Load GUI font
        gfont = venom.LoadGUIFont( "../media/fonthaettenschweiler.bmp")
        venom.SetGUIFont(gfont)
      
        #Add GUI button
        bquit = venom.AddGUIElement("button",0,101, (10,210,100,40) )
        venom.SetGUIElementText(bquit,"Quit")
        venom.SetGUICallback("clicked", 101, self.Quit)
        
        bnew = venom.AddGUIElement("button",0,102, (10,250,100,40) )
        venom.SetGUIElementText(bnew,"New")
        venom.SetGUICallback("clicked", 102, self.NewWin)
        bfile = venom.AddGUIElement("button",0,103, (10,300,100,40) )
        venom.SetGUIElementText(bfile,"File Open")
        venom.SetGUICallback("clicked", 103, self.FileOpen)
        
        #Add GUI text
        gtxt = venom.AddGUIElement( "text", 0, 100, (200,5,200,22) )
        venom.SetGUIElementText(gtxt, "Hello World!")

        #Add GUI Image
        logo = venom.LoadTexture( "../media/irrlichtlogoalpha.tga" )
        image = venom.AddGUIElement( "image",0, 200, ( 10, 10, 100, 100 ) )
        venom.SetGUIImageSource( image, logo )
        
        #Add Scrollbar
        gtxt = venom.AddGUIElement( "textborder", 0, 100, (150,20,350,20) )
        venom.SetGUIElementText(gtxt, "Transparent Control:")
        self.sBar = venom.AddGUIElement("scrollbar_horizontal", 0, 104, (150, 45, 350, 15) )
        venom.SetGUIScrollBarMax(self.sBar, 255)
        venom.SetGUIScrollBarPos(self.sBar, 255)
        venom.SetGUICallback("scrollbar_changed", 104, self.scrollbar,1)
        
        #Add listbox
        gtxt = venom.AddGUIElement( "textborder", 0, 100, (50,80,250,20) )
        venom.SetGUIElementText(gtxt, "Logging ListBox:")
        self.listBox = venom.AddGUIElement("listbox", 0, 105, (50, 110, 250, 90) ) 
        venom.AddListBoxItem (self.listBox, "Test")
 
        print "Running..."
        
    # Main game loop    
    def mainloop( self ):
        self.oldfps = 0

        while venom.ProcessEvents( ):
            self.fps = venom.GetFPS( )
            if self.fps != self.oldfps:
                self.oldfps = self.fps
                venom.SetWindowTitle( "Irrlicht Engine - User Inferface Demo FPS: "+str(self.fps))
            venom.ProcessEventsAndRenderColor((0,200,200,200) )
        print "End"
            

            
            
            
    
if __name__ == "__main__":
    mygame = Game( )
    mygame.run( )
    mygame.mainloop( )
    
