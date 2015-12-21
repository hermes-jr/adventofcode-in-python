#!/usr/bin/python
import re
import itertools

preferences = dict()
table = list()

f = open('in.txt', 'r')
for line in f:
	line = line.strip()
	if(not line): continue

	if __debug__: print line

	# parse guests
	name = line.split(' ')[0] # first word
	neighbour = line.split(' ')[-1][:-1] # last word, dod trimmed
	sign,happ = re.findall(r'(gain|lose) (\d+)', line)[0]
	sign = 1 if(sign == 'gain') else -1
	happ = sign * int(happ)

	if __debug__: print name, neighbour, happ
	preferences[(name, neighbour)] = happ
	preferences[(name, 'me')] = 0
	preferences[('me', neighbour)] = 0

	if name not in table: table.append(name)

table.append('me')

if __debug__: print preferences

if __debug__: print table

totals = list()

for perm in itertools.permutations(table):
	if __debug__: print "Analyzing permutation ",  perm

	happiness = 0
	for idx in range(len(perm)):
		idxp = len(perm) - 1 if (idx == 0) else idx-1
		idxn = 0 if (idx == len(perm) - 1) else idx+1
		if __debug__: print "%s <- %s -> %s" % (perm[idxp], perm[idx], perm[idxn])
		happiness += preferences[(perm[idx], perm[idxp])] + preferences[(perm[idx], perm[idxn])]
	if __debug__: print "Total happiness: ", happiness
	totals.append(happiness)

print "Max value is: ", max(totals)

r"""
--- Part Two ---

In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?
"""
