// SteelWar
// Autore: dak (dak.netsons.org)
// Licenza CreativeCommons

#include <raknet/PacketEnumerations.h>
#include <raknet/RakNetworkFactory.h>
#include <raknet/NetworkTypes.h>
#include <raknet/RakServerInterface.h>
#include <raknet/PacketEnumerations.h>
#include <raknet/RakClientInterface.h>
#include <raknet/BitStream.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream.h>
#include <irrlicht.h>

using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;

const unsigned char PACKET_ID_LINE = 100;

void SendLineToClients(RakServerInterface * server, PlayerID clientToExclude, int x1, int y1, int x2, int y2){
	RakNet::BitStream dataStream;
   
	dataStream.Write(PACKET_ID_LINE);
	dataStream.Write(x1);
	dataStream.Write(y1);
	dataStream.Write(x2);
	dataStream.Write(y2);
	    
	server->Send(&dataStream, HIGH_PRIORITY, RELIABLE_ORDERED, 0, clientToExclude, true);
}

void AnalizzaPacchetto(RakServerInterface * server, Packet * p){
	unsigned char packetID;
	RakNet::BitStream dataStream((unsigned char*)p->data, p->length, false);
	dataStream.Read(packetID);
	    
	cout<<packetID<<"\n";
	/*
	switch(packetID) {
		case PACKET_ID_LINE:*/
	int x1, y1, x2, y2;
	dataStream.Read(x1);
	dataStream.Read(y1);
	dataStream.Read(x2);
	dataStream.Read(y2);
	cout<<x1<<" "<<y1<<"\n";			
	/*
			SendLineToClients(server, p->playerId, x1, y1, x2, y2);
			break;
		default:
			break;
	}
	*/
}


int main(int argc, char* argv[])
{
	// Variabili
	RakServerInterface * server = RakNetworkFactory::GetRakServerInterface();
	Packet * packet = NULL;
	int port;				// Porta
	int max_pl;			// Player massimi
	bool play;			// Variabile di playing
	
	// Se gli argomenti sono di numero diverso da quelli richiesti, visualizzo il messaggio di help
	if(argc!=3){ cout<<"SteelWarServer: usa ./steelwar port maxplayer\n"; return 0; }
	
	// Imagazzina nelle variabili int, gli argomenti della main
	port = strtoul(argv[1], NULL, 0);
	max_pl = strtoul(argv[2], NULL, 0);
	
	// Se i player sono sopra la soglia supportata dal server, restituiamo il msg di errore
	if(max_pl>10){ cout<<"SteelWarServer: maxplayer troppo alto\n"; return 0; }
	
	// Messaggio iniziale
	cout<<"SteelWarServer...\nInizializzazione server\t\t\t";
	
	// Tentiamo di creare il server
	if(server->Start(max_pl, 0, 0, port)){ cout<<"[OK]\nBinding alla porta: "<<port<<"\t\t[OK]\n"; }
	else{ cout<<"[ER]\n"; return 0; }
	    

	while(play){
		// Riceve un pacchetto
		packet = server->Receive();
			
		// Se non è vuoto, allora
		if(packet != NULL) {
			AnalizzaPacchetto(server, packet);		// Analizziamo il pacchetto
			server->DeallocatePacket(packet);		// E lo disallochiamo
		}
	}
	
	// Chiusura server
	cout<<"Chiusura server";       
	server->Disconnect(300);
	RakNetworkFactory::DestroyRakServerInterface(server);        
	cout<<"\t\t\t[OK]";
}
