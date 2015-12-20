#!/usr/bin/python
from collections import deque
"""
--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
    xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
    uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
    ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

How many strings are nice under these new rules?
"""

f = open('in.txt', 'r')
nice_strings = 0

for line in f:
	line = line.strip()
	if(not line): continue

	print line

	prevl = ''
	doubles = dict()
	dq = deque(['', '', ''])
	goodgaps = 0
	gooddoubles = 0
	samecount = 1

	for letter in line:
		dq.popleft()
		dq.append(letter)
		if(dq[0] == dq[2]):
			goodgaps += 1
			print dq

		samecount = samecount + 1 if prevl == letter else 1

		pc = prevl + letter
		if(prevl != letter or samecount % 2 == 0):
			doubles[pc] = 1 if pc not in doubles.keys() else doubles[pc] + 1

		prevl = letter

	for key in doubles.keys():
		if(doubles[key] >= 2):
			print "Matching double %s %d" % (key, doubles[key])
			gooddoubles += 1

	if(gooddoubles >= 1 and goodgaps >= 1):
		nice_strings += 1
		print "Nice: %s" % line

print nice_strings
