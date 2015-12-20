#!/usr/bin/python

#startpass = 'ghijklmn'
startpass = 'cqjxjnds'
availchars = 'abcdefghijklmnopqrstuvwxyz' # no forbidden characters here

def inchar(char):
	if char == 'z':
		return ('a', True) # letter overflow
	return (availchars[availchars.index(char) + 1], False)

def incpass(pwd):
	if(pwd == "z"*8):
		return "a"*8 # password overflow
	"""
	from last to first:
		increment
		if overflowed: increment next
		break
	"""
	newpass = list(pwd) # because pwd is immutable (?)
	for idx,char in enumerate(reversed(pwd)):
		nc = inchar(char)
		newpass[len(pwd) - 1 - idx] = nc[0] # increment current register
		if(nc[1]): continue # if overflow happened, increment next register too
		return ''.join(newpass) # return as string

def validate(pwd):
	# TEST 0
	# fixed length, should never trigger this one
	assert len(pwd) == 8
	if(len(pwd) != 8):
		return False

	# TEST 1
	## no point in this since those characters never get to the password
	## forbidden characters
	if('i' in pwd or 'o' in pwd or 'l' in pwd):
		return False

	# TEST 2
	# store a collection of unique doubles
	alldoubles = dict()
	for i in range(len(pwd) - 1):
		comb = pwd[i: i+2]
		if(comb[0] == comb[1]):
			alldoubles[comb] = i
	if(len(alldoubles) < 2):
		return False
	if __debug__: print "Good combination of doubles found: %s" % alldoubles

	# TEST 3
	goodcomb = False
	for i in range(len(pwd) - 2):
		triplet = pwd[i:i+3]
		"""
		dirty quick workaround here about 'Z's because character overflows does not count
		this code could be prettier, but hey, there are no money involved ;-) hell with it
		"""
		if(triplet[0] != 'z' and triplet[1] != 'z' and triplet[2] == inchar(triplet[1])[0] and triplet[1] == inchar(triplet[0])[0]): # abc == a a+1 b+1
			goodcomb = True
			if __debug__: print "Good combination of three or more found: " + triplet
			break
	if(not goodcomb): return False # no good combination in password. failed test

	# all tests passed
	return True

cpass = startpass
#while(not validate(cpass)):
#	cpass = incpass(cpass)
#	if __debug__: print "Trying password: " + cpass

while(True):
	cpass = incpass(cpass)
	if(cpass == startpass):
		print "All combinations checked. Full cycle."
		break # full cycle done
	if(validate(cpass)):
		print "Good password found: " + cpass

r"""
--- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

    Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
    Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

For example:

    hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
    abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
    abbcegjk fails the third requirement, because it only has one double letter (bb).
    The next password after abcdefgh is abcdffaa.
    The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.

Given Santa's current password (your puzzle input), what should his next password be?
"""
