import pygame as p
from pygame.locals import *
from sys import exit
import random as r
p.init()
tbg='treebg.png'
fruit='mango.png'
bhimb='bh.png'
screen=p.display.set_mode((0,0),0,32)
#l=p.image.load(hj).convert()
tbg=p.image.load(tbg).convert_alpha()
fruit=p.image.load(fruit).convert_alpha()
bhimb=p.image.load(bhimb).convert_alpha()
#l=p.transform.scale(l,(750,1450))
tbg=p.transform.scale(tbg,(100,60))
fruit=p.transform.scale(fruit,(750,1450))
while True:
	for event in p.event.get():
		if event.type==QUIT:
			exit()
		screen.blit(tbg,(0,0))
		screen.blit(bhimb,(200,500))
		p.display.update()