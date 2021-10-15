import pygame

class sfx():
	def __init__(self,gui):
		self.gui      = gui
		self.black    = (0,0,0)
		self.red      = (230,0,0)
		self.surf     = pygame.Surface((self.gui.width,self.gui.height))
		self.alphaI   = 100
		self.ftbInit  = False
		self.fiInit   = False

	def fadeToBlack(self,gameState,inc=5):
		""" increments an index related to alpha"""
		

		#--------Init

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
		if(self.alphaI>254):self.alphaI = 255

	def fadeIn(self,gameState,inc=5):
		""" increments an index related to alpha"""
		
		#--------Init

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