
class stopTimer():
	def __init__(self):
		self.stopWatchInit  = False
		self.stopWatchState = None

	def stopWatch(self,countValue,source,trackedObject,gs):
		complete = False
		# Re-Initialise automatically
		if(self.stopWatchInit):
			if(self.stopWatchState['source']!= source or self.stopWatchState['endCount']!= countValue or self.stopWatchState['trackedObject']!= trackedObject):
				print('***initialising counter**** for : ' + str(source))
				self.stopWatchInit=False

		if(self.stopWatchInit==False):
			self.stopWatchState = {'elapsed': 0,'endCount':countValue,'source':source,'trackedObject':trackedObject}
			self.stopWatchInit=True

		if(self.stopWatchInit):
			self.stopWatchState['elapsed'] += gs.dt/1000
			#print('Iter: ' + str(self.itercount) + '  elapsed: ' + str(self.stopWatchState['elapsed']))
			if(self.stopWatchState['elapsed']>self.stopWatchState['endCount']):
				complete=True


		return(complete)