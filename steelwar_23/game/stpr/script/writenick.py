import GameLogic
nick=open('./tmp/nick.txt', 'w')
cont=GameLogic.getCurrentController()
own = cont.getOwner()
l=own.Text
nick.write(l)