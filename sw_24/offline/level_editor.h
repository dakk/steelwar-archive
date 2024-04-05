// SteelWar
// Autore: dak (dak.netsons.org)
// Licenza CreativeCommons

#include <irrlicht.h>
#include <iostream.h>
#include <stdio.h>


using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;

class sweditor : public IEventReceiver
{
	public:
		// Funzioni
		void init(int,int,bool,int);
		void draw_gui();
		void draw_mesh(const c8*);
		
		// Eventi tastiera
		virtual bool OnEvent(SEvent event);
	
		// Posizione mouse
		position2d<s32> pos;
	
		// Font
		IGUIFont* font;
		stringw buf;
	
		int fps;
	
		// Per irrlicht
		IrrlichtDevice *device;
		IVideoDriver* driver;
		ISceneManager* smgr;
		IGUIEnvironment* guienv;
	
		bool play;						// La uso x controllare se l'editor è in esecuzione
		bool test; 
		
		IAnimatedMesh* m;
		IAnimatedMeshSceneNode* mn;
		

		
		ICameraSceneNode* cam_edit;
		ICameraSceneNode* cam_try;
};

// Inizializziamo i device
void sweditor::init(int xa, int ya, bool fs, int bit){
	device = createDevice(EDT_OPENGL,dimension2d<s32>(xa,ya),bit,fs,false,false,this);
	driver = device->getVideoDriver();
	smgr = device->getSceneManager();
	guienv = device->getGUIEnvironment();
	device->setWindowCaption(L"SteelWarEditor");

	cam_try = smgr->addCameraSceneNodeFPS();
	cam_try->setPosition(vector3df(0,0,0));
	cam_edit = smgr->addCameraSceneNode();
	cam_edit->setPosition(vector3df(0,0,0));
	
	font = device->getGUIEnvironment()->getFont("data/font/guifont1.bmp");
	fps = -1;
	play = true;
	
	smgr->addSkyBoxSceneNode(
		driver->getTexture("data/sky/2/up.jpg"),
		driver->getTexture("data/sky/2/dn.jpg"),
		driver->getTexture("data/sky/2/lf.jpg"),
		driver->getTexture("data/sky/2/rt.jpg"),
		driver->getTexture("data/sky/2/ft.jpg"),
		driver->getTexture("data/sky/2/bk.jpg")); 
		
}

// Eventi
bool sweditor::OnEvent(SEvent event)
{
	if(!device){ return false; }
	if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_ESCAPE && event.KeyInput.PressedDown == false)
	{ 
		play = false;
	}
	
	if(event.EventType == EET_KEY_INPUT_EVENT && event.KeyInput.Key == KEY_F1 && event.KeyInput.PressedDown == false)
	{ 
		if(test){ test = false; cam_edit->setPosition(cam_try->getPosition()); cam_edit->setRotation(cam_try->getRotation());} else{ test = true; }
	}
	
	if (event.EventType == EET_GUI_EVENT)
	{
		s32 id = event.GUIEvent.Caller->getID();

		switch(event.GUIEvent.EventType)
		{

			case EGET_BUTTON_CLICKED:
				// Esci
				if (id == 101)
				{
					device->closeDevice();
					return true;
				}

				
			case EGET_FILE_SELECTED:
			{
				IGUIFileOpenDialog* dialog = (IGUIFileOpenDialog*)event.GUIEvent.Caller;
				draw_mesh(stringc(dialog->getFilename()).c_str());
				break;
			}
				
			case EGET_MENU_ITEM_SELECTED:
			{
				IGUIContextMenu* menu = (IGUIContextMenu*)event.GUIEvent.Caller;
				s32 id = menu->getItemCommandId(menu->getSelectedItem());
				
				switch(id)
				{
					case 120:
						guienv->addFileOpenDialog(L"Seleziona il file da aprire.");
						break;
					case 121:
						device->closeDevice();
						break;
					
				}
			}		
				
		}

        }
		
return false;
}

void sweditor::draw_gui(){
	
	
	IGUIContextMenu* menu = guienv->addMenu();
	menu->addItem(L"Modelli", -1, true, true);
	menu->addItem(L"?", -1, true, true);
	
	gui::IGUIContextMenu* sottomenu;
	
	sottomenu = menu->getSubMenu(0);
	sottomenu->addItem(L"Importa modello", 120);
	sottomenu->addItem(L"Inserisci modello", 122);
	
	sottomenu = menu->getSubMenu(1);
	sottomenu->addItem(L"Esci", 121);

}

void sweditor::draw_mesh(const c8* filename){
	m = smgr->getMesh(filename);
	mn = smgr->addAnimatedMeshSceneNode(m);
	mn->setPosition(cam_edit->getPosition());
}


