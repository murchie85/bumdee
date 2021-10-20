from _draw import *

class gameState():
	def __init__(self,state,tempState=None,functionState=None):
		self.state 			= state
		self.tempState      = tempState
		self.functionState  = functionState
		self.running        = True


		self.date           = ['Mon', '22', 'Aug', '22:57']
		self.userName       = "Dobber"
		self.level          = '1'
		self.money          = 5.27
		self.hp             = 33
		self.happiness      = 0.4
		self.hunger         = 0.5

		self.items          = [('cigs',4),('old condom',1),('rusty spanner',1),('cough medicine',1)]
		self.messages       = [[1,'Adam','Hello you prick, did you forget already?','pics/characters/Chester.png'],
							   [3,'Boris','Hi, please support my next election campaign and I promise to prevent mandatory organ donations'],
							   [4,'Cynthia', 'Dont text me again you creep','pics/characters/Jane.png'],
							   [5,'Python','Traceback (most recent call last): ...why bother you cant code anyway.'],
							   [8,'Dominic', 'Got any jobs going mate?','pics/characters/Gregg.png'],
							   [7,'Morphius','How did you get this number?']]

		self.music          = [[1,'solitude','music/solitude.mp3'],
							   [3,'Unknown Track 1','music/trackx.mp3'],
							   [4,'The Darkness I believe in a thing called love', 'music/trackx.mp3'],
							   [5,'Foo fighters learn to fly','music/trackx.mp3'],
							   [8,'Bloc Party Helicopter', 'music/trackx.mp3'],
							   [7,'Unknown Gimme yer wallet','music/trackX.mp3']]
		self.contacts       = [['1','Arnold','18:10'],
							   ['2','Gas Man','12:05'],
							   ['3','Mr X','19:35'],
							   ['4','Freddy','17:02'],
							   ['5','Christ','09:11'],
							   ['6','Stalone','14:36'],
							   ['7','Missy','12:19'],
							   ['8','Council','15:03'],

							   ]


		self.counter        = None
		self.initCounter    = 40


	def countDown(self,count):
		if(self.counter==None): self.counter = count

		self.counter-=1
		if(self.counter<1):
			self.counter= None
			return(True)

		return(False)
		