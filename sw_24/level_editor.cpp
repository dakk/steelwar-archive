// SteelWar
// Autore: dak (dak.netsons.org)
// Licenza CreativeCommons

#include <irrlicht.h>
#include <iostream.h>
#include <stdio.h>
#include "level_editor.h"


using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;

int main(){
	sweditor edit;	
	
	// Inizializziamo device, e variabili
	edit.play = false;
	edit.init(800,600,false,32);
	if(!edit.play){ return 0; }
	
	edit.draw_gui();
	
	edit.smgr->setActiveCamera(edit.cam_edit);
	edit.test = true;
	// Loop di rendering
	while(edit.device->run() && edit.play)
	{
		if(!edit.test){ edit.smgr->setActiveCamera(edit.cam_edit); }
		if(edit.test){ edit.smgr->setActiveCamera(edit.cam_try); }
			
		// Iniziamo scena
		edit.driver->beginScene(true, true, SColor(255,255,255,255));
		
		
		// Visualizziamo scena
		edit.smgr->drawAll();
		
		// Visualizziamo fps
		if(edit.fps!=edit.driver->getFPS()){ 
			edit.fps = edit.driver->getFPS(); 
			edit.buf = edit.fps;
			edit.buf += " FPS";
		}
		edit.font->draw(edit.buf.c_str(),core::rect<s32>(700,580,300,50),video::SColor(255,255,255,255));


		// Drawiamo gui e finiamo la scena
		edit.guienv->drawAll();
		edit.driver->endScene();
	}
	
	edit.device->drop();
	return 0;
}
