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
		bool key_chat;
		IGUIEditBox* chat;
		stringw chattx;
		int let;
		stringw nick;

};

// Inizializziamo i device
void steelwar::init(int xa, int ya, bool fs, int bit){
	device = createDevice(EDT_OPENGL,dimension2d<s32>(xa,ya),bit,fs,false,false,this);
	driver = device->getVideoDriver();
	smgr = device->getSceneManager();
	guienv = device->getGUIEnvironment();
	device->setWindowCaption(L"SteelWar");

	key_shoot = key_recarge = key_jump = key_chat = false;
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
	

	if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_F1  && event.KeyInput.PressedDown == false){ 
		if(!key_chat){ 
			key_chat = true; 
			chattx = nick+": ";
			let = 0;
			//chat = guienv->addEditBox(L"100.0", rect<s32>(20, 200, 250, 224), true, 0);
			return 0;
			
		}
		if(key_chat){ 
			key_chat = false; 
			//chat->drop();
			chattx = "";
			return 0;
		
		}	
		
	
	}
	
	if(key_chat){
		if(let<=53){
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_SPACE && event.KeyInput.PressedDown == false){ chattx += " "; let++; }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_A && event.KeyInput.PressedDown == false){ chattx += "A"; let++; }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_B && event.KeyInput.PressedDown == false){ chattx += "B"; let++; }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_C && event.KeyInput.PressedDown == false){ chattx += "C"; let++; }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_D && event.KeyInput.PressedDown == false){ chattx += "D"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_E && event.KeyInput.PressedDown == false){ chattx += "E"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_F && event.KeyInput.PressedDown == false){ chattx += "F"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_G && event.KeyInput.PressedDown == false){ chattx += "G"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_H && event.KeyInput.PressedDown == false){ chattx += "H"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_I && event.KeyInput.PressedDown == false){ chattx += "I"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_L && event.KeyInput.PressedDown == false){ chattx += "L"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_M && event.KeyInput.PressedDown == false){ chattx += "M"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_N && event.KeyInput.PressedDown == false){ chattx += "N"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_O && event.KeyInput.PressedDown == false){ chattx += "O"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_P && event.KeyInput.PressedDown == false){ chattx += "P"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_Q && event.KeyInput.PressedDown == false){ chattx += "Q"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_R && event.KeyInput.PressedDown == false){ chattx += "R"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_S && event.KeyInput.PressedDown == false){ chattx += "S"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_T && event.KeyInput.PressedDown == false){ chattx += "T"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_U && event.KeyInput.PressedDown == false){ chattx += "U"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_V && event.KeyInput.PressedDown == false){ chattx += "V"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_W && event.KeyInput.PressedDown == false){ chattx += "W"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_Z && event.KeyInput.PressedDown == false){ chattx += "Z"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_X && event.KeyInput.PressedDown == false){ chattx += "X"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_K && event.KeyInput.PressedDown == false){ chattx += "K"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_J && event.KeyInput.PressedDown == false){ chattx += "J"; let++;  }
			
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_F9 && event.KeyInput.PressedDown == false){ chattx += "?"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_F10 && event.KeyInput.PressedDown == false){ chattx += "!"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_F11 && event.KeyInput.PressedDown == false){ chattx += "."; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_F12 && event.KeyInput.PressedDown == false){ chattx += ","; let++;  }
			
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_1 && event.KeyInput.PressedDown == false){ chattx += "1"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_2 && event.KeyInput.PressedDown == false){ chattx += "2"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_3 && event.KeyInput.PressedDown == false){ chattx += "3"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_4 && event.KeyInput.PressedDown == false){ chattx += "4"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_7 && event.KeyInput.PressedDown == false){ chattx += "7"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_6 && event.KeyInput.PressedDown == false){ chattx += "6"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_7 && event.KeyInput.PressedDown == false){ chattx += "7"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_8 && event.KeyInput.PressedDown == false){ chattx += "8"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_9 && event.KeyInput.PressedDown == false){ chattx += "9"; let++;  }
			if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_0 && event.KeyInput.PressedDown == false){ chattx += "0"; let++;  }

		}
		if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_RETURN  && event.KeyInput.PressedDown == false){ key_chat = false;  chattx = ""; return 0;  }		
		
		
	}
	
	else{

		if(event.EventType == EET_MOUSE_INPUT_EVENT && event.MouseInput.Event==EMIE_LMOUSE_PRESSED_DOWN){ 
			key_shoot = true;
			}
			
		
		if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_KEY_R && event.KeyInput.PressedDown == false){ 
			key_recarge = true;
			}
		/*	
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
			}
		*/	
		if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_SPACE && event.KeyInput.PressedDown == false){ 
			key_jump = true;
			}
	}
	
		

		
return false;
}


#endif

