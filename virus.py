from __future__ import print_function
import os, time

def search():
	for filename in os.listdir("."):
		infect(filename)

def infect(filename):
	print (filename, end='')
	if filename.startswith("infected"):
		print (" infected")
	else:
		print (" not infected yet...", end='')
		time.sleep(5)
		print (" Infecting...")
		#os.rename(filename, "infected")

search()
