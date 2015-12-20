#!/usr/bin/python
import re
"""
--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

    turn on 0,0 through 0,0 would increase the total brightness by 1.
    toggle 0,0 through 999,999 would increase the total brightness by 2000000.
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
				lights[x][y] += 1
			if(result[0] == 'turn off'):
				if(lights[x][y] >= 1): lights[x][y] -= 1
			if(result[0] == 'toggle'):
				lights[x][y] += 2

litlights = 0
for x in range(1000):
	for y in range(1000):
		if(lights[x][y] > 0): litlights += lights[x][y]

print litlights

#print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in lights]))
