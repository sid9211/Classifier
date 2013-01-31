from music21 import *
from numpy import *
from collections import *
from Histogram import *
def pitchClassVector(score):
	#Flatten the score so that all notes are at the first level
	flat = score.flat

	#Total number of pitches in score

	totalPitchCount = len(flat.pitches)

	# An empty list to hold all the Pitch Classes
	L = []
	for pitch in flat.pitches:
		L.append(pitch.pitchClass)

	# Calculate the frequency count of each Pitch Class
	MyFreqPitchClass = histogram(L)
	# An empty list to return
	R = []

	# There are 12 Pitch Classes
	numPitchClasses = 12
	for i in range(numPitchClasses):
		# Get the frequency of each Pitch Class
		val = MyFreqPitchClass.get(i, 0)
		# Divide it by the total Pitch count(normalize)
		val = float(val)/totalPitchCount
		# Append it to the list we want to return
		R.append(val)
	return R
