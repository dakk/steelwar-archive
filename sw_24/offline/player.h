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
		// Inizializza la libreria
		void init(IrrlichtDevice*, IVideoDriver*,ISceneManager*,IGUIEnvironment*);
	
		// Funzioni
		void camera(int,int,int);		// Crea la camera
		void weapon();				// Crea l'arma
		void shoot();					// Funzione sparo
		void recarge();				// Funzione ricarica
		void show_life();				// Visualizza la vita
		void show_bullets();			// Visualizza i bullets residui
		void show_mirino();				// Mostra il mirino
		void show_fps();				// Mostra fps
		void show_team();				// Mostra team
		void jump();					// Salto
		void ch_weapon(int);			// Cambio arma
		void bullet_reset();				// Restore proiettili e caricatori
		void show_weapon();			// Mostra tipo di arma

		
		// Variabili
		int bullets;					// Proiettili
		int carge;					// Caricatori
		int life;						// Vita
		int fps;						// Fps
		
		int we1;
		int we11;
		int we2;
		int we21; 
		int we3;
		int we31;
		int we4;
		int we41;
		int we5;
		int we51;
	
		int cu_weapon;				// Current weapon
		
		// 1 = pistola    2 = mitragliatore  3 = fucile   4 = granate   5 = coltello
		// Americani
		// 1 = colt		2 = thompson	3 = m1 garand	4 = grenade		5 = knife
		// Tedeski
		// 1 = p38	2= mp40		3 = kar98		4 = stelgranade	5 = knife
		char vs_team;					// Team avversario
		char cu_team;					// Team corrente
		// 1 = americani	2 = tedeski	3 = Russo	4 = Giapponese	5 = Italiano	6 = Francese
	
		bool play;
		bool first;

	
		stringw gui_buf;				// Stringa per la gui, usata per tutto
	
		// Per irrlicht
		IrrlichtDevice *device;
		IVideoDriver* driver;
		ISceneManager* smgr;
		IGUIEnvironment* guienv;
	
		// Vita
		ITexture* l100;
		ITexture* l80;
		ITexture* l60;
		ITexture* l50;
		ITexture* l30;
		ITexture* l10;
		
		// Mirino
		ITexture* mirino;
		
		ITexture* bul;
		ITexture* bulmrk;
		ITexture* smoke;
		
		// Per la camera
		ICameraSceneNode* cam_game;
		scene::ISceneNodeAnimator* cam_coll;
		scene::ITriangleSelector* level_selector;
		ISceneNode* light_cam;
		IAnimatedMeshSceneNode* weapon_node;
		// Armi
		IAnimatedMesh* thompson;
		video::ITexture* thompsont;
		
		
		IAnimatedMesh* bracc;
		video::ITexture* bracct;
		IAnimatedMeshSceneNode* brac;
		
		// Font
		IGUIFont* font;
		

	
};

// Inizializza la classe
void swplayer::init(IrrlichtDevice *dev, IVideoDriver* driv,ISceneManager* sm,IGUIEnvironment* gui){
	device = dev;
	driver = driv;
	smgr = sm;
	guienv = gui;
	
	thompson = smgr->getMesh("data/model/weapon/usa/thompson.3ds"); 
	
	
	bullet_reset();
	cu_weapon = 2;
	bullets = 27;
	carge = 3;
	
	bracc = smgr->getMesh("data/model/braccio.3ds");
	bracct = driver->getTexture("data/texture/braccio.png");
	
	smoke = driver->getTexture("data/particle/smoke.png");
	bul = driver->getTexture("data/particle/shoot.bmp");
	bulmrk = driver->getTexture("data/particle/bulletmrk.tga");
	mirino = driver->getTexture("data/gui/mirino.png");
	l100 = driver->getTexture("data/gui/life/100.bmp");
	l80 = driver->getTexture("data/gui/life/80.bmp");
	l60 = driver->getTexture("data/gui/life/60.bmp");
	l50 = driver->getTexture("data/gui/life/50.bmp");
	l30 = driver->getTexture("data/gui/life/30.bmp");
	l10 = driver->getTexture("data/gui/life/10.bmp");
	font = device->getGUIEnvironment()->getFont("data/font/guifont1.bmp");
	
	//weapon_node = smgr->addAnimatedMeshSceneNode(thompson);
}


void swplayer::bullet_reset(){
	we1 = 7; we11 = 4;
	we2 = 27; we21 = 3;
	we3 = 11; we31 = 3;
	we4 = 4; we41 = 0;
	we5 = 0; we51 = 0;
	 

}

// Crea la camera di gioco, la poszioniamo. Creiamo 1 risposta alle collisioni, la applichiamo alla camera
void swplayer::camera(int x, int y, int z){
	
	// Wasd movement
	SKeyMap keyMap[8];
	
	keyMap[1].Action = EKA_MOVE_FORWARD;
	keyMap[1].KeyCode = KEY_KEY_W;
	
	keyMap[3].Action = EKA_MOVE_BACKWARD;
	keyMap[3].KeyCode = KEY_KEY_S;
	
	keyMap[5].Action = EKA_STRAFE_LEFT;
	keyMap[5].KeyCode = KEY_KEY_A;
	
	keyMap[7].Action = EKA_STRAFE_RIGHT;
	keyMap[7].KeyCode = KEY_KEY_D; 
	
	
	//cam_game = smgr->addCameraSceneNodeFPS(0,100.0f,300.0f);
	cam_game = smgr->addCameraSceneNodeFPS(0,100.0f,300.0f,-1, keyMap, 8);
	cam_game->setPosition(vector3df(x,y,z));
	cam_game->setFarValue(25000);
	light_cam = smgr->addLightSceneNode(0, core::vector3df(0,0,0), video::SColorf(1.0f, 1.0f, 1.0f, 1.0f), 8000.0f);
	light_cam->setParent(cam_game);	
	cam_coll = smgr->createCollisionResponseAnimator(level_selector, cam_game, core::vector3df(20,40,20),core::vector3df(0,-3,0),core::vector3df(0,50,0));
	cam_game->addAnimator(cam_coll);
	cam_coll->drop();	
	
	brac = smgr->addAnimatedMeshSceneNode(bracc);
	brac->setMaterialTexture(0, bracct );
	brac->setScale(vector3df(1.5,1.5,1.5));
	brac->setRotation(vector3df(90,0.0,270));
	brac->setPosition(vector3df(1,-7,8));
	brac->setParent(cam_game);
}

// Arma
void swplayer::weapon(){
	// Americani
	if(cu_team=='1'){
		// Colt
		if(cu_weapon==1){ 
			bullets = we1;
			carge = we11;
			//if(!first){ weapon_node->drop(); }
			//else{ first = false; }
		}
		// Thompson
		if(cu_weapon==2){ 
			bullets = we2;
			carge = we21;
			//if(!first){ weapon_node->drop(); }
			//else{ first = false; }
			weapon_node = smgr->addAnimatedMeshSceneNode(thompson);
			weapon_node->setScale(vector3df(7.0,7.0,7.0));
			weapon_node->setRotation(vector3df(90,-4.0,0));
			weapon_node->setPosition(vector3df(3,-7,10));
			//weapon_node->setMaterialFlag(EMF_NORMALIZE_NORMALS, false);
			weapon_node->setParent(cam_game);
			
		}
		if(cu_weapon==3){ 
			bullets = we3;
			carge = we31;
			//if(!first){ weapon_node->drop(); }
			//else{ first = false; }
		}
		if(cu_weapon==4){ 
			bullets = we4;
			carge = we41;
			//if(!first){ weapon_node->drop(); }
			//else{ first = false; }
		}
		
		if(cu_weapon==5){ 
			bullets = we5;
			carge = we51;
			//if(!first){ weapon_node->drop(); }
			//else{ first = false; }
		}
		
		
	}

	
	// Per riflessione speculare dell'arma
	//weapon_node->getMaterial(0).Shininess=20.0f;//shl_dimension_weapon; 
	//weapon_node->getMaterial(0).SpecularColor.set(200,50,150,200);//shl_color_weapon; 

}

// Salto
void swplayer::jump(){
	// Provisorio
	cam_game->setPosition(cam_game->getPosition() + vector3df(0,90.0,0));
}

// Cambia arma
void swplayer::ch_weapon(int w){
	if(w!=cu_weapon){ 
		if(cu_weapon==1){ we1 =  bullets; we11 = carge; }
		if(cu_weapon==2){ we2 =  bullets; we21 = carge; }
		if(cu_weapon==3){ we3 =  bullets; we31 = carge; }
		if(cu_weapon==4){ we4 =  bullets; we41 = carge; }
		if(first){ cu_weapon = 2; first = false; }
		else{ cu_weapon = w; }
		weapon();
	}
}

// Sparo
void swplayer::shoot(){
	// Se l'arma è il mitra
	if(cu_team=='1'){
	if(cu_weapon==2){ 
		// Se abbiamo proiettili
		if(bullets!=0){
			bullets=bullets-1;
			vector3df start = cam_game->getPosition();
			vector3df end = (cam_game->getTarget() - start);
			end.normalize();
			start += end*20.0f;
			end = start + (end * cam_game->getFarValue());
		
			triangle3df triangle;
			line3d<f32> line(start, end);
			
			vector3df intersection;
			
			/*
			vector3df pos = weapon_node->getPosition();
			ISceneNodeAnimator* rinculo = smgr->createFlyStraightAnimator(pos,pos-vector3df(0,-4,10),400,false);
			weapon_node->addAnimator(rinculo);
			rinculo->drop();
						
			ISceneNodeAnimator* rinculoa = smgr->createFlyStraightAnimator(pos-vector3df(0,-4,10),pos,400,false);
			weapon_node->addAnimator(rinculoa);
			rinculoa->drop();*/
			
			// Se colpisce la mappa, facciamo il fumo.
			if (smgr->getSceneCollisionManager()->getCollisionPoint(line, level_selector, intersection, triangle))
			{
				// Fumo del colpo
				vector3df normale = triangle.getNormal();
				normale.setLength(10);
				
				ISceneNode* smokea = smgr->addBillboardSceneNode(0,core::dimension2d<f32>(15,25), intersection);
				smokea->setMaterialFlag(video::EMF_LIGHTING, false);
				smokea->setMaterialTexture(0, smoke);
				smokea->setMaterialType(video::EMT_TRANSPARENT_ADD_COLOR);
				ISceneNodeAnimator* sanim = smgr->createFlyStraightAnimator(intersection, intersection+normale,600);
				smokea->addAnimator(sanim);	
				sanim->drop();
				sanim = smgr->createDeleteAnimator(700);
				smokea->addAnimator(sanim);
				sanim->drop();
				
				
				// Buco del proiettile per 18 secondi
				ISceneNode* bumr = smgr->addBillboardSceneNode(0,core::dimension2d<f32>(10,10), start);
				bumr->setMaterialFlag(video::EMF_LIGHTING, false);
				bumr->setMaterialTexture(0, bulmrk);
				bumr->setMaterialType(EMT_TRANSPARENT_ALPHA_CHANNEL);
				
				vector3df buco = intersection+normale;
				ISceneNodeAnimator* sanim2 = smgr->createFlyStraightAnimator(buco,buco,18000);
				bumr->addAnimator(sanim2);	
				sanim2->drop();
				sanim2 = smgr->createDeleteAnimator(18000);
				bumr->addAnimator(sanim2);
				sanim2->drop();
		
			}

			ISceneNode* bullet = smgr->addBillboardSceneNode(0,core::dimension2d<f32>(5,5), start);

			bullet->setMaterialFlag(video::EMF_LIGHTING, false);
			bullet->setMaterialTexture(0, bul);
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
}
}

// Ricarica
void swplayer::recarge(){
	if(cu_weapon!=5){ 
		if(carge!=0)
		{
			if(cu_weapon==1){ bullets = 7; }
			if(cu_weapon==2){ bullets = 27; }
			if(cu_weapon==3){ bullets = 11; }
			if(cu_weapon==4){ bullets = 4; }
			carge=carge-1;
			
		}
	}
}

// Visualizza vita
void swplayer::show_life(){
	if(life>=10){
		driver->draw2DImage(l10,core::position2d<s32>(10,490),core::rect<s32>(0,0,40,100),0,video::SColor(255,255,255,255), true);
	}
	if(life>=30){
		driver->draw2DImage(l30,core::position2d<s32>(10,490),core::rect<s32>(0,0,40,100),0,video::SColor(255,255,255,255), true);
	}	
	if(life>=50){
		driver->draw2DImage(l50,core::position2d<s32>(10,490),core::rect<s32>(0,0,40,100),0,video::SColor(255,255,255,255), true);
	}	
	if(life>=60){
		driver->draw2DImage(l60,core::position2d<s32>(10,490),core::rect<s32>(0,0,40,100),0,video::SColor(255,255,255,255), true);
	}	
	if(life>=80){
		driver->draw2DImage(l80,core::position2d<s32>(10,490),core::rect<s32>(0,0,40,100),0,video::SColor(255,255,255,255), true);
	}	
	if(life==100){
		driver->draw2DImage(l100,core::position2d<s32>(10,490),core::rect<s32>(0,0,40,100),0,video::SColor(255,255,255,255), true);
	}	

}

// Visualizza proiettili residui
void swplayer::show_bullets(){
	if(cu_weapon==5){
		gui_buf = ""; 
	}
	if(bullets==0 && carge == 0){
		gui_buf = "Vuoto";
	}
	else{
	gui_buf = "";
	gui_buf += bullets;
	gui_buf += "\\";
	gui_buf += carge;
	}
	font->draw(gui_buf.c_str(),core::rect<s32>(60,570,300,50),video::SColor(255,255,255,255));

}

// Visualizza mirino
void swplayer::show_mirino(){
	driver->draw2DImage(mirino,core::position2d<s32>(390,290),core::rect<s32>(0,0,20,20),0,video::SColor(100,255,255,255), true);
}

// Visualizza fps
void swplayer::show_fps(){
	if(fps!=driver->getFPS()){
		gui_buf = "";
		gui_buf += driver->getFPS();
		gui_buf += " FPS";
	}
	font->draw(gui_buf.c_str(),core::rect<s32>(700,580,300,50),video::SColor(255,255,255,255));
}

// Visualizza squadra
void swplayer::show_team(){
	gui_buf = "";
	if(cu_team=='1'){
		gui_buf += "Americano";
	}
	if(cu_team=='2'){
		gui_buf += "Tedesco";
	}
	if(cu_team=='3'){
		gui_buf += "Russo";
	}
	if(cu_team=='4'){
		gui_buf += "Giapponese";
	}
	if(cu_team=='5'){
		gui_buf += "Italiano";
	}
	if(cu_team=='6'){
		gui_buf += "Francese";
	}	

	font->draw(gui_buf.c_str(),core::rect<s32>(5,5,300,50),video::SColor(255,255,255,255));
}

// Visualizza arma
void swplayer::show_weapon(){
	gui_buf = "";
	if(cu_weapon==1){
		gui_buf += "Pistola";
	}
	if(cu_weapon==2){
		gui_buf += "Mitragliatore";
	}
	if(cu_weapon==3){
		gui_buf += "Fucile";
	}
	if(cu_weapon==4){
		gui_buf += "Granate";
	}
	if(cu_weapon==5){
		gui_buf += "Coltello";
	}


	font->draw(gui_buf.c_str(),core::rect<s32>(650,5,300,50),video::SColor(255,255,255,255));
}


#endif

