#!/usr/bin/python -OO
import re
r"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

	London to Dublin = 464
	London to Belfast = 518
	Dublin to Belfast = 141

	The possible routes are therefore:

		Dublin -> London -> Belfast = 982
		London -> Dublin -> Belfast = 605
		London -> Belfast -> Dublin = 659
		Dublin -> Belfast -> London = 659
		Belfast -> Dublin -> London = 605
		Belfast -> London -> Dublin = 982

		The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

		What is the distance of the shortest route?
"""

f = open('in2.txt', 'r')

prog = re.compile(r"^(\S+)\sto\s(\S+)\s=\s([0-9]+)$", re.UNICODE)
places = dict()
"""
places:
	0: (1, 217), (2, 123)...
	1: (0, 217)...
	2: (0, 123)...
	...
"""

"""
	for place:
		if been_there:
			continue
		if fullpath:
			return, continue
		# there are options otherwise
		get options
		for option:
			dig(option) # recurse
"""
def getpaths(path, poisoned = None):
	if poisoned == None: poisoned = list([None]) # there must be a first step

	padding = "...." * (len(poisoned) - 1) # display depth
	if __debug__: print padding + "Examining option %s , and been at %s" % (path, poisoned)

	if(path in poisoned and path != None):
		if __debug__: print padding + "Been here. Ignoring"
		if __debug__: print padding + "---\n"
		return # try next place

	poisoned.append(path) # mark as processed

	if(len(poisoned) >= len(places) + 1):
		if __debug__: print "\nPATH COVERING ALL THE PLACES FOUND AND SAVED: %s\n" % poisoned
		possiblepaths.append(list(poisoned))
		poisoned.pop()
		if __debug__: print "--- ---\n"
		return # try next place

	# no success or total failure, yet => there are options, try them
	if(path not in places.keys()):
		return # stub place

	if __debug__: print padding + "Possible subpaths are: %s" % places[path]

	for possible_path in places[path]:
		subname = possible_path[0]
		getpaths(subname, poisoned) # go deeper
		if __debug__: print "--- --- ---\n"
	poisoned.pop()

for line in f:
	line = line.strip()
	if(not line): continue # no empty lines allowed

	# store information about out graph connectivity and weights
	result = prog.findall(line)[0]
	if(result[0] not in places.keys()): places[result[0]] = list()
	places[result[0]].append(list([result[1], int(result[2])])) # adding path from one town to another
	if(result[1] not in places.keys()): places[result[1]] = list()
	places[result[1]].append(list([result[0], int(result[2])])) # and a path back

if __debug__: print "File parsed. Matrix: %s\n\n" % places

# time to recursively solve the puzzle
possiblepaths = list()
for start in places.keys():
	getpaths(start)

if __debug__: print "Total paths found: %s\n" % possiblepaths

# now it's time to sum all distances of all the paths. could be done earlier though
distances = list()
for path in possiblepaths:
		distance = 0
		if __debug__: print "Counting distance of %s" % path
		for cnt in range(1, len(path) - 1):
			if(path[cnt] not in places.keys()):
				continue # stub place
			for subcn in places[path[cnt]]:
				if(subcn[0] == path[cnt + 1]):
					if __debug__: print "Distance from %s to %s is %d" % (path[cnt], path[cnt + 1], subcn[1])
					distance += subcn[1]
		distances.append(distance)
		if __debug__: print "Distance of %s is %d" % (path, distance)

print "Shortest distance is: %d" % min(distances)
print "Longest distance is: %d" % max(distances)
