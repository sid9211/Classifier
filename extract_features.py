from music21 import *
from numpy import *
from collections import *
from Histogram import *
from PitchClassVector import *
from ListtoCSV import *
from csv_io import *

# Loop through all files
sBeethoven = converter.parse('./beetho5a.krn')

#For each file , extract all features.
#Each function for a feature will return a list
L = pitchClassVector(sBeethoven)

#Concatenate all lists into onr list along with target music class
feature =  list_to_csv(L)
targetclass = "1, "

targetandfeature = targetclass + feature

listfeatures = []


listfeatures.append(targetandfeature)

#Write this matrix to CSV
filename = 'testmusic.csv'
write_delimited_file(filename, listfeatures)
