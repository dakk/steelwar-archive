# Steelwar Phsycs Engine
import time

class World:
	def __init__(self):
		self.Gravity = 0.0
		self.Step = 0.0


	def setGravity(self, gravity): 
		self.Gravity = gravity

	def setStep(self, step):
		self.Step = step


class Body:
	def __init__(self,World):
		self.World = World
		self.LastPosition = (0.0,0.0,0.0)
		self.Position = (0.0,0.0,0.0)
		self.Mass = 0.0
		self.Velox = (0.0,0.0,0.0)
		self.Forces = []

	def setPosition(self, position):
		self.Position = position

	def getPosition(self):
		return self.Position
	
	def setMass(self, mass):
		self.Mass = mass

	def _getGravityForce(self):
		return (self.World.Gravity * self.Mass)

	def getVelox(self):
		return self.Velox

	def addForce(self,force):
		self.Forces.append(force)

	def delForce(self,forcen):
		del self.Forces[forcen]


	def Step(self):
		pos = self.getPosition()
		self.LastPosition = last = pos

		self.setPosition((pos[0],pos[1],pos[2]-self.World.Step * self._getGravityForce()))

		for x in self.Forces:
			self.setPosition((pos[0]+x[0]/self.World.Step,pos[1]+x[1]/self.World.Step,pos[2]+x[2]/self.World.Step))

		pos = self.getPosition()
		self.Velox = ((pos[0]-last[0]/self.World.Step),(pos[1]-last[1]/self.World.Step),(pos[2]-last[2]/self.World.Step))





def Test():
	# Creiamo un mondo
	world = World()

	# Settiamo la costante gravitazionale
	world.setGravity(9.8)
	world.setStep(0.5)

	body = Body(world)
	body.setMass(0.5)




	while 1:
		body.Step()
		print "position: ",body.getPosition()
		print "velox: ",body.getVelox()
		time.sleep(0.5)	
	

if __name__ == "__main__": Test()
