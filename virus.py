from __future__ import print_function
import os

def search():
	for filename in os.listdir("."):
		infect(filename)

def infect(filename):
	print (filename, end='')
		if not filename.startswith("infected"):
			print (" not infected...")
			os.rename(filename, "infected")

search()
