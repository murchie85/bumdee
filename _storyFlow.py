class gameFlow():
	def __init__(self):
		self.substate  = None
		self.waitDone  = False
	def phoneSequence(self,phase,message,returnState, phone,gui,gs,wait=1,alert=True,scrollOverride='normal'):
		waitIntro = gs.stopTimer.stopWatch(wait,phase,message,gs)

		# set cut scene while talking
		if(alert): gs.cutScene = True


		if(waitIntro):
			phone.messageUpdate(message,gui,gs,alert=alert,scrollOverride=scrollOverride)
			self.substate = returnState
	
	def phoneSequenceF(self,phase,message,returnState, phone,gui,gs,wait=1,alert=True,scrollOverride='normal'):

		waitIntro = gs.stopTimer.stopWatch(wait,phase,message,gs)

		# set cut scene while talking
		if(alert): gs.cutScene = True


		# Wait to start talking
		if(waitIntro and self.waitDone==False):
			phone.messageUpdate(message,gui,gs,alert=alert,scrollOverride=scrollOverride)
			self.waitDone = True

		# wait until finished talking then change state
		if(self.waitDone and gui.smsScrollDialogue.finished==True):
			self.substate = returnState
			self.waitDone = False
			gs.cutScene   = False
			gui.smsScrollDialogue.finished=False # needs further investigation 

	#----------main flow


	def checkDecisionFlow(self,gs,gui,phone,afterCommand=False):
		"""
		series of if/else check statements which 
		guides player through scenes and unlocks
		new events
		eventually might read from a file

		State tracked in GS for simplicity and easy load
		"""
		speed='fast'
		args = None
		command = ['desktop','recycle','forex','phone','afterCommand']
		
		if(gs.halt == True):
			gui.debug('Halting at story flow')
			return(command,args)




		# [1]--------begin sequence
		if(gs.stage=='day1-intro'):


			# allowed commands 
			command = ['desktop','recycle','phone','afterCommand']


			# Fade in (run at the end )
			if(self.substate == None and afterCommand):
				c = gui.fx.fadeIn(gs.stage,inc=6)
				if(c): self.substate = 'intro'
			


			# =============TALKING Intorduction Message

			if(self.substate == 'intro'):
				message = [99,'Cheryl','Hi welcome to Dundee, I dont have time to fuck about so will get straight to the point. Times are tough and I dont have any jobs for you, but I put in a good word with some recycle centers - maybe you can help them out?','pics/characters/Phoebe.png']
				self.phoneSequenceF('gameStartIntro',message,'flashingWidget',      phone,gui,gs,scrollOverride=speed)





			# ==============TALKING Introduce the widget and a job

			if(self.substate == 'flashingWidget'):
				command = ['desktop','recycle','phone']
				# trigger the demo alert in recycle widget
				args = 'demoWidgetAlert'
				message = [99,'Cheryl','You see that widget flashing? Start here, its not much and certainly tedious but it MIGHT help keep you a float. Ok, get a move on. I will check in with you later - ciao.','pics/characters/Phoebe.png']
				self.phoneSequenceF('flashingWidget',message,'flashOutro',      phone,gui,gs,wait=2,scrollOverride=speed)
			# keep widget going
			#if(self.substate == 'flashOutro' and (gui.smsScrollDialogue.finished==False) ): args = 'demoWidgetAlert'
			# CONVO FINISHED
			if(self.substate == 'flashOutro'):
				if(gs.stopTimer.stopWatch(1,'flashOutro','demoalert',gs)): self.substate = 'oneFinalThing'
				




			# ==============TALKING ONE FINAL THING

			if(self.substate == 'oneFinalThing'):
				command = ['desktop','recycle','phone']

				# trigger the demo alert in recycle widget
				message = [99,'Cheryl',
				"Oh, one other thing, dont worry if you miss something, just check your phone messages. Surely you aren't too far gone that you cant even use a phone?" ,
				'pics/characters/Phoebe.png']
				self.phoneSequenceF('oneFinalThing',message,'introcomplete',      phone,gui,gs,scrollOverride=speed)

			if(self.substate == 'introcomplete'):
				self.substate  = 'collectTabs'
				gs.cutScene = False # disabling cutscene


			if(self.substate == 'collectTabs'):
				print(gs.recycleLevel)
				if(gs.recycleLevel==2):
					print('setting dialogue')
					message = [14,'Cheryl','That was fasst! Ok, I think you get the idea, just keep spamming the tabs (or you can press the c key) - im sure if you keep doing it something good will happen...','pics/characters/Phoebe.png']
					self.phoneSequenceF('tabsdone',message,'tabsComplete',      phone,gui,gs)

			if(self.substate == 'tabsComplete'):
				print('Tabs done')
				

			# Add another person into the mix before next step of 'you hit your limit'
			return(command,args)
				








		return(command,args)