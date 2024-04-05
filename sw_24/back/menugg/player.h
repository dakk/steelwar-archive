// SteelWar
// Autore: dak (dak.netsons.org)
// Licenza CreativeCommons

#ifndef _PLAYER_H_
#define _PLAYER_H_

#include <irrlicht.h>
#include <iostream.h>
#include <stdio.h>


using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;


class swplayer{
	public:
		void init(IrrlichtDevice*, IVideoDriver*,ISceneManager*,IGUIEnvironment*);//,scene::ITriangleSelector*);
	
		void camera(int,int,int);
		void camera_sl();
		void shoot();
		void recarge();
		void show_life();
		void show_bullets();
		void show_mirino();
		
		int weapon;
		int bullets;
		int carge;
		int life;
	
		// Per irrlicht
		IrrlichtDevice *device;
		IVideoDriver* driver;
		ISceneManager* smgr;
		IGUIEnvironment* guienv;
	
		
		video::ITexture* l100;
		video::ITexture* l80;
		video::ITexture* l60;
		video::ITexture* l50;
		video::ITexture* l30;
		video::ITexture* l10;
		
		video::ITexture* mirino;
	
		ICameraSceneNode* cam_game;
		ICameraSceneNode* cam_sleep;
		scene::ISceneNodeAnimator* cam_coll;
	
		scene::ITriangleSelector* level_selector;

		gui::IGUIFont* font;
	
};


void swplayer::init(IrrlichtDevice *dev, IVideoDriver* driv,ISceneManager* sm,IGUIEnvironment* gui){
	device = dev;
	driver = driv;
	smgr = sm;
	guienv = gui;
	
	mirino = driver->getTexture("data/gui/mirino.bmp");
	l100 = driver->getTexture("data/gui/life/100.bmp");
	l80 = driver->getTexture("data/gui/life/80.bmp");
	l60 = driver->getTexture("data/gui/life/60.bmp");
	l50 = driver->getTexture("data/gui/life/50.bmp");
	l30 = driver->getTexture("data/gui/life/30.bmp");
	l10 = driver->getTexture("data/gui/life/10.bmp");
	font = device->getGUIEnvironment()->getBuiltInFont();
}

void swplayer::camera(int x, int y, int z){
	// Creiamo la camera di gioco, la poszioniamo. Creiamo 1 risposta alle collisioni, la applichiamo alla camera
	cam_game = smgr->addCameraSceneNodeFPS(0,100.0f,300.0f);
	cam_game->setPosition(vector3df(x,y,z));
	cam_game->setFarValue(25000);
}

void swplayer::camera_sl(){
	cam_sleep = smgr -> addCameraSceneNode(0, vector3df(0,0,0), vector3df(0,0,0));
}

void swplayer::shoot(){
	if(bullets!=0){
		bullets--;
		vector3df start = cam_game->getPosition();
		vector3df end = (cam_game->getTarget() - start);
		end.normalize();
		start += end*5.0f;
		end = start + (end * cam_game->getFarValue());
	
		triangle3df triangle;
		line3d<f32> line(start, end);

		scene::ISceneNode* bullet = smgr->addBillboardSceneNode(0,core::dimension2d<f32>(5,5), start);

		bullet->setMaterialFlag(video::EMF_LIGHTING, false);
		bullet->setMaterialTexture(0, device->getVideoDriver()->getTexture("data/particle/shoot.bmp"));
		bullet->setMaterialType(video::EMT_TRANSPARENT_ADD_COLOR);
		
		f32 length = (f32)(end - start).getLength();
		const f32 speed = 1.6f;
		u32 time = (u32)(length / speed);

		ISceneNodeAnimator* anim = smgr->createFlyStraightAnimator(start, end, time);
		bullet->addAnimator(anim);	
		anim->drop();

		anim = smgr->createDeleteAnimator(time);
		bullet->addAnimator(anim);
		anim->drop();
	}

}
void swplayer::recarge(){
		if(carge!=0)
		{
			bullets = 5;
			carge--;
		}
}

void swplayer::show_life(){
	if(life==100){
		driver->draw2DImage(l100,core::position2d<s32>(10,490),core::rect<s32>(0,0,40,100),0,video::SColor(255,255,255,255), true);
	}
	
	if(life>=80){
		driver->draw2DImage(l80,core::position2d<s32>(10,490),core::rect<s32>(0,0,40,100),0,video::SColor(255,255,255,255), true);
	}
	
	if(life>=60){
		driver->draw2DImage(l60,core::position2d<s32>(10,490),core::rect<s32>(0,0,40,100),0,video::SColor(255,255,255,255), true);
	}
	
	if(life>=50){
		driver->draw2DImage(l50,core::position2d<s32>(10,490),core::rect<s32>(0,0,40,100),0,video::SColor(255,255,255,255), true);
	}
	
	if(life>=30){
		driver->draw2DImage(l30,core::position2d<s32>(10,490),core::rect<s32>(0,0,40,100),0,video::SColor(255,255,255,255), true);
	}
	
	if(life>=10){
		driver->draw2DImage(l10,core::position2d<s32>(10,490),core::rect<s32>(0,0,40,100),0,video::SColor(255,255,255,255), true);
	}
	
	else{
		driver->draw2DImage(l100,core::position2d<s32>(10,490),core::rect<s32>(0,0,40,100),0,video::SColor(255,255,255,255), true);
	}


}

void swplayer::show_bullets(){
font->draw(L"This is some text.",core::rect<s32>(130,10,300,50),video::SColor(255,255,255,255));	
}

void swplayer::show_mirino(){
	driver->draw2DImage(mirino,core::position2d<s32>(400,300),core::rect<s32>(0,0,5,5),0,video::SColor(255,255,255,255), true);
}

#endif

