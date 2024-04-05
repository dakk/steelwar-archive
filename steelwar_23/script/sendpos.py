import GameLogic
obf = GameLogic.getCurrentController()
obj = obf.getOwner()
pos = obj.getPosition()
sock.send(pos)
