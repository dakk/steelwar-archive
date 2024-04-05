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
#include "enemy.h"
#include "net.h"
#include <math.h>


#include <raknet/PacketEnumerations.h>
#include <raknet/RakNetworkFactory.h>
#include <raknet/NetworkTypes.h>
#include <raknet/RakClientInterface.h>
#include <raknet/BitStream.h>


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
	swnet net;
	
	char fbuf[20];
	bool fs;
	bool netb;
	bool fx;
	FILE * ff;	
	stringw nick;


	ff = fopen("steelwar.conf","r");
	fscanf(ff, "%20s", fbuf);
	nick = fbuf;
	player.nick = fbuf;
	sw.nick = fbuf;	
	
	fscanf(ff, "%20s", fbuf);
	if(fbuf[0]=='T' || fbuf[0]=='t'){ fx = true; }
	else{ fx = false; }
	
	fscanf(ff, "%20s", fbuf);
	if(fbuf[0]=='T' || fbuf[0]=='t'){ fs = true; }
	else{ fs = false; }
	

	if(argv[4][0] == 't'){ netb = true; }
	else{ netb = false; }
	
	fclose(ff);



	

	// Inizializziamo device, e variabili
	sw.init(800,600,fs,32);
	sw.play = true;
	player.play = true;
	map.play = true;
	
	
	
	// Inizializziamo map e player
	map.init(sw.device, sw.driver, sw.smgr, sw.guienv);
	player.init(sw.device, sw.driver, sw.smgr, sw.guienv);
	enemy.init(sw.device, sw.driver, sw.smgr, sw.guienv);
	
	if(netb){ net.connect(); }
	
	// Settiamo armi al massimo
	player.life = 100;
	
	// Prima volta
	sw.first = true;
	player.first = true;
	
	// Scelta mappa
	if(!netb){
		map.load_map(argv[1]);
		player.cu_team=argv[2][0];
		player.vs_team=argv[3][0];
		map.skybox(2);
	}


	// Aggiungiamo camera e arma
	player.level_selector = map.level_selector;
	enemy.level_selector = map.level_selector;
	
	if(!netb){ player.camera(0,80,0); }
	map.cam_game = player.cam_game;
	if(fx){ map.lens_init(); }
	player.weapon();

	

	// Rendiamo invisibile il cursore
	sw.device->getCursorControl()->setVisible(false);
	
	vector3df pos, rot;
	// Loop di rendering
	while(sw.device->run() && sw.play /*&& player.play*/ && map.play)
	{
		// Iniziamo scena
		sw.driver->beginScene(true, true, SColor(255,255,255,255));
		
		map.update_cam(player.cam_game);
		
		if(fx){ map.update_lens(); }
		if(netb){ net.update(); }
		
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
		
		player.font->draw(sw.chattx.c_str(),core::rect<s32>(60,550,300,50),video::SColor(255,255,255,255));

		// Drawiamo gui e finiamo la scena
		sw.guienv->drawAll();
		sw.driver->endScene();
	}
	
	sw.device->drop();
	return 0;
}

