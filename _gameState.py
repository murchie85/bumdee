class gameState():
	def __init__(self,state,tempState=None,functionState=None):
		self.state 			= state
		self.tempState      = tempState
		self.functionState  = functionState
		self.running        = True

		self.userName       = "Dobber"
		self.money          = 5.27
		self.hp             = 33
		self.happiness      = 0.4
		self.hunger         = 0.5

		self.items          = [('cigs',4),('old condom',1),('rusty spanner',1),('cough medicine',1)]




		self.counter        = None
		self.initCounter    = 40


	def countDown(self,count):
		if(self.counter==None): self.counter = count

		self.counter-=1
		if(self.counter<1):
			self.counter= None
			return(True)

		return(False)
		