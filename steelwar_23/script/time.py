import time
import GameLogic

obf = GameLogic.getCurrentController()
obj = obf.getOwner()
obj.Text = str(time.strftime("%H:%M:%S", time.gmtime()))
