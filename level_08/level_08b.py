#!/usr/bin/python
import re
r"""
--- Part Two ---

Now, let's go the other way. In addition to finding the number of characters of code, you should now encode each code representation as a new string and find the number of characters of the new encoded representation, including the surrounding double quotes.

For example:

    "" encodes to "\"\"", an increase from 2 characters to 6.
    "abc" encodes to "\"abc\"", an increase from 5 characters to 9.
    "aaa\"aaa" encodes to "\"aaa\\\"aaa\"", an increase from 10 characters to 16.
    "\x27" encodes to "\"\\x27\"", an increase from 6 characters to 11.

Your task is to find the total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal. For example, for the strings above, the total encoded length (6 + 9 + 16 + 11 = 42) minus the characters in the original code representation (23, just like in the first part of this puzzle) is 42 - 23 = 19.
"""

f = open('in.txt', 'r')

totalsyms = 0
totalmem = 0

for line in f:
	line = line.strip()
	if(not line): continue # no empty lines allowed

	totalsyms += len(line)
	filtered = line
	filtered = re.sub(r"\\", r"\\\\", filtered)
	filtered = re.sub(r"\"", r"\"", filtered)
	totalmem += len(filtered)
	totalmem += 2 # fake two additional quotes
	
	print "%s => %s" % (line, filtered)

print totalsyms
print totalmem-totalsyms
