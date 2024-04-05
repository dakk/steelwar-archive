// SteelWar
// Autore: dak (dak.netsons.org)
// Licenza CreativeCommons


#ifndef _ENEMY_H_
#define _ENEMY_H_

#include <irrlicht.h>
#include <iostream.h>
#include <stdio.h>


using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;

class swenemy{
	public:
		void init(IrrlichtDevice*, IVideoDriver*,ISceneManager*,IGUIEnvironment*);
		void mostro();
		bool play;
	
		// Per irrlicht
		IrrlichtDevice *device;
		IVideoDriver* driver;
		ISceneManager* smgr;
		IGUIEnvironment* guienv;
	
		// Per lasciare la versione giocabile, metto un mostro merdoso
		IAnimatedMeshSceneNode* mostri;	
		ISceneNodeAnimator* mostri_coll;
		IAnimatedMesh* mostrom;
		video::ITexture* mostrot;
	
		scene::ITriangleSelector* level_selector;
	
};

void swenemy::init(IrrlichtDevice *dev, IVideoDriver* driv,ISceneManager* sm,IGUIEnvironment* gui){
	device = dev;
	driver = driv;
	smgr = sm;
	guienv = gui;
	
	mostrom = smgr->getMesh("data/model/enemy/tris.md2"); 
	mostrot = driver->getTexture("data/model/enemy/skin.jpg");
	
}

void swenemy::mostro(){
	
	mostri = smgr->addAnimatedMeshSceneNode(mostrom);
	mostri->setMaterialTexture(0, mostrot );
	mostri_coll = smgr->createCollisionResponseAnimator(level_selector, mostri, core::vector3df(20,40,20),core::vector3df(0,-3,0),core::vector3df(0,50,0));
	mostri->addAnimator(mostri_coll);
	mostri_coll ->drop();	
}


#endif
