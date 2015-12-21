#!/usr/bin/python
import math

targetnum = 33100000
#targetnum = 990000

"""
a bit smarter solution using sequence:
A000203 a(n) = sigma(n), the sum of the divisors of n. Also called sigma_1(n).
(Formerly M2329 N0921)

if n is squared(x) then divisors are symmetric therefore no need to calculate all of them, only half
example:
8 = 8x1 or 1x8, 2x4 or 4x2
"""
targetnum /= 10 # each elf brings 10. reduce
done = False

def get_divisors(number):
	dlist = list()
	root = math.sqrt(number)
	if(math.modf(root)[0] == 0.0):
		dlist.append(root)
		yield int(root)

	for divisor in range(1, number):
		if(divisor in dlist and divisor != 1):
			return # returning half way through
		if(number % divisor == 0):
			dlist.append(divisor) # divisor
			dlist.append(number / divisor) # remember complementary
			yield divisor
			yield number / divisor

def sigma_1(num):
	return sum(get_divisors(num))

idx = 1
while(not done):
	sigma = sigma_1(idx)
	if __debug__: print "Trying house: %10d, sum of divisors is: %10d." % (idx, sigma)
	if (sigma_1(idx) >= targetnum):
		solution = idx
		done = True
	idx += 1
print "Solution found:", solution

r"""
# brute force solution, insane time
for house in range(1, targetnum):
	gifts = 0
	for elf in range(1, house+1):
		elvnfits = (house % elf == 0)
		if(elvnfits):
			if __debug__: print "elf %d fits for house %d" % (elf, house)
			gifts += 10 * elf
	if __debug__: print "In house %d there are %d gifts." % (house, gifts)
	if(gifts >= targetnum):
		print "Solution found, house number is %d, gifts number is: %d" % (house, gifts)
		quit()
		break
print "No solution found", quit()
"""

r"""
--- Day 20: Infinite Elves and Infinite Houses ---

To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door. He sends them down a street with infinite houses numbered sequentially: 1, 2, 3, 4, 5, and so on.

Each Elf is assigned a number, too, and delivers presents to houses based on that number:

    The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, ....
    The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, ....
    Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15, ....

There are infinitely many Elves, numbered starting with 1. Each Elf delivers presents equal to ten times his or her number at each house.

So, the first nine houses on the street end up like this:

House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.

The first house gets 10 presents: it is visited only by Elf 1, which delivers 1 * 10 = 10 presents. The fourth house gets 70 presents, because it is visited by Elves 1, 2, and 4, for a total of 10 + 20 + 40 = 70 presents.

What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?
"""
