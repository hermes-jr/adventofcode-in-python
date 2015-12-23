#!/usr/bin/python
import ctypes
import re

""" since Python has no unsigned int builtin: """
class ureg(object):
	a, b = 0, 0
	def __setattr__(self, attr, val):
		self.__dict__[attr] = ctypes.c_uint32(val).value

regs = ureg()
prog = []
cir, eip = 0, 0

with open('in.txt', 'r') as f:
	for line in f:
		line = line.strip()
		
		if __debug__: print line
		prog.append(line)

def dumpregs():
	print("Registers: a: {0: <10d} b: {1:<10d}".format(regs.a, regs.b))

print("Running...")
done = False
while(not done):
	cir = eip
	eip += 1

	if(cir >= len(prog)):
		print("Done. Out of instructions")
		dumpregs()
		done = True
		break

	act = prog[cir]
	if __debug__:
		print("[{0:4d}]: {1:30s}".format(cir, act)),
		dumpregs()

	if(act.split()[0] == 'inc'):
		setattr(regs, act.split()[1], getattr(regs, act.split()[1]) + 1)
		continue
	elif(act.split()[0] == 'tpl'):
		setattr(regs, act.split()[1], getattr(regs, act.split()[1]) * 3)
		continue
	elif(act.split()[0] == 'hlf'):
		setattr(regs, act.split()[1], int(getattr(regs, act.split()[1]) / 2) )
		continue
	elif(act.split()[0] == 'jmp'):
		eip = cir + int(act.split()[1])
		continue
	elif(act.split()[0] == 'jio'):
		parts = re.split(' |,', act)
		comp = parts[1]
		trg = int(parts[3])
		if(getattr(regs, comp) == 1):
			eip += trg - 1
		continue
	elif(act.split()[0] == 'jie'):
		parts = re.split(' |,', act)
		comp = parts[1]
		trg = int(parts[3])
		if(getattr(regs, comp) % 2 == 0):
			eip += trg - 1
		continue

r"""
--- Day 23: Opening the Turing Lock ---

Little Jane Marie just got her very first computer for Christmas from some unknown benefactor. It comes with instructions and an example program, but the computer itself seems to be malfunctioning. She's curious what the program does, and would like you to help her run it.

The manual explains that the computer supports two registers and six instructions (truly, it goes on to remind the reader, a state-of-the-art technology). The registers are named a and b, can hold any non-negative integer, and begin with a value of 0. The instructions are as follows:

    hlf r sets register r to half its current value, then continues with the next instruction.
    tpl r sets register r to triple its current value, then continues with the next instruction.
    inc r increments register r, adding 1 to it, then continues with the next instruction.
    jmp offset is a jump; it continues with the instruction offset away relative to itself.
    jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
    jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

All three jump instructions work with an offset relative to that instruction. The offset is always written with a prefix + or - to indicate the direction of the jump (forward or backward, respectively). For example, jmp +1 would simply continue with the next instruction, while jmp +0 would continuously jump back to itself forever.

The program exits when it tries to run an instruction beyond the ones defined.

For example, this program sets a to 2, because the jio instruction causes it to skip the tpl instruction:

inc a
jio a, +2
tpl a
inc a

What is the value in register b when the program in your puzzle input is finished executing?
"""
