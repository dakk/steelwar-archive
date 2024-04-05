// SteelWar
// Autore: dak (dak.netsons.org)
// Licenza CreativeCommons

#include <iostream.h>
#include <string.h> 
#include <stdio.h>
#include <stdlib.h>
#include <irrlicht.h>
#include <fstream.h>



using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;


IrrlichtDevice *device = 0;

IGUIListBox* listbox = 0;
IGUICheckBox* fs = 0;
IGUICheckBox* pb = 0;
bool punkbuster;
bool fullscreen;
bool box;
int mn;


class menu : public IEventReceiver
{
	public:
		virtual bool OnEvent(SEvent event){
			if (event.EventType == EET_GUI_EVENT)
			{
			s32 id = event.GUIEvent.Caller->getID();
			IGUIEnvironment* env = device->getGUIEnvironment();
			switch(event.GUIEvent.EventType)
			{
			case EGET_BUTTON_CLICKED:
				if (id == 103)
				{
					device->closeDevice();
					return true;
				}
				
				if(id==101){
					if(box!=true){ listbox = env->addListBox(rect<s32>(10, 55, 440, 490)); box = true; }
					listbox->clear();
					mn = 1;
					FILE * ff;
					ff = fopen("data/maps/map.ls","r");
					char buf[50];
					char buf2[50];
					stringw map;
					bool a = true;
					
				
					
					while(a!=false){
						memset(buf,50,0);
						memset(buf2,50,0);
						map = "";
						fscanf(ff, "%50s", buf);
						if(strcmp(buf,buf2)==0){ a = false; break; }
						for(int o = 0; o!=50; o++){
							buf2[o]=buf[o];
						}
						map = buf;
						listbox->addItem(map.c_str());
					}
					
					fclose(ff);
				}
				
				if(id==102){
					if(box!=true){ listbox = env->addListBox(rect<s32>(10, 55, 440, 490)); box = true; }
					listbox->clear();
					mn = 2;
					
					FILE * ff;
					ff = fopen("data/server.ls","r");
					char buf[50];
					char buf2[50];
					stringw map;
					bool a = true;
					
				
					
					while(a!=false){
						memset(buf,50,0);
						memset(buf2,50,0);
						map = "";
						fscanf(ff, "%50s", buf);
						if(strcmp(buf,buf2)==0){ a = false; break; }
						for(int o = 0; o!=50; o++){
							buf2[o]=buf[o];
						}
						map = buf;
						listbox->addItem(map.c_str());
					}
					
					fclose(ff);					
				}
				
	
				if (id == 104)
				{
					fullscreen = fs->isChecked();
					punkbuster = pb->isChecked();
					
					int m = listbox->getSelected();
					if(m==-1){ return false; }
					
					if(mn==2){
						int oa;
					}
					if(mn==1){
						FILE * ff;
						ff = fopen("data/maps/map.ls","r");
						char buf[50];
						char buf2[55];
						bool a = true;
						stringw map;
						int aa = 0;
					
						while(a!=false){
							map = "";
							map += "./sw data/maps/";
							memset(buf,50,0);
							fscanf(ff, "%50s", buf);
							map += buf;
							map += " 1 2 ";
							if(fullscreen==true){ map += "t"; }
							if(fullscreen!=true){ map += "f"; }
							
							if(aa==m){ 
								a = false;
								for(int u = 0; u<55; u++){ buf2[u] = map.c_str()[u]; }
								cout<<buf2<<"\n";
								device->drop();
								system(buf2); 
								
								}
								
							aa++;
						}
						
						fclose(ff);
					}
					
					
					return true;
				}
				
			}
			}
			return false;
		}
};

int main(){
	menu mn;

	
	device = createDevice(EDT_OPENGL, core::dimension2d<s32>(550, 500));
	video::IVideoDriver* driver = device->getVideoDriver();
	IGUIEnvironment* env = device->getGUIEnvironment();
	
	device->setEventReceiver(&mn);
	device->setWindowCaption(L"Steelwar");

	
	IGUIImage* img = env->addImage(
		driver->getTexture("data/menu/sw.jpg"),
		position2d<int>(-125,-50));

	env->addButton(rect<s32>(10,20,110,50), 0, 101, L"Single player");
	env->addButton(rect<s32>(120,20,210,50), 0, 102, L"Multi player");
	
	env->addButton(rect<s32>(450,20,540,50), 0, 103, L"Quit");
	
	env->addButton(rect<s32>(450,460,540,490), 0, 104, L"Gioca");
	
	
	fs = env->addCheckBox(fullscreen, core::rect<int>(450,50,540,80),0, 3, L"FullScreen");
	pb = env->addCheckBox(punkbuster, core::rect<int>(450,70,540,100),0, 3, L"PunkBuster");
	
	box = false;

	while(device->run() && driver){
			driver->beginScene(true, true, SColor(0,122,65,171));
			env->drawAll();
			driver->endScene();
	}
	device->drop();

	return 0;
}


