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

# initialize letter counter list
lettercounts = [0] * 26

# loop through file, find letters, iterate on relevant counter
for char in lowerfile:
	char = ord(char)
	if 97 <= char <= 122:
		char -= 97
		lettercounts[char] += 1
		
for thecount in lettercounts:
    print thecount