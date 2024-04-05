#Autore: dak

from GameLogic import *
from Rasterizer import *
a=True
f=open('tmp/scrn.txt','r')
c=f.read()
c=int(c)
c+=1
f.close()
f=open('tmp/scrn.txt','w')
f.write(str(c))
f.close()

makeScreenshot('tmp/scr'+str(c)+'.png')
