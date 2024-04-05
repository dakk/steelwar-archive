// SteelWar
// Autore: dak (dak.netsons.org)
// Licenza CreativeCommons

#ifndef _NET_H_
#define _NET_H_

#include <irrlicht.h>
#include <iostream.h>
#include <stdio.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h> 


using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;


class swnet
{
	public:
		void update();
		void init();								// Inizializza
		void connect();							// Connette
		void send();								// Invia
		void disconnect();							// Disconnette socket
		void socket(int,int,int);
		void adr_init(struct sockaddr_in *, int, long);	// Inizializza indirizzo
	
		int port; 		// Porta
		int sd;		// Descrittore del socket
		int error;		// Controllo della connessione
		
		struct sockaddr_in server_addr; 	// Indirizzo del server
		struct sockaddr_in mio_addr;		// Indirizzo del client
		int mio_addr_len;				// Dimensione client adress
		


		
		

};

void swnet::adr_init(struct sockaddr_in *indirizzo, int port, long IPaddr){
	/*indirizzo->sin_family = AF_INET;
	indirizzo->sin_port = htons((u_short) port);
	indirizzo->sin_addr.s_addr = IPaddr; 	*/
		int o;
}


void swnet::socket(int family, int type, int protocol){
	/*sd=socket(AF_INET,SOCK_STREAM,0);*/
	int o;
}

void swnet::init(){
	/*mio_addr_len = sizeof(mio_addr);	 	// Setta dimensione client adress*/
	port = 4000;
}

void swnet::connect(){
	/*addr_initialize(&server_addr, PORT, inet_addr(argv[1])); 
	sd=socket(AF_INET,SOCK_STREAM,0);
	error=connect(sd,(struct sockaddr*) &server_addr, sizeof(server_addr)); 
	if (error==0) 
	{ 
		printf("Ho eseguito la connessione\n"); 
		getsockname(sd, &mio_addr, &mio_addr_len); 
		printf("il mio port e': %d\n\n",ntohs(mio_addr.sin_port));
		close(sd);
	} 
	else printf("%s","\nErrore di connect\n\n"); 
	{
		close(sd);
	}*/

	
}

void swnet::send(){
	int o;
}

void swnet::disconnect(){
	int o;//close(sd);
}

void swnet::update(){
	int o;
	
}

#endif
