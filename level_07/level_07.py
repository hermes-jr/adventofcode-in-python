#!/usr/bin/python
import struct

f = open('in2.txt', 'r')

variables = dict()

for line in f:
	line = line.strip()
	if(not line): continue

	if __debug__: print line

	proc, dest = line.split(" -> ")

	variables[dest] = [None, proc]

"""
getvarval('x')
	if(already calculated)
		return value
	return parse(proc)
	return none

parse('a and b')
	#parse calculation

	if int() return int
	if lshift
		return getvarval(op1) << getvarval(op2)
	...
"""
def calc16bit(varname):
	return struct.unpack('I', struct.pack('i', calcvar(varname)))[0]

def calcvar(varname):
	calcval = None
	if(varname not in variables.keys()):
		return int(varname) # raw number
	if(variables[varname][0] != None):
		return variables[varname][0] # already calculated

	try:
		calcval = int(varname)
	except ValueError:
		calcval = parseproc(variables[varname][1])

	variables[varname][0] = calcval

	return calcval

def parseproc(proc):
	if "NOT" in proc:
		gate, op1 = proc.split()
		return ~calcvar(op1)
	elif "AND" in proc:
		op1, gate, op2 = proc.split()
		return calcvar(op1) & calcvar(op2)
	elif "OR" in proc:
		op1, gate, op2 = proc.split()
		return calcvar(op1) | calcvar(op2)
	elif "LSHIFT" in proc:
		op1, gate, op2 = proc.split()
		return calcvar(op1) << calcvar(op2)
	elif "RSHIFT" in proc:
		op1, gate, op2 = proc.split()
		return calcvar(op1) >> calcvar(op2)
	else:
		return calcvar(proc)
	return None

print variables
firsta = calc16bit('a')
print firsta

# reset the grid
for wire in variables.keys(): variables[wire][0] = None

# set val
variables['b'] = [firsta, str(firsta)]

# recalculate
print calc16bit('a')

"""
NOT x
x LSHIFT y
x RSHIFT y
x AND y
x OR y
"""

r"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

    123 -> x means that the signal 123 is provided to wire x.
    x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
    p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i

After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
"""
