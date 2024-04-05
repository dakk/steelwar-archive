#include <irrlicht.h>
#include <raknet/PacketEnumerations.h>
#include <raknet/RakNetworkFactory.h>
#include <raknet/NetworkTypes.h>
#include <raknet/RakClientInterface.h>
#include <raknet/BitStream.h>

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream.h>

using namespace irr;
using namespace core;
using namespace scene;
using namespace video;

const unsigned char PACKET_ID_LINE = 100;

class ClientConnection
{
public:
    ClientConnection(char * serverIP, char * portString)
    : client(NULL)
    {
        client = RakNetworkFactory::GetRakClientInterface();
        
        client->Connect(serverIP, atoi(portString), 0, 0, 0);
    }
    
    ~ClientConnection()
    {
        client->Disconnect(300);
        RakNetworkFactory::DestroyRakClientInterface(client);
    }
    
    void AddLineLocal(s32 x1, s32 y1, s32 x2, s32 y2)
    {
        line2d<s32> myLine(x1, y1, x2, y2);
        
        lineList.push_back(myLine);
    }
    
    void SendLineToServer(s32 x1, s32 y1, s32 x2, s32 y2)
    {
        RakNet::BitStream dataStream;
        
        dataStream.Write(PACKET_ID_LINE);
        dataStream.Write(x1);
        dataStream.Write(y1);
        dataStream.Write(x2);
        dataStream.Write(y2);
        
        client->Send(&dataStream, HIGH_PRIORITY, RELIABLE_ORDERED, 0);
    }
    
    list<line2d<s32> > * GetLineList()
    {
        return &lineList;
    }
    
    void DrawLines(IVideoDriver * irrVideo)
    {
        list<line2d<s32> >::Iterator it = lineList.begin();
    
        for(; it != lineList.end(); ++it) {
            line2d<s32> currentLine = (*it);
            position2d<s32> start = position2d<s32>(currentLine.start.X, currentLine.start.Y);
            position2d<s32> end = position2d<s32>(currentLine.end.X, currentLine.end.Y);
        
            irrVideo->draw2DLine(start, end);
        }
    }

    void ListenForPackets()
    {
        Packet * p = client->Receive();
        
        if(p != NULL) {
	 cout<<p<<"\n";
            HandlePacket(p);
            
            client->DeallocatePacket(p);
        }
    }
    
    void HandlePacket(Packet * p)
    {
        RakNet::BitStream dataStream((unsigned char*)p->data, p->length, false);
        unsigned char packetID;
    
        dataStream.Read(packetID);
    
        switch(packetID) {
        case PACKET_ID_LINE:
            int x1, y1, x2, y2;
        
            dataStream.Read(x1);
            dataStream.Read(y1);
            dataStream.Read(x2);
            dataStream.Read(y2);
        
            AddLineLocal(x1, y1, x2, y2);
        break;
        }
    }
    
private:
    RakClientInterface * client;
    list<line2d<s32> > lineList;
};

class ChalkboardEventReceiver : public IEventReceiver
{
public:
    ChalkboardEventReceiver(ClientConnection * c) 
    : mouseDown(false), connection(NULL)
    {
        connection = c;
    }
    
    bool OnEvent(SEvent event)
    {
        if(event.EventType == EET_MOUSE_INPUT_EVENT) {
            if(event.MouseInput.Event == EMIE_LMOUSE_PRESSED_DOWN) {
                x = event.MouseInput.X;
                y = event.MouseInput.Y;
                mouseDown = true;
                
                return true;
            }
            else if(event.MouseInput.Event == EMIE_LMOUSE_LEFT_UP) {
                connection->AddLineLocal(x, y, event.MouseInput.X, event.MouseInput.Y);
                connection->SendLineToServer(x, y, event.MouseInput.X, event.MouseInput.Y);
                mouseDown = false;
                
                return true;
            }
            else if(mouseDown && event.MouseInput.Event == EMIE_MOUSE_MOVED) {
                connection->AddLineLocal(x, y, event.MouseInput.X, event.MouseInput.Y);
                connection->SendLineToServer(x, y, event.MouseInput.X, event.MouseInput.Y);
                x = event.MouseInput.X;
                y = event.MouseInput.Y;
                
                return true;
            }
        }
        
        return false;
    }
    
    
protected:
    s32 x, y;
    bool mouseDown;
    ClientConnection * connection;
};

int main()
{
    ClientConnection myConnection("127.0.0.1", "123456");
    ChalkboardEventReceiver myReceiver(&myConnection);
    IrrlichtDevice * irrDevice = createDevice(EDT_SOFTWARE, dimension2d<s32>(300,300));
    IVideoDriver * irrVideo = irrDevice->getVideoDriver();

    irrDevice->setEventReceiver(&myReceiver);
    
    while(irrDevice->run()) {
  
        irrVideo->beginScene(true, true, SColor(0,0,0,0));
            myConnection.DrawLines(irrVideo);
        irrVideo->endScene();
     
         myConnection.ListenForPackets();
    }
    
    irrDevice->setEventReceiver(NULL);
    
    irrDevice->drop();

    return 0;
}
