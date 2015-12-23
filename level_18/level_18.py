#!/usr/bin/python
import copy

IN = ('in.txt', 100, 100)
#IN = ('in2.txt', 6, 4) # test case
SIZE = IN[1]
STEPS = IN[2]

lights = [[0 for x in range(SIZE)] for x in range(SIZE)]

with open(IN[0], 'r') as f:
	for j,line in enumerate(f):
		line = line.strip()
		if(not line): continue

		if __debug__: print("{0:3d}: {1}".format(j + 1, line))
		for k,char in enumerate(line):
			if(char == '#'): lights[j][k] = 1

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
--- Day 18: Like a GIF For Your Yard ---

After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.

The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

    A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
    A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.

All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......

After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?
"""
