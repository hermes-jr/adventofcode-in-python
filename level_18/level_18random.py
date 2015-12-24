#!/usr/bin/python
import copy
import random

WIDTH = 70
HEIGHT = 46
STEPS = 1000000

lights = [[0 for x in range(WIDTH)] for x in range(HEIGHT)]

dark = '\x1b[32;40m#\x1b[0m'
bright = '\x1b[32;1m#\x1b[0m'

random.seed()
for i in range(HEIGHT):
	for j in range(WIDTH):
			lights[i][j] = random.randint(0,1)

nextgen = copy.deepcopy(lights)

def neighbour_vals(x, y):
	for i in range(x - 1, x + 2):
		for j in range(y - 1, y + 2):
			if((i in range(HEIGHT) and j in range(WIDTH)) and (x != i or y != j)): # definitely need some sleep. why the fuck OR works here instead of AND?!
				yield lights[i][j]

history = list()

def animate():
	global lights
	global nextgen
	global history

	for i in range(HEIGHT):
		for j in range(WIDTH):
			if( lights[i][j] == 1):
				if(sum(neighbour_vals(i, j)) not in (2, 3) ):
					nextgen[i][j] = 0
			if( lights[i][j] == 0):
				if( sum(neighbour_vals(i, j)) == 3 ):
					nextgen[i][j] = 1
	
	lights = copy.deepcopy(nextgen)

	if(len(history) > 7):
		history.pop(0)
		if(history[0] == history[6] or history[0] == history[5]):
			print("Endless loop detected, I quit.")
			quit()
	history.append(lights)

	for i in range(HEIGHT):
		line = ''
		for j in range(WIDTH):
			if(nextgen[i][j] == 1): line += dark
			else: line += '.'
		print("{0:3d}: {1}".format(i + 1, line))

for i in range(STEPS):
	if __debug__: print ("step {0:3d}".format(i + 1))
	animate()

print ("original {} lights on ".format( sum(map(sum, lights)) ))
print ("nextgen {} lights on ".format( sum(map(sum, nextgen)) ))
