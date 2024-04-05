# zf
import sys
import random
import math
import os
import getopt
import pygame
from pygame.locals import *

ver = '0.1'
pygame.init()
pygame.display.set_caption('Steelwar '+ver)
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
#pygame.FULLSCREEN()
	


def load_png(name):
	fullname = os.path.join('men_data', name)
	try:
		image = pygame.image.load(fullname)
		if image.get_alpha() is None:
			image = image.convert()
		else:
			image = image.convert_alpha()
	except pygame.error, message:
       		print 'Impossibile caricare l\'immgagine:', fullname
       		raise SystemExit, message
	return image, image.get_rect()


class steelwar_intro:
	def __init__(self):
		self.first1=True
		self.second2=True
		
	def main(self):
		self.first()
		self.second()
		
		
		
	def first(self):
		img1, rect1 = load_png('steelwar_contr.png')
		while self.first1:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE: self.first1 = False
					if event.key == K_RETURN: self.first1 = False
					if event.key == K_SPACE: self.first1 = False
				elif event.type == pygame.QUIT: sys.exit()
			screen.blit(img1, rect1)
			pygame.display.flip()
			
			
	def second(self):
		img2, rect2 = load_png('steelwar_contr.png')
		while self.second2:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE: self.second2 = False
					if event.key == K_RETURN: self.second2 = False
					if event.key == K_SPACE: self.second2 = False
				elif event.type == pygame.QUIT: sys.exit()
			screen.blit(img2, rect2)
			pygame.display.flip()
		
		

		
	
#class steelwar_menu:
#	def __init__(self):
#		pygame.init()
#		pygame.font.init()
		

steelwar_intro = steelwar_intro()
#stellwar_menu = stellwar_menu()
steelwar_intro.main()