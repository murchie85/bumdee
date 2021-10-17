class gameState():
	def __init__(self,state,tempState=None,functionState=None):
		self.state 			= state
		self.tempState      = tempState
		self.functionState  = functionState
		self.running        = True

		self.userName       = "Dobber"
		self.counter        = None
		self.initCounter    = 40


	def countDown(self,count):
		if(self.counter==None): self.counter = count

		self.counter-=1
		if(self.counter<1):
			self.counter= None
			return(True)

		return(False)
		