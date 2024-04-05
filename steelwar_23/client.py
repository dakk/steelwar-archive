# Steelwar
# Dak
# dak.freelabs.it
# GPL


#This source code is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License as published 
#by the Free Software Foundation; either version 2 of the License,
#or (at your option) any later version.

#This source code is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#Please refer to the GNU Public License for more details.

#You should have received a copy of the GNU Public License along with
#this source code; if not, write to:
#Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import pygtk						# Per le gtk
pygtk.require('2.0')					# Per le gtk
import gtk						# Per le gtk
from thread import *					# Per i thread
import thread						# Per i thread
import os						# Per l'osso
import socket
import time
import string

class sw_men:
	def __init__(self):
		self.ver = '0.1'
	
	def main(self):
		self.mainwin()
		self.mainmen()

	def esci(self, *args):
		gtk.main_quit()
		
	def mainwin(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.connect("destroy", self.esci)
		self.win.set_position(gtk.WIN_POS_CENTER)
		self.win.set_resizable(True)
		self.icon = self.win.render_icon(gtk.STOCK_FLOPPY, gtk.ICON_SIZE_BUTTON)
		self.win.set_icon(self.icon)
		self.win.set_title('Steelwar '+self.ver)
		self.win.set_border_width(0)
		
		# Inizializziamo e visualizziamo le box necessarie
		self.vbox_main = gtk.VBox(False, 0)
		self.vbox_main.set_border_width(0)
		self.win.add(self.vbox_main)
		
		self.hbox_main3 = gtk.HBox(False, 0)
		self.hbox_main3.set_border_width(0)
		self.vbox_main.add(self.hbox_main3)
		
		self.hbox_main = gtk.HBox(False, 0)
		self.hbox_main.set_border_width(0)
		self.vbox_main.add(self.hbox_main)

		# Bottoni 
		gtk.stock_add([(gtk.STOCK_QUIT, "Esci", 0, 0, "")])	
		gtk.stock_add([(gtk.STOCK_HOME, "Allenamento", 0, 0, "")])	
		gtk.stock_add([(gtk.STOCK_REFRESH, "Gioca", 0, 0, "")])	
		
		self.besc = gtk.Button("Esci", gtk.STOCK_QUIT)
		self.besc.connect("clicked", self.esci, None)
		self.hbox_main.add(self.besc)
		
		self.bof = gtk.Button("Allenamento", gtk.STOCK_HOME)
		self.bof.connect("clicked", self.noimp, None)
		self.hbox_main.add(self.bof)
		
		self.bon = gtk.Button("Online", gtk.STOCK_REFRESH)
		self.bon.connect("clicked", self.pl, None)
		self.hbox_main.add(self.bon)

		# img		
		self.scrv = gtk.Image()
		self.scrv.set_from_file('data/steelmain.png')
		self.scrv.show()
		self.hbox_main3.add(self.scrv)


		self.win.show()
		self.win.show_all()
		gtk.threads_enter()
		gtk.main()
		gtk.threads_leave()
		
	def pl(self, *args):
		self.win.destroy()

		

	def mainmen(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.connect("destroy", self.esci)
		self.win.set_position(gtk.WIN_POS_CENTER)
		self.win.set_resizable(True)
		self.icon = self.win.render_icon(gtk.STOCK_FLOPPY, gtk.ICON_SIZE_BUTTON)
		self.win.set_icon(self.icon)
		self.win.set_title('Steelwar '+self.ver)
		self.win.set_border_width(0)
		
		# Inizializziamo e visualizziamo le box necessarie
		self.vbox_main = gtk.VBox(False, 0)
		self.vbox_main.set_border_width(0)
		self.win.add(self.vbox_main)
		
		self.hbox_main3 = gtk.HBox(False, 0)
		self.hbox_main3.set_border_width(0)
		self.vbox_main.add(self.hbox_main3)
		
		self.hbox_main4 = gtk.HBox(False, 0)
		self.hbox_main4.set_border_width(0)
		self.vbox_main.add(self.hbox_main4)	
		
		
		
		self.hbox_main5 = gtk.HBox(False, 0)
		self.hbox_main5.set_border_width(0)
		self.vbox_main.add(self.hbox_main5)
		

		self.hbox_main2 = gtk.HBox(False, 0)
		self.hbox_main2.set_border_width(0)
		self.vbox_main.add(self.hbox_main2)
		
		self.hbox_main21 = gtk.HBox(False, 0)
		self.hbox_main21.set_border_width(0)
		self.vbox_main.add(self.hbox_main21)		
		
		self.hbox_main = gtk.HBox(False, 0)
		self.hbox_main.set_border_width(0)
		self.vbox_main.add(self.hbox_main)

		
		
		
		#self.pro = gtk.ProgressBar(adjustment=None)
		#self.pro.set_text('')
		#self.pro.set_fraction(0.0)
		#self.hbox_main21.add(self.pro)	
		
		# Bottoni 
		gtk.stock_add([(gtk.STOCK_QUIT, "Esci", 0, 0, "")])	
	
		gtk.stock_add([(gtk.STOCK_REFRESH, "Joina", 0, 0, "")])	
		
		self.besc = gtk.Button("Esci", gtk.STOCK_QUIT)
		self.besc.connect("clicked", self.esci, None)
		self.hbox_main.add(self.besc)
		
		self.bserver = gtk.Entry(max=0)
		self.bserver.set_text('Server')
		self.hbox_main5.add(self.bserver)
		
		self.bport = gtk.Entry(max=0)
		self.bport.set_text('Porta')
		self.hbox_main2.add(self.bport)
		

		gtk.stock_add([(gtk.STOCK_PREFERENCES, "Preferenze", 0, 0, "")])	
		
		self.bop = gtk.Button("Preferenze", gtk.STOCK_PREFERENCES)
		self.bop.connect("clicked", self.noimp, None)
		self.hbox_main4.add(self.bop)
		
		self.bnick = gtk.Entry(max=0)
		self.bnick.set_text('Nick')
		self.hbox_main2.add(self.bnick)

		self.bpas = gtk.Entry(max=0)
		self.bpas.set_text('Password')
		self.hbox_main2.add(self.bpas)
				
		self.bon = gtk.Button("Online", gtk.STOCK_REFRESH)
		self.bon.connect("clicked", self.connect, None)
		self.hbox_main.add(self.bon)

		# img		
		self.scrv = gtk.Image()
		self.scrv.set_from_file('data/steelmain.png')
		self.scrv.show()
		self.hbox_main3.add(self.scrv)


		self.win.show()
		self.win.show_all()
		gtk.threads_enter()
		gtk.main()
		gtk.threads_leave()
		
	def connect(self, *args):
		self.connect2()

	def connect2(self):
		self.server = self.bserver.get_text()
		self.port = self.bport.get_text()
		self.nick = self.bnick.get_text()
		self.passs = self.bpas.get_text()
		#self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#self.sock.connect((self.server, int(self.port)))

		
		
		#tmp = True
		
		#time.sleep(1)

		#self.sock.send(self.ver)

		#gtk.threads_enter()
		#self.pro.set_fraction(0.10)
		#self.pro.set_text('Versione inviata')
		#gtk.threads_leave()

		#print 'Versione inviata'
		#time.sleep(1)
		#rec = self.sock.recv(1024)
		#rec = rec[:-2]
		#self.mapp = rec[1:]
		#try: 
		#	f = open('map/'+self.mapp+'.3dt', 'r')
		#	f = open('map/'+self.mapp+'.ol', 'r')
		#except: 
		#	tmp = False
		#	print 'Map non trovata'

		#print 'Mappa ricevuta'
		#time.sleep(1)
		#self.sock.send(self.nick)
		#print 'Nick inviato'
		
		#if tmp == True:
		#	time.sleep(5)
		#	print 'Parametri accettati'
		#	self.sock.send('+JA+')
		#	
		fol = open('etc/tmpdata', 'w')
		fol.write(self.server+'\n'+self.port+'\n'+self.nick+'\n'+self.passs)
		fol.close()
		


	
	def noimp(self, *args): print 'ciao'

sw_men = sw_men()
sw_men.main()
