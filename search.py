import os

def search(path="."):
	normalFiles = set() # set of uninfected file names
	for filename in os.listdir(path): # gets a list of file names in a given path
		if not filename.startswith("infected"):
			normalFiles.add(filename)
	return normalFiles



