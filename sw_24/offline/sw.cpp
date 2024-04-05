// SteelWar
// Autore: dak (dak.netsons.org)
// Licenza CreativeCommons

#include <iostream.h>
#include <cstdlib> 
#include <irrlicht.h>
#include <stdio.h>
#include <string.h>
//#include <SDL/SDL.h>
//#include <SDL/SDL_mixer.h>
#include "sw.h"
#include "map.h"
#include "player.h"
#include "enemy.h"

using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;

int main(int argc, char* argv[]){
	steelwar sw;
	swmap map;
	swplayer player;
	swenemy enemy;

	bool fs;
	
	if(argv[4][0]=='t'){ fs = true; }
	else{ fs = false; }
	// Inizializziamo device, e variabili
	sw.init(800,600,fs,32);
	sw.play = true;
	player.play = true;
	map.play = true;
	
	
	// Inizializziamo map e player
	map.init(sw.device, sw.driver, sw.smgr, sw.guienv);
	player.init(sw.device, sw.driver, sw.smgr, sw.guienv);
	enemy.init(sw.device, sw.driver, sw.smgr, sw.guienv);
	
	// Settiamo armi al massimo
	player.life = 100;
	
	// Prima volta
	sw.first = true;
	player.first = true;
	
	// Scelta mappa
	//if(argc==3){
	map.load_map(argv[1]);
	player.cu_team=argv[2][0];
	player.vs_team=argv[3][0];
	map.skybox(2);
	//}
	/*else{
		map.load_map("data/maps/example.pk3");
		player.cu_team='1';
		map.skybox(2);
	}*/

	// Aggiungiamo camera e arma
	player.level_selector = map.level_selector;
	enemy.level_selector = map.level_selector;
	
	player.camera(0,80,0);
	player.weapon();
	

	// Rendiamo invisibile il cursore
	sw.device->getCursorControl()->setVisible(false);


	// Loop di rendering
	while(sw.device->run() && sw.play /*&& player.play*/ && map.play)
	{
		// Iniziamo scena
		sw.driver->beginScene(true, true, SColor(255,255,255,255));
		
		// Se e' il primo rendering, effetto fadein
		if(sw.first){
			sw.fader->fadeIn(7000);
			sw.first = false;
		}
		
		// Sparo e ricarica
		if(sw.key_shoot){ player.shoot(); sw.key_shoot = false;	}
		if(sw.key_recarge){ player.recarge(); sw.key_recarge = false; }	
		if(sw.key_jump){ player.jump(); sw.key_jump = false; }
		player.ch_weapon(sw.key_weapon);
		
		// Visualizziamo scena
		sw.smgr->drawAll();
		
		// Visualizziamo gui
		player.show_life();
		player.show_bullets();	
		player.show_mirino();
		player.show_fps();
		player.show_team();
		player.show_weapon();

		// Drawiamo gui e finiamo la scena
		sw.guienv->drawAll();
		sw.driver->endScene();
	}
	
	sw.device->drop();
	return 0;
}

