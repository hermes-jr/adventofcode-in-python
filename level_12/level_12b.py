#!/usr/bin/python
import re
import json

nums = list()

def filterhook(param):
	for x in param:
		if(param[x] == 'red'): # discard object
			return None
	return param

f = open('in.txt', 'r')
filtered = json.load(f, object_hook=filterhook)

if __debug__: print json.dumps(filtered)
nums = list(re.findall(r'-?\d+', json.dumps(filtered)))

if __debug__: print nums
nums = list(map(int, nums))
if __debug__: print nums
print "Sum: %d" % sum(nums)

r"""
--- Day 12: JSAbacusFramework.io ---
--- Part Two ---

Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

    [1,2,3] still has a sum of 6.
    [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
    {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
    [1,"red",5] has a sum of 6, because "red" in an array has no effect.
"""
