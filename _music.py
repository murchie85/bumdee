import pygame

class music():
	def __init__(self, tune=None,state='stopped'):
		self.tune  = tune
		self.state = state

	def play(self,tune,pos=None):
		self.tune = tune
		print('playing ' + str(tune))
		if(self.state=='playing'):
			self.stop()
			return()
		if(self.state=='stopped'):
			pygame.mixer.init()
			pygame.mixer.music.load(tune)
			pygame.mixer.music.play()
			if(pos):
				pygame.mixer.music.pause()
				pygame.mixer.music.set_pos(pos)
				pygame.mixer.music.unpause()
			self.state = 'playing'
	def stop(self):
		if(self.state=='playing'):
			pygame.mixer.music.stop()
			self.state= 'stopped'