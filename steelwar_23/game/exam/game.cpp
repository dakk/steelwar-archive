#include <irrlicht.h>

using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;

#pragma comment(lib, "Irrlicht.lib")

int main()
{
// Crea il device video con risoluzione 800*600 in modalita' wide
IrrlichtDevice *device =
	  createDevice(video::EDT_SOFTWARE2,dimension2d<s32>(800,600),16,false,false,false, 0);

device->setWindowCaption(L"Battlefield GL Test");

IVideoDriver* driver = device->getVideoDriver();
ISceneManager* smgr = device->getSceneManager();
IGUIEnvironment* guienv = device->getGUIEnvironment();


//IGUIWindow* window = guienv->addWindow(rect<s32>(20, 100, 400, 900),false,L"Menu'"); 
IGUIImage* img = guienv->addImage(driver->getTexture("data/logo3.tga"),position2d<int>(10,10));


/*smgr->addSkyBoxSceneNode(
	driver->getTexture("./data/sky/0.bmp"),
	driver->getTexture("./data/sky/0.bmp"),
	driver->getTexture("./data/sky/0.bmp"),
	driver->getTexture("./data/sky/0.bmp"),
	driver->getTexture("./data/sky/0.bmp"),
	driver->getTexture("./data/sky/0.bmp"));
*/



smgr->addCameraSceneNode(0, vector3df(0,30,-40), vector3df(0,5,0));




while(device->run())
{
	driver->beginScene(true, true, SColor(255,255,255,255));
	smgr->drawAll();
	guienv->drawAll();
	driver->endScene();
}

device->drop();
return 0;

}
