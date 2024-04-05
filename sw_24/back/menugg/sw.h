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
		void menu_lp();
		
		virtual bool OnEvent(SEvent event);
	
		// Posizione mouse
		position2d<s32> pos;
	
		// Per irrlicht
		IrrlichtDevice *device;
		IVideoDriver* driver;
		ISceneManager* smgr;
		IGUIEnvironment* guienv;

		// Immagini
		video::ITexture* men_img;
		video::ITexture* men_img_single;
		video::ITexture* men_img_multy;
		video::ITexture* men_img_host;
		video::ITexture* men_img_option;
		
		video::ITexture* pres_img;
		
		
		bool play;
		bool menu;
		bool menu_single;
		bool menu_multy;
		bool menu_option;
		bool menu_host;
		
		bool click;
		bool recarge;
		bool pres;
		
		bool cambiato;

		
};

// Inizializziamo i device
void steelwar::init(int xa, int ya, bool fs, int bit){
	device = createDevice(EDT_OPENGL,dimension2d<s32>(xa,ya),bit,fs,false,false,this);
	driver = device->getVideoDriver();
	smgr = device->getSceneManager();
	guienv = device->getGUIEnvironment();
	device->setWindowCaption(L"SW");
	
	men_img = driver->getTexture("data/menu/menu.png");
	men_img_single = driver->getTexture("data/menu/single.png");
	men_img_multy = driver->getTexture("data/menu/multy.png");
	men_img_host = driver->getTexture("data/menu/host.png");
	men_img_option = driver->getTexture("data/menu/option.png");
	
	pres_img = driver->getTexture("data/sw_logo.png");

	
	menu = true;
	menu_single = false;
	menu_multy = false;
	menu_option = false;
	menu_host = false;
	pres = true;
	click = false;
	recarge = false;
}

bool steelwar::OnEvent(SEvent event)
{
	if(!device){ return false; }
	if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_ESCAPE && event.KeyInput.PressedDown == false)
	{ 
		if(!menu){ 
			menu = true; 
			cambiato = true; 
			}
		else{ 
			menu = false; 
			cambiato = true; 
			}

	}
	
	if(pres){
		if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_RETURN && event.KeyInput.PressedDown == false)
		{ pres = false; }
	}
	
	
	if(!menu && !pres){
		if(event.EventType == EET_MOUSE_INPUT_EVENT && event.MouseInput.Event==EMIE_LMOUSE_PRESSED_DOWN){ 
			click = true;
			}
		
		if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_R && event.KeyInput.PressedDown == false){ 
			recarge = true;
			}
	}
	
	
	if(menu){
		if(event.EventType == EET_MOUSE_INPUT_EVENT && event.MouseInput.Event==EMIE_LMOUSE_PRESSED_DOWN){ 
			click = true;
			pos = device->getCursorControl()->getPosition();
			if( (pos.Y>=6) && (pos.Y<=22) && (pos.X>=6) && (pos.X<=102) ){ 
				cout<<"SinglePlayer\n"; 
				if(menu_single)	{ 	menu_single = false; 	}
				else			{	menu_single = true; 	}
			
				menu_multy = false;
				menu_option = false;
				menu_host = false;
			}
		
			if( (pos.Y>=6) && (pos.Y<=22) && (pos.X>=205) && (pos.X<=293) ){ 
				cout<<"MultyPlayer\n"; 
				if(menu_multy)		{ 	menu_multy = false; 	}
				else			{	menu_multy = true; 	}
				
				menu_single = false;
				menu_option = false;
				menu_host = false;
			}
		
			if( (pos.Y>=6) && (pos.Y<=22) && (pos.X>=402) && (pos.X<=483) ){ 
				cout<<"HostGame\n"; 
				if(menu_host)		{ 	menu_host = false; 	}
				else			{	menu_host = true; 	}
			
				menu_single = false;
				menu_multy = false;
				menu_option = false;
			}
		
			if( (pos.Y>=6) && (pos.Y<=22) && (pos.X>=593) && (pos.X<=647) ){ 
				cout<<"Option\n"; 
				if(menu_option)	{ 	menu_option = false; 	}
				else			{	menu_option = true; 	}
			
				menu_single = false;
				menu_multy = false;
				menu_host = false;
			}
		
			if( (pos.Y>=6) && (pos.Y<=22) && (pos.X>=756) && (pos.X<=793) ){ 
				device->closeDevice(); 
				cout<<"Quit\n"; 
			}
		}
	}

	return false;

}


void steelwar::menu_lp(){
	if(menu){
	if(pres){
		driver->draw2DImage(pres_img,core::position2d<s32>(0,0),core::rect<s32>(0,0,800,600),0,video::SColor(255,255,255,255), true);
	}
	
	if(pres==false){
		driver->draw2DImage(men_img,core::position2d<s32>(0,0),core::rect<s32>(0,0,800,600),0,video::SColor(255,255,255,255), true);
		if(menu_single){
			driver->draw2DImage(men_img_single,core::position2d<s32>(0,40),core::rect<s32>(0,0,800,540),0,video::SColor(255,255,255,255), true);
			}
		if(menu_multy){
			driver->draw2DImage(men_img_multy,core::position2d<s32>(0,40),core::rect<s32>(0,0,800,540),0,video::SColor(255,255,255,255), true);
			}
		if(menu_host){
			driver->draw2DImage(men_img_host,core::position2d<s32>(0,40),core::rect<s32>(0,0,800,540),0,video::SColor(255,255,255,255), true);
			}
		if(menu_option){
			driver->draw2DImage(men_img_option,core::position2d<s32>(0,40),core::rect<s32>(0,0,800,540),0,video::SColor(255,255,255,255), true);
			}
	}

}
}



#endif

