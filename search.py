import os

def search(path="."):
	maxLength = 0 # length of longest string
	normalFiles = set() # set of uninfected file names
	for filename in os.listdir(path): # gets a list of file names in a given path
		stringLength = len(filename)
		if not filename.startswith("infected"):
			normalFiles.add(filename)
		if stringLength > maxLength:
			maxLength = stringLength
	return (normalFiles, maxLength)

def getExtension(fileName):
	return fileName.split(".")[-1]


