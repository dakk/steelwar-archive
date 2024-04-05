// SteelWar
// Autore: dak (dak.netsons.org)
// Licenza CreativeCommons

#ifndef _NET_H_
#define _NET_H_

#include <irrlicht.h>
#include <iostream.h>
#include <stdio.h>
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

class swnet
{
	public:
		//const unsigned char PACKET_ID_LINE = 100;
		void connect();
		void update();

};

void swnet::connect(){
	
	//RakClientInterface * client;
	//RakNet::BitStream dataStream;
	// Connessione al server
	//client = RakNetworkFactory::GetRakClientInterface();
       // client->Connect("127.0.0.1", atoi("5115"), 0, 0, 0);	
	
}

void swnet::update(){
	
		/*dataStream.Write(PACKET_ID_LINE);
		
		pos = player.cam_game->getPosition();
		rot = player.cam_game->getRotation();
		
		cout<<fabsf(pos.X)<<" "<<fabsf(pos.Y)<<" "<<fabsf(pos.Z)<<" "<<fabsf(rot.X)<<" "<<fabsf(rot.Y)<<" "<<fabsf(rot.Z)<<"\n\n";
		dataStream.Write(14);
		dataStream.Write(fabsf(pos.X));
		dataStream.Write(fabsf(pos.Y));
		dataStream.Write(fabsf(pos.Z));
		dataStream.Write(fabsf(rot.X));
		dataStream.Write(fabsf(rot.Y));
		dataStream.Write(fabsf(rot.Z));
		
		client->Send(&dataStream, HIGH_PRIORITY, RELIABLE_ORDERED, 0);
		
		*/
}


#endif
