// SteelWar
// Autore: dak (dak.netsons.org)
// Licenza CreativeCommons

#include <iostream.h>
#include <cstdlib> 
#include <irrlicht.h>
#include <stdio.h>
#include <string.h>
#include "sw.h"
#include "map.h"
#include "player.h"


using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;

int main(){
	steelwar sw;
	swmap map;
	swplayer player;

	
	
	sw.play = true;
	sw.pres = true;
	sw.menu = true;
	sw.init(800,600,false,32);


	map.init(sw.device, sw.driver, sw.smgr, sw.guienv);
	player.init(sw.device, sw.driver, sw.smgr, sw.guienv);
	
	player.bullets = 5;
	player.carge = 5;
	player.life = 100;
	
	map.level();
	map.skybox(2);
	map.add_box(50,0,0,0);
	

	player.camera(0,80,0);
	player.camera_sl();
	
	player.cam_coll = sw.smgr->createCollisionResponseAnimator(map.level_selector, player.cam_game, core::vector3df(20,40,20),core::vector3df(0,-3,0),core::vector3df(0,50,0));
	player.cam_game->addAnimator(player.cam_coll);
	player.cam_coll->drop();

	
	while(sw.device->run() && sw.play)
	{
		sw.driver->beginScene(true, true, SColor(255,255,255,255));

		// Se il menu e' attivo, lo visualizziamo.
		if(sw.menu){ 
			if(sw.cambiato){
				sw.smgr->setActiveCamera(player.cam_sleep);
				sw.device->getCursorControl()->setVisible(true);
				sw.cambiato = false;
			}
			
			if(sw.click){ sw.click = false;	}
			if(sw.recarge){ sw.recarge = false; }
			sw.menu_lp(); 
		}
		
		// Altrimenti giochiamo!
		else{
			if(sw.cambiato){
				sw.smgr->setActiveCamera(player.cam_game);
				sw.device->getCursorControl()->setVisible(false);	
				sw.cambiato = false;
			}
			player.show_life();
			player.show_bullets();	
			player.show_mirino();

			if(sw.click){ player.shoot(); sw.click = false;	}
			if(sw.recarge){ player.recarge(); sw.recarge = false; }
			
				
		}
		
		sw.smgr->drawAll();
		sw.guienv->drawAll();
		sw.driver->endScene();
	}
	
	sw.device->drop();
	return 0;
}

