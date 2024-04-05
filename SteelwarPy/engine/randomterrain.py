import Image
import ImageDraw
import sys
import random

def GetRandomMap(max,dim):
	map = []
	for x in range(0,dim):
		l = []
		for y in range(0,dim):
			l.append(random.randint(1,max))
		map.append(l)

	return map


def SmoothMap(map,dim):
	for x in range(1,dim-1):
		for y in range(1,dim-1):
			smooth = map[x-1][y]+map[x+1][y]+map[x-1][y+1]+map[x-1][y-1]+map[x+1][y+1]+map[x+1][y-1]+map[x][y]
			map[x][y] = smooth/7

	return map 

def PrintMap(map):
	for x in map:
		line = ""
		for y in x:
			line+=str(y)
		print line

def GetEggCode(map,dim):
	egg = "<CoordinateSystem> { Y-Up-Left } \n\n"
	egg += "<Comment> { \"SteelwarTerrainGenerator\" } \n"
	egg += "<Material> mref1 {\n"
	egg += "\t<Scalar> diffr { 0.8 }\n"
	egg += "\t<Scalar> diffg { 0.8 }\n"
	egg += "\t<Scalar> diffb { 0.8 }\n"
	egg += "\t<Scalar> specr { 1 }\n"
	egg += "\t<Scalar> specg { 1 }\n"
	egg += "\t<Scalar> specb { 1 }\n"
	egg += "\t<Scalar> shininess { 0.5 }\n}\n\n"
	
	egg += "<Group> Mesh_Plane {\n"
	egg += "\t<VertexPool> Mesh_Plane {\n"
   
	num = 1
	for x in range(0,dim):
		for y in range(0,dim):
			egg += "\t\t<Vertex> "+str(num)+" {\n"
			egg += "\t\t\t"+str(y)+" "+str(x)+" "+str(map[x][y])+"\n"
			egg += "\t\t\t<Normal> { 0 -1 0 }\n"
			egg += "\t\t}\n"
			num += 1
	egg += "\t}"

	num = 1


	for x in range(0,(dim-1)/2):
		for y in range(0,(dim-1)/2):
			egg += "\t<Polygon> {\n"
			egg += "\t\t<RGBA> { 0.8 0.8 0.8 1 }\n"
			egg += "\t\t<MRef> { mref1 }\n"
			egg += "\t\t<VertexRef> { "+str(num)+" "+str(num+1)+" "+str(num+dim)+" "+str(num+dim+1)+" <Ref> { Mesh_Plane } }\n"
			egg += "\t}\n"
			num += 1
		num += 1

	egg += "}\n"

	return egg

def DrawHeight(map,dim,max):
	HeightMap = Image.new("RGB",(dim,dim))

	Draw = ImageDraw.Draw(HeightMap)
	for x in range(0,dim):
		for y in range(0,dim):
			Draw.point((x,y),(255,255,255))

	for x in range(0,dim):
		for y in range(0,dim):
			Color = (map[x][y]*255)/max
			Draw.point((x,y),(Color,Color,Color))

	HeightMap.save("asda.bmp")
	

map = GetRandomMap(5,64)
map = SmoothMap(map,64)
#PrintMap(map)
DrawHeight(map,64,5)
#open("file.egg","w").write(GetEggCode(map,40))

