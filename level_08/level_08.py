#!/usr/bin/python
import re
"""
--- Day 8: Matchsticks ---

Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.

It is common in many programming languages to provide a way to escape special characters in strings. For example, C, JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.

However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.

For example:

    "" is 2 characters of code (the two double quotes), but the string contains zero characters.
    "abc" is 5 characters of code, but 3 characters in the string data.
    "aaa bsbs"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
    "bsbs x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.

Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are bsbs (which represents a single backslash), bs" (which represents a lone double-quote character), and bs x plus two hexadecimal characters (which represents a single character with that ASCII code).

Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?

For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.
"""

f = open('in.txt', 'r')

totalsyms = 0
totalmem = 0

prog = re.compile(r"(\\){2}|\\x[0-9abcdef]{2}|\\\"", re.UNICODE)

for line in f:
	line = line.strip()
	if(not line): continue # no empty lines allowed

	totalsyms += len(line)
	filtered = line[1:-1] # remove first and last quotes
	filtered = prog.sub('_', filtered)
	totalmem += len(filtered)
	
	print "%s => %s" % (line, filtered)

print totalsyms
print totalsyms-totalmem
