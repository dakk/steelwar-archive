import direct.directbase.DirectStart
from pandac.PandaModules import *
import parser



class Map:
	class Mesh:
		Mesh = ""
		Position = [0,0,0]
		Rotation = [0,0,0]
		Scale = [0,0,0]
		Texture = "" 

	def __init__(self,detail):
		self.MapDir = ""
		self.Name = ""
		self.Mod = ""
		
		self.Detail = detail

		self.Teama = [0,0,0,""]
		self.Teamb = [0,0,0,""]

		self.Limits = [[0,0],[0,0],[0,0],[0,0]]

		self.MFog = None
		self.MEnv = None
		self.MSun = None
		self.MTerrain = None
		self.MObjects = []

	def TerrainGenerator(self,filename,tex,scale):
		hscale=scale[0]
		vscale=scale[1]
		heightmap = loader.loadTexture(Filename.fromOsSpecific(filename).getFullpath())
		filename = Filename(filename)
		if(tex!=None and not(isinstance(tex,Texture))):
			tex=loader.loadTexture(tex)
 
		XScale=heightmap.getXSize()*hscale #calc size
		YScale=heightmap.getYSize()*hscale #calc size
		x0=-.5*XScale     #origin of terrain mesh, panda units   
		y0= .5*YScale     #origin of terrain mesh, panda units
		XScale**=-1       #invert xscale
		YScale**=-1       #invert yscale
		fx=0              #focal point, pixel units
		fy=0              #focal point, pixel units
		threshold=8       #threshhold for moving the focal point, pixel units
 
		# Create the tesselator
		tesselator=HeightfieldTesselator('Terrain')
		tesselator.setHeightfield(filename)
		tesselator.setHorizontalScale(hscale)
		tesselator.setVerticalScale(vscale)
		tesselator.setFocalPoint(fx,fy)
 
		# Dummy node for first loop
		node1=tesselator.generate()
		while True:
			x=int((x0-camera.getX())/-hscale)
			y=int((y0-camera.getY())/ hscale)
			if abs(x-fx)>threshold or abs(y-fy)>threshold:
				fx=x
				fy=y
				tesselator.setFocalPoint(fx,fy)
				node1.removeNode()
				node1=tesselator.generate()
				node1.setTexGen(TextureStage.getDefault(),TexGenAttrib.MWorldPosition)
      		node1.setTexScale(TextureStage.getDefault(),XScale,YScale)
      		node1.setTexOffset(TextureStage.getDefault(),0.5,0.5)
      		node1.setTexture(tex)
		return node1



	def DrawMap(self, map):
		
		self.MapDir = map
		TmpParsed = parser.Parser(self.MapDir+"map.swm").get_vars()

		self.Name = TmpParsed["Name"]
		self.Mod = TmpParsed["Mod"]


		#for x in range(0,4):
			#for y in range(0,2):
				#self.Limits[x][y] = float(TmpParsed["Limit"+str(x+1)].split(",")[y])

		if TmpParsed.has_key("Teama"):
			TT = TmpParsed["Teama"].split(",")
			self.Teama = [float(TT[0]),float(TT[1]),float(TT[2]),str(TT[3])]
		if TmpParsed.has_key("Teamb"):
			TT = TmpParsed["Teamb"].split(",")
			self.Teamb = [float(TT[0]),float(TT[1]),float(TT[2]),str(TT[3])]


		if TmpParsed.has_key("Sun"):
			
			TT = TmpParsed["Sun"].split(",")
			self.MSun = AmbientLight("alight")
			self.MSun.setColor(VBase4(float(TT[0]),float(TT[1]),float(TT[2]),float(TT[3])))						
			render.setLight(render.attachNewNode(self.MSun.upcastToPandaNode()))

		if TmpParsed.has_key("Fog"):
			TT = TmpParsed["Fog"].split(",")
			
			self.MFog = Fog('Fog')
			self.MFog.setColor(float(TT[0]),float(TT[1]),float(TT[2]))
			self.MFog.setExpDensity(float(TT[3]))
			render.setFog(self.MFog)




		if TmpParsed.has_key("Terrain"):
			Terrain = TmpParsed["Terrain"]
			if Terrain.has_key("Mesh"):
				self.MTerrain = loader.loadModel(self.MapDir+Terrain["Mesh"])
				self.MTerrain.reparentTo(render)
				if Terrain.has_key("Texture"): 
					TT = Terrain["Texture"]
					self.MTerrain.setTexture(loader.loadTexture(TT))
				if Terrain.has_key("Scale"):
					TT = Terrain["Scale"].split(",")
					self.MTerrain.setScale(float(TT[0]),float(TT[1]),float(TT[2]))
			
				if Terrain.has_key("Position"):				
					TT = Terrain["Position"].split(",")
			
		
					self.MTerrain.setPos(float(TT[0]),float(TT[1]),float(TT[2]))
	
				if Terrain.has_key("Rotation"):	
					TT = Terrain["Rotation"].split(",")
		
					self.MTerrain.setHpr(float(TT[0]),float(TT[1]),float(TT[2]))

			elif Terrain.has_key("Heightmap"):
				TT = Terrain["Heightmap"].split(",")
				self.MTerrain = self.TerrainGenerator(TT[0],TT[1],(float(TT[2]),float(TT[3]),float(TT[4])))
				self.MTerrain.reparentTo(render)

				if Terrain.has_key("Scale"):
					TT = Terrain["Scale"].split(",")
					self.MTerrain.setScale(float(TT[0]),float(TT[1]),float(TT[2]))
			
				if Terrain.has_key("Position"):				
					TT = Terrain["Position"].split(",")
		
					self.MTerrain.setPos(float(TT[0]),float(TT[1]),float(TT[2]))
	
				if Terrain.has_key("Rotation"):	
					TT = Terrain["Rotation"].split(",")
	
				#self.MTerrain.reparentTo(render)
		else:
			print "No terrain"
			
			return 1

		if TmpParsed.has_key("Env"):
			self.MEnv = loader.loadModel("./data/env/"+TmpParsed["Env"]+"/"+TmpParsed["Env"])
			self.MEnv.reparentTo(render) 
			self.MEnv.setPos(0, 0, 1000)
			self.MEnv.setScale(54.5,54.5,54.5)

		for x in range(0,len(TmpParsed)):
			if TmpParsed.has_key("Obj"+str(x)):
				Mesh = TmpParsed["Obj"+str(x)]
				if Mesh.has_key("Mesh"):
					M = loader.loadModel(self.MapDir+Mesh["Mesh"])
					if M == None: M = loader.loadModel("./"+Mesh["Mesh"])
					M.reparentTo(render)

					print Mesh["Mesh"]
					if Mesh.has_key("Scale"):
						MM = Mesh["Scale"].split(",")
						M.setScale(float(TT[0]),float(TT[1]),float(TT[2]))

					if Mesh.has_key("Texture"): 
						MM = Terrain["Texture"]
						M.setTexture(loader.loadTexture(MM))

					if Mesh.has_key("Position"):				
						MM = Mesh["Position"].split(",")
			
		
						M.setPos(float(TT[0]),float(TT[1]),float(TT[2]))
	
					if Mesh.has_key("Rotation"):				
						MM = Mesh["Rotation"].split(",")
			
		
						M.setHpr(float(TT[0]),float(TT[1]),float(TT[2]))
	
					#M.reparentTo(render)
					self.MObjects.append(M)
					
					

		return 0

		
