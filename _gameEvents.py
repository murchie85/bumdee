class processGameEvent():

	def __init__(self):
		self.eventState = None


	def processEvent(self,gs,gui):



		#----------Process Next Day
		if(gs.eventState == 'nextDay'):
			gui.debug('Going to Next Day')
			gs.nextDay()
			gs.eventState = 'animateNextDay'
		if(gs.eventState=='animateNextDay'):
			c = gui.fx.boxOut(gui,'gs.stage',inc=15)
			gui.hideExitButton = True
			if(c):
				gs.eventState = None
				gui.debug('Day complete')
				gui.hideExitButton = False

