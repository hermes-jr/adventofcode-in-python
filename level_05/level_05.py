#!/usr/bin/python

"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
    aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    jchzalrnumimnmhp is naughty because it has no double letter.
    haegwjzuvuyypxyu is naughty because it contains the string xy.
    dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?
"""

f = open('in.txt', 'r')
nice_strings = 0

for line in f:
	line = line.strip()
	if(not line): continue

	print line

	forbidden = ('ab', 'cd', 'pq', 'xy')
	prevl = ''
	vovels = 'aeiou'
	has_double = False
	has_vovels = 0
	good = True

	for letter in line:
		if(prevl + letter in forbidden):
			good = False
			break
		if(prevl == letter): has_double = True
		prevl = letter

		if(letter in vovels): has_vovels += 1
	
	if(good and has_vovels >= 3 and has_double): nice_strings += 1

print nice_strings
