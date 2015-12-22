#!/usr/bin/python
from scipy.misc import comb
from itertools import combinations

TARGET = 150
MIN_BATCH = 2

bottles = []
with open('in.txt', 'r') as f:
	for line in f:
		bottles.append(int(line))

""" test case """
#bottles = [20, 15, 10, 5, 5]
#TARGET = 25

if(sum(bottles) == TARGET):
	print ("There's only one :-)")
	quit()

if __debug__: print(bottles)

""" i don't get yet how this shit works, just playing around """
cmb = sum( (comb(len(bottles), x, exact=True) for x in range(MIN_BATCH, len(bottles))) )
print("There would be a total of {0} bruteforce combinations.".format(cmb))

def getcombs():
	for batch in range(MIN_BATCH, len(bottles)):
		if __debug__: print ("Trying batches of: {0}".format(batch))
		for comb in combinations(bottles, batch):
			if __debug__: print ("Trying combination: {0}".format(comb))
			if sum(comb) == TARGET: yield comb

result = list(getcombs())
if __debug__:
	for res in result: print(res)
print("\n{0} of successful combinations found.".format(len(result)))

result2 = 0
minlen = len(result[0])
for res in result:
	l = len(res)
	if l < minlen:
		minlen = len(res)
		result2 = 1 # shorter result found, reset counter
	elif(l == minlen):
		result2 += 1 # one more short result found

print("{0} results of length {1}".format(result2, minlen))



r"""
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

    15 and 10
    20 and 5 (the first 5)
    20 and 5 (the second 5)
    15, 5, and 5

Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

--- Part Two ---

While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.
"""
