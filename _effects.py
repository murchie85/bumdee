import pygame
from _draw       import *

class sfx():
	def __init__(self,gui):
		self.gui          = gui
		self.black        = (0,0,0)
		self.red          = (230,0,0)
		self.surf         = pygame.Surface((self.gui.width,self.gui.height))
		self.alphaI       = 100
		self.ftbInit      = False
		self.fiInit       = False
		self.gameState    = None

	def fadeOut(self,gameState,inc=5,alpha=254):
		""" increments an index related to alpha"""
		

		#--------Init
		complete = False
		if(self.gameState!=gameState):self.ftbInit=False
		if(self.ftbInit==False):
			self.alphaI = 0
			self.gameState = gameState
			self.ftbInit=True

		#------increment Alpha up

		self.surf.set_alpha(self.alphaI)
		self.surf.fill((0,0,0))
		self.gui.screen.blit(self.surf,(0,0))
		self.alphaI +=inc
		if(self.alphaI>alpha):self.alphaI = alpha
		if(self.alphaI>=alpha): complete = True

		return(complete)



	def fadeIn(self,gameState,inc=5,skip=False):
		""" increments an index related to alpha"""
		
		#--------Init
		complete = False

		if(self.gameState!=gameState):self.ftbInit=False
		if(self.fiInit==False):
			self.alphaI = 255
			self.gameState = gameState
			self.fiInit=True

		#------increment Alpha down

		self.surf.set_alpha(self.alphaI)
		self.surf.fill((0,0,0))
		self.gui.screen.blit(self.surf,(0,0))
		self.alphaI -=inc
		if(self.alphaI<1):self.alphaI = 0
		if(self.alphaI<1): complete = True

		if(skip): self.alphaI = 0

		return(complete)



	def hurt(self,gameState,gui,inc=10):
		""" increments an index related to alpha"""
		

		#--------Init

		if(self.gameState!=gameState):self.ftbInit=False
		if(self.ftbInit==False):
			self.alphaI    = 0
			self.showTxt   = False
			self.shake     = False
			self.shakeDir  = 'r'
			self.shakeTime = 0
			self.rx        = 0
			self.ry        = 0
			self.gameState = gameState
			self.ftbInit   =True

		if(self.shake):gui.screen.fill((0,0,0))
		#------increment Alpha up

		self.surf.set_alpha(self.alphaI)
		
		rect = pygame.draw.rect(self.surf, (128,0,0), [self.rx, self.ry, 1500,850])
		self.gui.screen.blit(self.surf,(self.rx,self.ry,))
		self.alphaI +=inc
		if(self.alphaI>254):self.alphaI  = 255
		if(self.alphaI>254):self.shake   = True
		if(self.alphaI>100):self.showTxt = True

		if(self.showTxt):
			drawText(gui.screen,gui.bigFont,"You took Damage",0.4*gui.width,gui.height/3,(255,255,255),pos=(gui.mx,gui.my))
			drawText(gui.screen,gui.font,"HP - 10%",0.45*gui.width,gui.height/2,(255,255,255),pos=(gui.mx,gui.my))

		if(self.shake):
			self.shakeTime +=1
			if(self.shakeTime>10): self.shake = False
			if(self.shakeDir == 'r'): self.rx += 40
			if(self.shakeDir == 'l'): self.rx -= 40
			if(self.rx>50): self.shakeDir = 'l'
			if(self.rx<-50): self.shakeDir = 'r'

