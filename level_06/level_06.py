#!/usr/bin/python
import re
"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
    turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?
"""

f = open('in.txt', 'r')
lights = [[0 for col in range(1000)] for row in range(1000)]

for line in f:
	line = line.strip()
	if(not line): continue

	prog = re.compile("^(turn on|turn off|toggle)\s([0-9]{1,3}),([0-9]{1,3})\sthrough\s([0-9]{1,3}),([0-9]{1,3})$", re.UNICODE)
	result = prog.findall(line)
	result = result[0]
	print result

	xl = int(result[1])
	yt = int(result[2])
	xr = int(result[3])
	yb = int(result[4])

	for x in range(xl, xr+1):
		for y in range(yt, yb+1):
			if(result[0] == 'turn on'):
				lights[x][y] = 1
			if(result[0] == 'turn off'):
				lights[x][y] = 0
			if(result[0] == 'toggle'):
				lights[x][y] = 1 if lights[x][y] == 0 else 0

litlights = 0
for x in range(1000):
	for y in range(1000):
		if(lights[x][y] == 1): litlights += 1

print litlights

#print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in lights]))
