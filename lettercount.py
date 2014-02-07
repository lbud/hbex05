"""
open a file in the command line
make a list of all the characters in that file
make all of the letters lowercase
git rid of the ones who aren't in the range of hexadecimal letters
count each one:
	make a list of length 26 where all values = 0
	convert all hexidecimal numbers back to 0-25
	go to the count[thatnumbersasanindex] and iterate on that letter count
note: ords of lowercases are 97 (a) - 122 (z)
"""

from sys import argv

script, filename = argv

# open file and write the entire thing as a string, lowercase
f = open(filename)
filetext = f.read()
f.close()

lowerfile = filetext.lower()

# divide into individual character strings
chars = []
for char in lowerfile:
	chars.append(char)
	
# convert all to ords
ords = []
for char in chars:
	ords.append(ord(char))

# only want letters, strip the rest
letterords = []
for theord in ords:
	if 97 <= theord <= 122:
		letterords.append(theord)

# make these nicer numbers
letterords[:] = [x - 97 for x in letterords]

# initialize empty counter list
lettercounts = [0] * 26

# count letters!
for i in range(len(letterords)):
	lettercounts[letterords[i]] += 1

# print letter counts so that we can pipe this list to spark
for thecount in lettercounts:
    print thecount