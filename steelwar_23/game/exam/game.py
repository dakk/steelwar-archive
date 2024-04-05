import venom
game = True

def exit():
	game = False
	venom.Stop()

venom.Initialize('opengl', 640, 480, 24, 0)
venom.SetWindowTitle("Battlefield GL")

venom.SetInputCallback("keydown", "escape", exit())



cam = venom.AddCamera()
venom.SetPosition(cam, (0,30,-40))
venom.SetCameraTarget(cam, (0,5,0))


logo = venom.LoadTexture("data/logo3.tga")
image = venom.AddGUIElement("image",0, 500, ( 10, 10, 100, 500 ))
venom.SetGUIImageSource(image, logo)


t1 = venom.LoadTexture("data/sky2/top.jpg" )
t2 = venom.LoadTexture("data/sky2/bottom.jpg" )
t3 = venom.LoadTexture("data/sky2/left.jpg" )
t4 = venom.LoadTexture("data/sky2/right.jpg" )
t5 = venom.LoadTexture("data/sky2/front.jpg" )
t6 = venom.LoadTexture("data/sky2/back.jpg" )
Skybox = venom.AddSkyboxNode( t1, t2, t3, t4, t5, t6 )




while game:#venom.ProcessEvents():
	venom.ProcessEventsAndRenderColor((0,200,200,200))
            
