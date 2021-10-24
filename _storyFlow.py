class gameFlow():
	def __init__(self):
		self.substate = None
		print('Initialised')


	def checkDecisionFlow(self,gs,gui,phone,afterCommand=False):
		"""
		series of if/else check statements which 
		guides player through scenes and unlocks
		new events
		eventually might read from a file

		State tracked in GS for simplicity and easy load
		"""
		args = None
		command = ['desktop','pulltab','phone','afterCommand']
		

		# [1]--------begin sequence
		if(gs.stage=='day1-intro'):
			gs.eventState = 'cutScene'
			


			# allowed commands 
			command = ['desktop','pulltab','phone','afterCommand']


			# Fade in (run at the end )
			if(self.substate == None and afterCommand):
				c = gui.fx.fadeIn(gs.stage,inc=6)
				if(c): self.substate = 'intro'
			


			# =============TALKING Intorduction Message

			if(self.substate == 'intro'):
				message = [99,'Cheryl','Hi welcome to Dundee, I dont have time to fuck about so will get straight to the point. Times are tough and I dont have any jobs for you, but I put in a good word with some recycle centers - maybe you can help them out?','pics/characters/Phoebe.png']
				waitIntro = gs.stopWatch(1,'gameStartIntro',message)
				if(waitIntro):
					phone.messageUpdate(message,gui,gs,alert=True,scrollOverride='normal')
					self.substate = 'wait'
			
			# CONVO FINISHED
			if(self.substate == 'wait' and gui.smsScrollDialogue.finished==True):
					self.substate = 'flashingWidget'


			# ==============TALKING Introduce the widget and a job

			if(self.substate == 'flashingWidget'):
				command = ['desktop','pulltab','phone']

				# trigger the demo alert in pulltab widget
				args = 'demoWidgetAlert'
				message = [99,'Cheryl','You see that widget flashing? Start here, its not much and certainly tedious but it MIGHT help keep you a float. Ok, get a move on. I will check in with you later - ciao.','pics/characters/Phoebe.png']
				waitToTalk = gs.stopWatch(2,'gameStartIntro',message)
				
				# once flashign is finished, jump to message 
				if(waitToTalk):
					
					self.substate = 'flashOutro'
					phone.messageUpdate(message,gui,gs,alert=True,scrollOverride='normal')
			

			# keep widget going
			if(self.substate == 'flashOutro' and (gui.smsScrollDialogue.finished==False) ):
				args = 'demoWidgetAlert'

			# CONVO FINISHED
			if(self.substate == 'flashOutro' and (gui.smsScrollDialogue.finished==True)):
				flashCount = gs.stopWatch(0.1,'flashOutro','demoalert')
				if(flashCount):
					self.substate = 'oneFinalThing'
				

			# ==============TALKING ONE FINAL THING

			if(self.substate == 'oneFinalThing'):
				command = ['desktop','pulltab','phone']

				# trigger the demo alert in pulltab widget
				message = [99,'Cheryl',
				"Oh, one other thing, dont worry if you miss something, just check your phone messages. Surely you aren't too far gone that you cant even use a phone?" ,
				'pics/characters/Phoebe.png']
				
				waitToTalk = gs.stopWatch(2,'oneFinalThing',message)
				# once flashign is finished, jump to message 
				if(waitToTalk):

					self.substate = 'oneFinalThingOutro'
					phone.messageUpdate(message,gui,gs,alert=True,scrollOverride='normal')

			# CONVO FINISHED
			if(self.substate == 'oneFinalThingOutro' and (gui.smsScrollDialogue.finished==True)):
				otfCount = gs.stopWatch(2,'end-onefinalthing','demoalert')
				if(otfCount):
					self.substate = 'introcomplete'
					gui.debug('end of message ' + str('Oh, one other thing,'))
			


			if(self.substate == 'introcomplete'):
				gs.eventState = None



			if(gs.stage=='day1-guest'):
				print('introducing new person')
				# Add another person into the mix before next step of 'you hit your limit'
					
		    


			return(command,args)








		return(command,args)