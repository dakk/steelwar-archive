import GameLogic
import Rasterizer

obf = GameLogic.getCurrentController()
obj = obf.getOwner()

#wh = Rasterizer.getWindowHeight()
#ww = Rasterizer.getWindowWidth()
#mouse=obj.getSensor("MOUSE")

#SCALE=[.3, .3]
#x = (ww/2 - mousemove.getXPosition())*SCALE[0]
#y = (wh/2 - mousemove.getYPosition())*SCALE[1]

#mx = mouse.getXPosition()
#my = mouse.getYPosition()

obj.setOrientation(0.9)#obb.rot + mx
#Rasterizer.setMousePosition(ww/2, wh/2)
