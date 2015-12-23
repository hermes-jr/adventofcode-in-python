#!/usr/bin/python
import copy

IN = ('in.txt', 100, 100)
#IN = ('in3.txt', 6, 5) # test case
SIZE = IN[1]
STEPS = IN[2]

lights = [[0 for x in range(SIZE)] for x in range(SIZE)]

# part 2: corners olways on
def iscorner(x, y):
	if (x == 0 and y == 0): return True
	if (x == 0 and y == SIZE-1): return True
	if (x == SIZE-1 and y == 0): return True
	if (x == SIZE-1 and y == SIZE-1): return True
	return False

with open(IN[0], 'r') as f:
	for j,line in enumerate(f):
		line = line.strip()
		if(not line): continue

		if __debug__: print("{0:3d}: {1}".format(j + 1, line))
		for k,char in enumerate(line):
			if(char == '#' or iscorner(j, k)): lights[j][k] = 1


nextgen = copy.deepcopy(lights)

def neighbour_vals(x, y):
	for i in range(x - 1, x + 2):
		for j in range(y - 1, y + 2):
			if((i in range(SIZE) and j in range(SIZE)) and (x != i or y != j)): # definitely need some sleep. why the fuck OR works here instead of AND?!
				yield lights[i][j]
				"""
				# clamp values to matrix size
				nx = max(0, min(i, SIZE))
				ny = max(0, min(j, SIZE))
				"""

def animate():
	global lights
	global nextgen

	for i in range(SIZE):
		for j in range(SIZE):
			#if __debug__: print("for light {}:{} (state: {}) sum of neighbors is {}".format(i, j, lights[i][j], sum(neighbour_vals(i, j)) )),
			if( lights[i][j] == 1):
				if(sum(neighbour_vals(i, j)) not in (2, 3) ):
					nextgen[i][j] = 0
			if( lights[i][j] == 0):
				if( sum(neighbour_vals(i, j)) == 3 ):
					nextgen[i][j] = 1
			if(iscorner(i, j)):
				nextgen[i][j] = 1
	lights = copy.deepcopy(nextgen)

	if __debug__:
		for i in range(SIZE):
			line = ''
			for j in range(SIZE):
				if(nextgen[i][j] == 1): line += '#'
				else: line += '.'
			print("{0:3d}: {1}".format(i + 1, line))

for i in range(STEPS):
	if __debug__: print ("step {0:3d}".format(i + 1))
	animate()

print ("original {} lights on ".format( sum(map(sum, lights)) ))
print ("nextgen {} lights on ".format( sum(map(sum, nextgen)) ))

r"""
--- Part Two ---

You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off. The example above will actually run like this:

Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#

After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?
"""
