CPP = g++
OPTSmain =  -I"/usr/local/include" -I"/usr/lib/irrlicht/include" -I"/usr/X11R6/include" -L"/usr/X11R6/lib" -L"/usr/lib/irrlicht/lib/Linux" -lIrrlicht -lGL -lGLU -lXxf86vm -lXext -lX11 -lraknet

OPTSeditor =  -I"/usr/lib/irrlicht/include" -I"/usr/X11R6/include" -L"/usr/X11R6/lib" -L"/usr/lib/irrlicht/lib/Linux" -lIrrlicht -lGL -lGLU -lXxf86vm -lXext -lX11


all:
	$(CPP) sw.cpp -o sw $(OPTSmain)
menu:
	$(CPP) steelwar.cpp -o steelwar $(OPTSeditor)
server:
	$(CPP) swserver.cpp -o server $(OPTSmain)
client:
	$(CPP) cl.cpp -o cl $(OPTSmain)
editor:
	$(CPP) level_editor.cpp -o editor $(OPTSeditor)

