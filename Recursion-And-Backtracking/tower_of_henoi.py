def towerofhenoi(numberOfDisks, startPeg=1, endPeg=3):
	if(numberOfDisks):
		towerofhenoi(numberOfDisks-1, startPeg, 6-startPeg-endPeg)
		print "Move disk "+numberOfDisks+" from "+startPeg+" to "+endPeg
		towerofhenoi(numberOfDisks-1,6-startPeg-endPeg, endPeg)