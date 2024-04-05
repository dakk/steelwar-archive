import venom
import time
import thread
import sys

    
class steelwar:
	def __init__(self):
		self.gm_name = 'SteelWar'
		self.gm_ver = '0.1'
		self.seconds = 5
		self.sleep_var = True
		self.full_screen = 0
		self.res_x = 800
		self.res_y = 600
		self.autors = 'Dak'


		print self.gm_name+' '+self.gm_ver

	def sky_box(self,t1,t2,t3,t4,t5,t6):
		t1 = venom.LoadTexture(t1)
		t2 = venom.LoadTexture(t2)
		t3 = venom.LoadTexture(t3)
		t4 = venom.LoadTexture(t4)
		t5 = venom.LoadTexture(t5)
		t6 = venom.LoadTexture(t6)
		Skybox = venom.AddSkyboxNode( t1, t2, t3, t4, t5, t6 )

	def sky_box_add(self,tipo):
		if tipo == 'light':
			self.sky_box(	"data/sky/light/top.jpg"	, 
					"data/sky/light/bottom.jpg"	, 
					"data/sky/light/left.jpg"	,
					"data/sky/light/right.jpg"	,
					"data/sky/light/front.jpg"	,
					"data/sky/light/back.jpg"	)
		if tipo == 'dark':
			self.sky_box(	"data/sky/dark/top.jpg"		, 
					"data/sky/dark/bottom.jpg"	, 
					"data/sky/dark/left.jpg"	,
					"data/sky/dark/right.jpg"	,
					"data/sky/dark/front.jpg"	,
					"data/sky/dark/back.jpg"	)

	def quit_irr(self):
		venom.Stop()


	def sleep(self):
		self.sleep_var = True
		time.sleep(self.seconds)
		self.sleep_var = False

	def init_irr(self):
		if sys.platform == 'linux2':
			venom.Initialize('opengl', self.res_x, self.res_y, 24, 0 )
		elif sys.platform == 'win32':
			venom.Initialize('directx9', self.res_x, self.res_y, 24, 0 )
		else:
			print 'Impossibile usare il gioco su piattaforma '+sys.platform
			sys.exit(0)

	def info_gm(self):
		return self.gm_name+' '+self.gm_ver+'\nFPS: '+str(venom.GetFPS())+'\nOS: '+sys.platform+'\nMap: '+sys.argv[1]+'\nAutors: '+self.autors

	def scr_irr(self):
		os.system('scrot -n scr.png')


	def gun_shot(self): 
		print 'Proiettile'
		shot = venom.LoadMesh("data/obj/thompson.x")
		shot_o = venom.AddOctTreeNode(shot)
		#shot_t = venom.LoadTexture("data/.jpg")
		venom.SetNodeTexture(shot_o, shot_t,0 )
		venom.SetPosition(shot_o, venom.GetPosition(self.main_camera))
		venom.SetRotation(shot_o, venom.GetRotation(self.main_camera))



 

	def main(self):
		self.init_irr()
		venom.ShowMouse(0)
		venom.SetWindowTitle(self.gm_name+' '+self.gm_ver)
		venom.SetInputCallback("keydown", "escape", self.quit_irr )
		venom.SetInputCallback("keydown", "stamp", self.scr_irr )
		venom.SetInputCallback("keydown", "0", self.gun_shot )


		terrain = venom.AddTerrainNode ( "data/terrain.bmp" )
		venom.SetNodeMaterialFlag( terrain, venom.MAT_LIGHTING, 0 )
		venom.SetScale ( terrain, ( 40, 4, 40))
		texture = venom.LoadTexture( "data/Landscape/big_water.bmp" )
		venom.SetNodeTexture( terrain, texture,0 )
		venom.SetPosition( terrain, ( -1300.0, -970.0, -1000.0 ) )




		venom.AddArchive('maps/'+sys.argv[1]+'.pk3')
		map = venom.LoadMesh( "map.bsp" )
		mapn = venom.AddOctTreeNode(map)
		venom.SetPosition( mapn, ( -1300.0, -120.0, -1249.0 ) )



		self.mirino = venom.LoadTexture("data/mirino.tga")
		self.mirino_o=venom.AddGUIElement("image",0,1,(self.res_x/2, self.res_y/2,6,6))
		venom.SetGUIImageSource(self.mirino_o, self.mirino)

		self.main_cam = venom.AddFPSCamera()
		venom.SetPosition( self.main_cam, ( -1300.0, -120.0, -1249.0 ) )
		
		self.gun = venom.LoadMesh( "data/obj/thompson.x" )
		self.gun_node = venom.AddOctTreeNode(self.gun)
		self.gun_text = venom.LoadTexture( "data/text/guns.jpg" )
		venom.SetNodeTexture( self.gun_node, self.gun_text,0 )
		venom.SetPosition( self.gun_node, ( -1300.0, -120.0, -1249.0 ) )


		self.sky_box_add('light')

        	self.win_info = venom.AddGUIElement("window",0,101,(50,500,200,75))
		venom.SetGUIElementText(self.win_info, "Game Info")
    		self.win_infotxt=venom.AddGUIElement("textborder",self.win_info,102,(0,20,198,73))


		while venom.ProcessEvents():
			venom.SetGUIElementText(self.win_infotxt, self.info_gm())
			
			# Posizione arma e rotazione
			campos = [0,0,0]
			campos[0] = venom.GetPosition(self.main_cam)[0]#+10
			campos[1] = venom.GetPosition(self.main_cam)[1]#-10
			campos[2] = venom.GetPosition(self.main_cam)[2]#+5
			venom.SetPosition( self.gun_node, campos)
			venom.SetRotation( self.gun_node, venom.GetRotation(self.main_cam))
			venom.ProcessEventsAndRender()

	
			
	
if __name__ == "__main__":
	steelwar = steelwar( )
	steelwar.main()

	
