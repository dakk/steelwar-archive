from direct.showbase.DirectObject import DirectObject
from direct.task import Task

from pandac.PandaModules import *
from direct.task.Task import Task
from direct.interval.IntervalGlobal import *
import time
import parser


class Player:
	def __init__(self):
		self.PlayerNode = None
		self.Life = 100

		self.CurrentBull = 0
		self.CurrentBullMax = 0
		self.CurrentCharg = 0
		self.CurrentWeapon = "No Weapon"
		self.Weapon = None
		self.WeaponCurrent = 0
		self.Weapons = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
		self.Bullets = []
		self.BulletsDir = []
		self.Shoot = False
		self.ShootFactor = 0
		self.BulletAtr = [0,0]

		self.Map = None

		self.Team = ""

		self.CollisionEvent=CollisionHandlerQueue()

		self.FPS = 0
		self.FPSTime = 0

		self.MouseX = 0.0
		self.MouseY = 0.0
		self.MouseMove = 2.5



		self.RotX = 0
		self.RotY = 0
		self.RotZ = 0
	
		self.MoveFactor = 250

		self.Avanti = False
		self.Indietro = False
		self.Sinistra = False
		self.Destra = False

		self.heading = 180
		self.pitch = 0

	def InitPlayer(self,map):
		self.FPSTime = time.time()

		self.Map = map

		self.PlayerNode = base.camera
		self.PlayerNode.reparentTo(render)
		self.PlayerNode.setPos(self.Map.Teama[0], self.Map.Teama[1], self.Map.Teama[2])
		self.Team = self.Map.Teama[3]


		self.Lens = base.camNode.getLens()
		self.Lens.setFar(500000)
		self.Lens.setNear(0.1)



		#self.b = loader.loadModel("./mods/"+self.Map.MapDir.split("/")[-3]+"/Models/braccio")
		#self.b.reparentTo(self.PlayerNode)
		#self.b.setPos(03,60,-10)
		#self.b.setHpr(60,-90,90)
		#self.b.setTexture(loader.loadTexture("./mods/"+self.Map.MapDir.split("/")[-3]+"/Models/braccio.png"))
		#self.b.setScale(3,3,3)

		self.LoadWeaponsInfo()
		self.Weapon = self.LoadWeapon(0)


	def LoadWeaponsInfo(self):
		Weapon_Dir = "./mods/"+self.Map.MapDir.split("/")[-3]+"/Models/"+self.Team+"/"
		TmpParsed=parser.Parser(Weapon_Dir+self.Team+".txt").get_vars()

		for x in range(0,5):
			if TmpParsed.has_key("Weapon"+str(x)):
				if TmpParsed["Weapon"+str(x)].has_key("bullet"): 
					self.Weapons[x][0] = int(TmpParsed["Weapon"+str(x)]["bullet"])
				if TmpParsed["Weapon"+str(x)].has_key("bullet"): 
					self.Weapons[x][2] = int(TmpParsed["Weapon"+str(x)]["bullet"])
				if TmpParsed["Weapon"+str(x)].has_key("charg"): 
					self.Weapons[x][1]  = int(TmpParsed["Weapon"+str(x)]["charg"])
				if TmpParsed["Weapon"+str(x)].has_key("velox"): 
					self.ShootFactor = int(TmpParsed["Weapon"+str(x)]["velox"])

	def LoadWeapon(self,x):
		if self.Weapon != 0 and self.Weapon != None: 
			self.Weapon.removeNode()

		if self.Weapon != None:
			self.Weapons[self.WeaponCurrent][0] = self.CurrentBull
			self.Weapons[self.WeaponCurrent][1] = self.CurrentCharg
		
		self.WeaponCurrent = x
		self.CurrentWeapon = "No Weapon"
		self.CurrentBull = self.Weapons[x][0]
		self.CurrentBullMax = self.Weapons[x][2]
		self.CurrentCharg = self.Weapons[x][1]

		Weapon_Dir = "./mods/"+self.Map.MapDir.split("/")[-3]+"/Models/"+self.Team+"/"
		TmpParsed=parser.Parser(Weapon_Dir+self.Team+".txt").get_vars()
		
		if TmpParsed.has_key("Weapon"+str(x)):
			Mesh = TmpParsed["Weapon"+str(x)]
			M = 0
			if Mesh.has_key("model"):
				M = loader.loadModel(Weapon_Dir+Mesh["model"])
				M.reparentTo(self.PlayerNode)
				
				if Mesh.has_key("texture"):
					M.setTexture(loader.loadTexture(Weapon_Dir+Mesh["texture"]))

				if Mesh.has_key("scale"):
					MM = Mesh["scale"].split(",")
					M.setScale(float(MM[0]),float(MM[1]),float(MM[2]))

				if Mesh.has_key("position"):				
					MM = Mesh["position"].split(",")
					M.setPos(float(MM[0]),float(MM[1]),float(MM[2]))
	
				if Mesh.has_key("rotation"):				
					MM = Mesh["rotation"].split(",")
					M.setHpr(float(MM[0]),float(MM[1]),float(MM[2]))

			if Mesh.has_key("name"):
				self.CurrentWeapon = Mesh["name"]
					
			else:
				self.CurrentWeapon = "NoName"
			return M

		


	def PrintPos(self):
		print self.PlayerNode.getPos()

	def Event(self,action):
		if action == "d": self.Destra = True
		if action == "du": self.Destra = False

		if action == "a": self.Sinistra = True
		if action == "au": self.Sinistra = False

		if action == "w": self.Avanti = True
		if action == "wu": self.Avanti = False

		if action == "s": self.Indietro = True
		if action == "su": self.Indietro = False

		if action == "m1": self.Shoot = True
		if action == "m1u": self.Shoot = False

		if action == "1": self.Weapon = self.LoadWeapon(0)
		if action == "2": self.Weapon = self.LoadWeapon(1)
		if action == "3": self.Weapon = self.LoadWeapon(2)
		if action == "4": self.Weapon = self.LoadWeapon(3)
		if action == "5": self.Weapon = self.LoadWeapon(4)


	def BulletsTask(self,task):
		if self.Shoot:
			Sh = False
			if self.CurrentBull != 0:
				self.CurrentBull -= 1
				Sh = True
			if self.CurrentBull == 0:
				if self.CurrentCharg != 0:
					self.CurrentCharg -= 1
					self.CurrentBull = self.CurrentBullMax - 1
					Sh = True
	
			if Sh:
				bullet = loader.loadModel("./data/models/bullet/bullet")
				bullettexture = loader.loadTexture("./data/models/bullet/bullet.jpg")
				bullet.setTexture(bullettexture)
				bullet.setScale(0.01,0.01,0.01)
				bullet.reparentTo(render) 

				new = self.PlayerNode.getPos() + (self.PlayerNode.getMat().getRow3(1)*self.ShootFactor/10/self.FPS)
				bullet.setPos(new[0],new[1],self.PlayerNode.getZ())

				self.BulletsDir.append(self.PlayerNode.getMat().getRow3(1))
				self.Bullets.append(bullet)

		if len(self.Bullets) > 15:
			self.Bullets[0].detachNode()
			del self.BulletsDir[0]
			del self.Bullets[0]

		for x in self.Bullets:
			new = x.getPos() + (self.BulletsDir[self.Bullets.index(x)]*self.ShootFactor/10/self.FPS)
			x.setPos(new[0],new[1],x.getZ())

		return Task.cont


	def MoveTask(self,task):
		if self.Avanti:
			dir = self.PlayerNode.getMat().getRow3(1)
			new = self.PlayerNode.getPos() + (dir*(self.MoveFactor/self.FPS))	
			self.PlayerNode.setPos(new[0],new[1],self.PlayerNode.getZ())

		if self.Indietro:
			dir = self.PlayerNode.getMat().getRow3(1)
			new = self.PlayerNode.getPos() + (dir*-(self.MoveFactor/self.FPS))
			self.PlayerNode.setPos(new[0],new[1],self.PlayerNode.getZ())

		if self.Sinistra:
			dir = self.PlayerNode.getMat().getRow3(0)
			new = self.PlayerNode.getPos() + (dir*-(self.MoveFactor/self.FPS))
			self.PlayerNode.setPos(new[0],new[1],self.PlayerNode.getZ())

		if self.Destra:
			dir = self.PlayerNode.getMat().getRow3(0)
			new = self.PlayerNode.getPos() + (dir*(self.MoveFactor/self.FPS))
			self.PlayerNode.setPos(new[0],new[1],self.PlayerNode.getZ())

		return Task.cont


	def GetFPSTask(self,task):
		NewTime = time.time()
		Diff = NewTime-self.FPSTime
		self.FPSTime = NewTime
		self.FPS = 1/Diff
		return Task.cont
		

	def MouseTask(self,task):
		try:
			x = base.win.getPointer(0).getX()
			y = base.win.getPointer(0).getY()

			if base.win.movePointer(0, 100, 100):
				self.heading = self.heading - (x - 100)*0.2
				self.pitch = self.pitch - (y - 100)*0.2
			if (self.pitch < -45): self.pitch = -45
			if (self.pitch >  45): self.pitch =  45
        		self.PlayerNode.setHpr(self.heading,self.pitch,0)
		except: pass

		return Task.cont





