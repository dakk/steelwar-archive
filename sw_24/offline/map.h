// SteelWar
// Autore: dak (dak.netsons.org)
// Licenza CreativeCommons


#ifndef _MAP_H_
#define _MAP_H_

#include <irrlicht.h>
#include <iostream.h>
#include <stdio.h>


using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;

class swmap{
	public:

		void init(IrrlichtDevice*, IVideoDriver*,ISceneManager*,IGUIEnvironment*);
		void skybox(int);
		void add_box(int,int,int,int);
		void load_map(char *path);
	
		// Per irrlicht
		IrrlichtDevice *device;
		IVideoDriver* driver;
		ISceneManager* smgr;
		IGUIEnvironment* guienv;
	
		IAnimatedMesh* level_mesh;
		ITriangleSelector* level_selector;
		ISceneNode* level_node;
	
		IAnimatedMesh* level_mesh1;
		ISceneNode* level_node1;
	
		ISceneNode* light_sun;
		bool play;
	
};

void swmap::init(IrrlichtDevice *dev, IVideoDriver* driv,ISceneManager* sm,IGUIEnvironment* gui){
	device = dev;
	driver = driv;
	smgr = sm;
	guienv = gui;
	
}

void swmap::load_map(char *file_path){
	light_sun = smgr->addLightSceneNode(0, core::vector3df(0,0,0), video::SColorf(1.0f, 1.0f, 1.0f, 1.0f), 8000.0f);
	light_sun->setPosition(vector3df(0.0,40,0.0));
	
	device->getFileSystem()->addZipFileArchive(file_path);
	level_mesh = false;
	if(!level_mesh){ level_mesh = smgr->getMesh("map.x"); }
	if(!level_mesh){ level_mesh = smgr->getMesh("map.3ds"); }
	if(!level_mesh){ level_mesh = smgr->getMesh("map.bsp"); }
	if(!level_mesh){ level_mesh = smgr->getMesh("map.obj"); }
	if(level_mesh){
		level_node = smgr->addOctTreeSceneNode(level_mesh->getMesh(0)); 
		level_node->setScale(vector3df(0.5,0.5,0.5));
		level_selector = smgr->createOctTreeTriangleSelector(level_mesh->getMesh(0), level_node, 128);
		level_node->setTriangleSelector(level_selector);
		level_selector->drop();
	}
	else{
		cout<<"Mappa non trovata\n";
		play = false;
	}
}

void swmap::skybox(int a){
	// Skybox
	/*
	char pos[] = "light";
	driver->setTextureCreationFlag(video::ETCF_CREATE_MIP_MAPS, false);
	int ii = strlen(pos)+strlen("data/sky/");

	const int temp = ii;
	char* temp2= strcat("data/sky/",pos);
	char ss[temp];
	
	strncpy( ss, temp2, ii );
	cout << ss << "\n";
	*/
	
	//ss = char(temp2);
	/*
	smgr->addSkyBoxSceneNode(
		driver->getTexture(strcat(ss, "/up.jpg") ),
		driver->getTexture(strcat(ss, "/up.jpg") ),
		driver->getTexture(strcat(ss, "/up.jpg") ),
		driver->getTexture(strcat(ss, "/up.jpg") ),
		driver->getTexture(strcat(ss, "/up.jpg") ),
		driver->getTexture(strcat(ss, "/up.jpg") ) );
		*/
		
	if(a==1){
	smgr->addSkyBoxSceneNode(
		driver->getTexture("data/sky/1/up.jpg"),
		driver->getTexture("data/sky/1/dn.jpg"),
		driver->getTexture("data/sky/1/lf.jpg"),
		driver->getTexture("data/sky/1/rt.jpg"),
		driver->getTexture("data/sky/1/ft.jpg"),
		driver->getTexture("data/sky/1/bk.jpg")); 
		}
		
	if(a==2){
	smgr->addSkyBoxSceneNode(
		driver->getTexture("data/sky/2/up.jpg"),
		driver->getTexture("data/sky/2/dn.jpg"),
		driver->getTexture("data/sky/2/lf.jpg"),
		driver->getTexture("data/sky/2/rt.jpg"),
		driver->getTexture("data/sky/2/ft.jpg"),
		driver->getTexture("data/sky/2/bk.jpg")); 
		}
		
	if(a==3){
	smgr->addSkyBoxSceneNode(
		driver->getTexture("data/sky/3/all.jpg"),
		driver->getTexture("data/sky/3/all.jpg"),
		driver->getTexture("data/sky/3/all.jpg"),
		driver->getTexture("data/sky/3/all.jpg"),
		driver->getTexture("data/sky/3/all.jpg"),
		driver->getTexture("data/sky/3/all.jpg"));
		}
		
	driver->setTextureCreationFlag(video::ETCF_CREATE_MIP_MAPS, true);
}

void swmap::add_box(int l,int x,int y,int z){
	scene::ISceneNode* cube = smgr->addTestSceneNode(l);
	cube->setPosition(core::vector3df(x,y,z));
	cube->setMaterialTexture(0, driver->getTexture("data/texture/box.jpg"));
	cube->setMaterialFlag(video::EMF_LIGHTING, false);
}

#endif
