#!/usr/bin/python
import re

aunts = {}
TARGETPROPS = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
			'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
result1 = -1
result2 = -1

with open('in.txt', 'r') as f:
	for line in f:
		line = line.strip()
		if(not line): continue

		if __debug__: print(line)

		params = {'children': -1, 'cats': -1, 'samoyeds': -1, 'pomeranians': -1, 'akitas': -1,
				'vizslas': -1, 'goldfish': -1, 'trees': -1, 'cars': -1, 'perfumes': -1}
		auntid = int(re.findall(r'^Sue (\d+)', line)[0])
		for match in re.findall(r'(\S+): (\d+)', line):
			params[match[0]] = int(match[1])
		aunts[auntid] = params

if __debug__: print("\n".join("{}: {}".format(k, v) for k, v in aunts.items()))

for k, v in aunts.items():
	allkeys = True
	for key in TARGETPROPS.keys():
		if(v[key] == -1): continue
		if(TARGETPROPS[key] != v[key]):
			if __debug__: print("Aunt {}: no match".format(k))
			allkeys = False
			break
	if(allkeys):
		if __debug__: print("Aunt {}: MATCH FOUND!".format(k))
		result1 = k

""" this is bullshit. lack of sleep """
""" gives a correct result however """
for k, v in aunts.items():
	allkeys = True
	for key in TARGETPROPS.keys():
		if(v[key] == -1): continue
		if((key in ('cats', 'trees')) and TARGETPROPS[key] >= v[key]):
			allkeys = False
			if __debug__: print("Aunt {}: no match, cats and trees".format(k))
			break
		elif((key in ('pomeranians', 'goldfish')) and TARGETPROPS[key] <= v[key]):
			allkeys = False
			if __debug__: print("Aunt {}: no match, fish and pompom".format(k))
			break
		elif(key not in ('pomeranians', 'goldfish', 'cats', 'trees') and TARGETPROPS[key] != v[key]):
			allkeys = False
			if __debug__: print("Aunt {}: no match, known data {}".format(k, key))
			break
	if(allkeys):
		result2 = k
		if __debug__: print("Aunt {}: MATCH FOUND!".format(k))

print("Part1 answer: {}".format(result1))
print("Part2 answer: {}".format(result2))

r"""
--- Day 16: Aunt Sue ---

Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

    children, by human DNA age analysis.
    cats. It doesn't differentiate individual breeds.
    Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
    goldfish. No other kinds of fish.
    trees, all in one group.
    cars, presumably by exhaust or gasoline or something.
    perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1

You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?

--- Part Two ---

As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?
"""
