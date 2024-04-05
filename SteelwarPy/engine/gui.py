import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.task.Task import Task
from direct.interval.IntervalGlobal import *   
from direct.gui.DirectGui import *
from direct.gui.OnscreenImage import OnscreenImage 


class Gui:
	Player = None

	def InitGui(self):
		self.Title = TopTitle("Steelwar: Programming")
		
		self.Life = Label("100%",.09,1.13,-0.95)
		self.BullLeft = Label("0/0",.09,-1.30,-0.95)
		self.Team = Label("None",.09,0.00,-0.95)
		self.Mirino = Image("./data/gui/mirino.png",(0,0,0),0.04,0,0.04)
		self.Mirino.SetTrasp()

	def UpdateTask(self, task):
		self.Life.SetText(str(self.Player.Life)+"%")
		self.BullLeft.SetText(str(self.Player.CurrentBull)+"/"+str(self.Player.CurrentCharg)+"  "+self.Player.CurrentWeapon)
		self.Team.SetText(self.Player.Team[0].upper()+self.Player.Team[1:])
		return Task.cont


class TopTitle:
	def __init__(self, title):
		self.top = OnscreenText(text=title, style=2, fg=(0,0,0,0), pos=(-0.97,0.9), scale = .08,mayChange = 1)
		
	def SetTitle(self,title):
		self.top.setText(title)


class Image:
	def __init__(self,file,pos,*args):
		self.img = OnscreenImage(file, pos)
		self.img.setScale(args[0],args[1],args[2])

	def SetTrasp(self):
		self.img.setTransparency(TransparencyAttrib.MAlpha)


class Label:
	def __init__(self,text,scale,x,y):
		self.label = OnscreenText(text=text,style=1,pos=(x,y),align=TextNode.ALeft,scale=scale,mayChange=1,fg=(1,1,1,1))
				
	def SetText(self,text):
		self.label.setText(text)

class Chat:
	def __init__(self, num):
		self.lines = []
		self.text = []
		self.num = num
		self.curr = 0
		for x in range(1,num):
			a = OnscreenText(style=1,pos=(-1.3,0.85-(.05*x)),align=TextNode.ALeft,scale=.06,mayChange=1,fg=(1,1,1,1))
			self.lines.append(a)
		
	def AddLine(self, text):
		self.text.append(text)

		if len(self.text) == self.num:
			del self.text[0]

		for x in range(0,self.num-1):
			try: self.lines[x].setText(self.text[x])
			except: pass

	
