// SteelWar
// Autore: dak (dak.netsons.org)
// Licenza CreativeCommons

#ifndef _SW_H_
#define _SW_H_

#include <irrlicht.h>
#include <iostream.h>
#include <stdio.h>


using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;

class steelwar : public IEventReceiver
{
	public:
		// Funzioni
		void init(int,int,bool,int);
		
		// Eventi tastiera
		virtual bool OnEvent(SEvent event);
	
		// Posizione mouse
		position2d<s32> pos;
	
		// Per irrlicht
		IrrlichtDevice *device;
		IVideoDriver* driver;
		ISceneManager* smgr;
		IGUIEnvironment* guienv;
	
		IGUIInOutFader* fader;
		
	
		bool key_shoot;
		bool key_recarge;
		bool key_jump;
		int key_weapon;
		bool play;
		bool first;

};

// Inizializziamo i device
void steelwar::init(int xa, int ya, bool fs, int bit){
	device = createDevice(EDT_OPENGL,dimension2d<s32>(xa,ya),bit,fs,false,false,this);
	driver = device->getVideoDriver();
	smgr = device->getSceneManager();
	guienv = device->getGUIEnvironment();
	device->setWindowCaption(L"SteelWar");

	key_shoot = key_recarge = key_jump = false;
	key_weapon = 2;
	fader = device->getGUIEnvironment()->addInOutFader();
}


// Evento tastiera
bool steelwar::OnEvent(SEvent event)
{
	if(!device){ return false; }
	if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_ESCAPE && event.KeyInput.PressedDown == false)
	{ 
		play = false;
	}
	

	if(event.EventType == EET_MOUSE_INPUT_EVENT && event.MouseInput.Event==EMIE_LMOUSE_PRESSED_DOWN){ 
		key_shoot = true;
		}
		
	
	if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_R && event.KeyInput.PressedDown == false){ 
		key_recarge = true;
		}
		
	if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_SPACE && event.KeyInput.PressedDown == false){ 
		key_jump = true;
		}
		
	/*if(event.EventType == EET_MOUSE_INPUT_EVENT && event.MouseInput.Event==EMIE_MOUSE_WHEEL){
		if(key_weapon!=6) { key_weapon+=1; }

		else{ key_weapon = 1; }
		}*/
		
	// Cambio armi
	/*// Disabilitato per mancanza di armi :D
	if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_1 && event.KeyInput.PressedDown == false){
		key_weapon = 1; 
	}
	
	if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_2 && event.KeyInput.PressedDown == false){
		key_weapon = 2; 
	}
	
	if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_3 && event.KeyInput.PressedDown == false){
		key_weapon = 3; 
	}
	
	if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_4 && event.KeyInput.PressedDown == false){
		key_weapon = 4; 
	}
	
	if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_5 && event.KeyInput.PressedDown == false){
		key_weapon = 5; 
	}*/
		
return false;
}


#endif

