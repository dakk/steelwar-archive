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
		void lens_init();
		void add_box(int,int,int,int);
		void load_map(char *path);
		void update_lens();
		void update_cam(ICameraSceneNode*);
	
		// Per irrlicht
		IrrlichtDevice *device;
		IVideoDriver* driver;
		ISceneManager* smgr;
		IGUIEnvironment* guienv;
	
		IAnimatedMesh* water;
		ISceneNode* water_node;
		IAnimatedMesh* level_mesh;
		ITriangleSelector* level_selector;
		ISceneNode* level_node;
	
		IAnimatedMesh* level_mesh1;
		ISceneNode* level_node1;
	
		ISceneNode* light_sun;
		
		ITexture* lens0;
		ITexture* lens1;
		ITexture* lens2;
		ITexture* lens3;
		ITexture* lens4;
		ISceneNode* lensNode1;
		ISceneNode* lensNode2;
		ISceneNode* lensNode3;
		ISceneNode* lensNode4;
		ISceneNode* lensNode0;
		
		ICameraSceneNode* cam_game;
		
		bool play;
	
};

void swmap::init(IrrlichtDevice *dev, IVideoDriver* driv,ISceneManager* sm,IGUIEnvironment* gui){
	device = dev;
	driver = driv;
	smgr = sm;
	guienv = gui;
}

void swmap::update_cam(ICameraSceneNode* cam){
	cam_game = cam;
}

void swmap::update_lens(){
	vector3df pos = cam_game->getPosition();
	vector3df light = vector3df(1544.0f, 6631.0f, -2132.0f);
	float d = pos.getDistanceFrom(light);
	vector3df f = pos - cam_game->getTarget();
	f.setLength(-d);
	line3d<f32> line;
	line.start = light;
	line.end = pos + f;
	vector3df m = line.getMiddle();
	   
	line3d<f32> line2;
	line2.start = m;
	line2.end = light;
	vector3df q = line2.getMiddle();
	   
	lensNode0->setPosition( light );
	lensNode1->setPosition( m );
	lensNode2->setPosition( q );
	lensNode3->setPosition( light );
	//map.lensNode4->setPosition( m );
}

void swmap::lens_init(){
	lens0 = driver->getTexture("data/fx/flare/flare0.jpg");
	lens1 = driver->getTexture("data/fx/flare/flare1.jpg");
	lens2 = driver->getTexture("data/fx/flare/flare2.jpg");
	lens3 = driver->getTexture("data/fx/flare/flare3.jpg");
	lens4 = driver->getTexture("data/fx/flare/flare4.jpg");
	driver->makeColorKeyTexture(lens0, position2d<s32>(1,1));
	driver->makeColorKeyTexture(lens1, position2d<s32>(1,1));	
	driver->makeColorKeyTexture(lens2, position2d<s32>(1,1)); 
	driver->makeColorKeyTexture(lens3, position2d<s32>(1,1)); 
	driver->makeColorKeyTexture(lens4, position2d<s32>(1,1)); 

	lensNode0 = smgr->addBillboardSceneNode(0, dimension2d<f32>(1860, 1860));
	lensNode0->setMaterialType(EMT_TRANSPARENT_ADD_COLOR);
	lensNode0->setMaterialTexture(0, lens0);
	lensNode0->setPosition(vector3df(0,0,0));//cam_game->getPosition());
	
	lensNode1 = smgr->addBillboardSceneNode(0, dimension2d<f32>(1860, 1860));
	lensNode1->setMaterialType(EMT_TRANSPARENT_ADD_COLOR);
	lensNode1->setMaterialTexture(0, lens1);
	lensNode1->setPosition(vector3df(0,0,0));//cam_game->getPosition());
	
	lensNode2 = smgr->addBillboardSceneNode(0, dimension2d<f32>(1860, 1860));
	lensNode2->setMaterialType(EMT_TRANSPARENT_ADD_COLOR);
	lensNode2->setMaterialTexture(0, lens4);
	lensNode2->setPosition(vector3df(0,0,0));//cam_game->getPosition());
	
	lensNode3 = smgr->addBillboardSceneNode(0, dimension2d<f32>(1560, 1560));
	lensNode3->setMaterialType(EMT_TRANSPARENT_ADD_COLOR);
	lensNode3->setMaterialTexture(0, lens3);
	lensNode3->setPosition(vector3df(0,0,0));//cam_game->getPosition());
	/*
	lensNode4 = smgr->addBillboardSceneNode(0, dimension2d<f32>(560, 560));
	lensNode4->setMaterialType(EMT_TRANSPARENT_ADD_COLOR);
	lensNode4->setMaterialTexture(0, lens4);
	lensNode4->setPosition(vector3df(0,0,0));//cam_game->getPosition());*/
       
}

void swmap::load_map(char *file_path){
	light_sun = smgr->addLightSceneNode(0, core::vector3df(0,0,0), video::SColorf(1.0f, 1.0f, 1.0f, 1.0f), 8000.0f);
	light_sun->setPosition(vector3df(0.0,40,0.0));
	
	water = smgr->addHillPlaneMesh("myHill",
		core::dimension2d<f32>(999,999),
		core::dimension2d<s32>(40,40), 0, 0,
		core::dimension2d<f32>(0,0),
		core::dimension2d<f32>(10,10));



	water_node = smgr->addWaterSurfaceSceneNode(water->getMesh(0), 5.0f, 300.0f, 30.0f);
	water_node->setPosition(vector3df(0,-150,0));
	//water_node->setMaterialTexture(0,	driver->getTexture("data/texture/water.jpg"));
	water_node->setMaterialTexture(0,	driver->getTexture("data/texture/water.bmp"));
	//water_node->setMaterialType(EMT_SPHERE_MAP);
	//water_node->setMaterialType(EMT_REFLECTION_2_LAYER);

	
	device->getFileSystem()->addZipFileArchive(file_path);
	level_mesh = false;
	if(!level_mesh){ level_mesh = smgr->getMesh("map.x"); }
	if(!level_mesh){ level_mesh = smgr->getMesh("map.3ds"); }
	if(!level_mesh){ level_mesh = smgr->getMesh("map.bsp"); }
	if(!level_mesh){ level_mesh = smgr->getMesh("map.obj"); }
	if(level_mesh){
		level_node = smgr->addOctTreeSceneNode(level_mesh->getMesh(0)); 
		level_node->setScale(vector3df(0.5,0.5,0.5));
		//level_node->setMaterialFlag(video::EMF_NORMALIZE_NORMALS, true);
		
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
	scene::ISceneNode* cube = 0;//smgr->addTestSceneNode(l);
	//cube->setPosition(core::vector3df(x,y,z));
	//cube->setMaterialTexture(0, driver->getTexture("data/texture/box.jpg"));
	//cube->setMaterialFlag(video::EMF_LIGHTING, false);
}

#endif
