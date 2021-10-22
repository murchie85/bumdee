from _draw import *

class gameState():
	def __init__(
		self,
		state,
		tempState=None,
		functionState=None,
		initCounter=0,
		counter=None,
		dt=0,
		tickTimePassed=0,
		gameTime = {'day':6,'date':30,'month':8,'hour':23,'minute':59,'seconds':59},
		gameElapsed = 0):


		self.state 			= state
		self.tempState      = tempState
		self.functionState  = functionState
		self.running        = True


		self.displayDate    = ['Mon', '22', 'Aug', '02:57']
		self.userName       = "Dobber"
		self.level          = '1'
		self.money          = 5.27
		self.hp             = 33
		self.happiness      = 0.4
		self.hunger         = 0.5

		self.items          = [('cigs',4),('old condom',1),('rusty spanner',1),('cough medicine',1)]
		self.messages       = [[1,'Cheryl','Welcome to Bumdonian, have a look around and talk to Adam McMurchie if you get stuck. This game is a work in progress and not yet complete, it takes inpsiration from Drug wars, Undertale, Shenzhen IO and other classics. ','pics/characters/Phoebe.png'],
							   [2,'Adam','Hello you prick, did you forget already?','pics/characters/Chester.png'],
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
		

		self.initCounter    = initCounter
		self.counter        = counter
		
		self.dt 			= dt        
		self.tickTimePassed = tickTimePassed
		self.gameTime		= gameTime
		self.gameElapsed    = 0





		#--------------cantabs 
		self.cantabs			= 0
		self.exchangeRate       = 0.10





		# -----------widget states 
		self.activeWidget   = None 

	def countDown(self,count):
		if(self.counter==None): self.counter = count

		self.counter-=1
		if(self.counter<1):
			self.counter= None
			return(True)

		return(False)



	def tickTime(self):


		# ----------tick minute for every second
		# --------- calculation
		self.tickTimePassed += self.dt/1000
		if(self.tickTimePassed>1): 
			self.gameTime['minute']+=1
			self.tickTimePassed = 0

		# increment minute, reset second
		if(self.gameTime['seconds'] >59):
			self.gameTime['minute'] += 1
			self.gameTime['seconds'] = 0

		# increment hour, reset minute
		if(self.gameTime['minute'] >59):
			self.gameTime['hour'] += 1
			self.gameTime['minute'] = 0

		# date and date value
		if(self.gameTime['hour'] >23):
			self.gameTime['day'] += 1
			self.gameTime['date'] += 1
			self.gameTime['hour'] = 0

		if(self.gameTime['date']>30):
			self.gameTime['date'] = 1

		# Print Day
		if(self.gameTime['day'] > 6):
			self.gameTime['day'] =0



		# --------- format
		dayFmt   = {0:'Sun',1:'Mon',2:'Tue',3:'Wed',4:'Thu',5:'Fri',6:'Sat'}
		monthFmt = {0:'Jan',1:'Feb',2:'Mar',3:'Apr',4:'May',5:'Jun',6:'Jul',7:'Aug',8:'Sep',9:'Oct',10:'Nov',11:'Dec'}		

		# Formatting 
		day     = dayFmt[self.gameTime['day']]
		date    = self.gameTime['date']
		month   = monthFmt[self.gameTime['month']]
		hour    = self.gameTime['hour']
		minute  = self.gameTime['minute']
		seconds = self.gameTime['seconds']

		displayMinute = minute
		displayHour   = hour 
		if(minute<10): displayMinute =  '0' + str(minute) 
		if(hour<10):   displayHour   =  '0' +str(hour) 
		
		time    = str(displayHour) + ':' + str(displayMinute) 
		self.displayDate = [str(day),str(date),str(month),str(time)]

		