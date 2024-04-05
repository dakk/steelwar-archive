import GameLogic

obf = GameLogic.getCurrentController()
obj = obf.getOwner()
f = open('tmp/line1.txt','r')
c = f.read()
f.close()
obj.Text = c