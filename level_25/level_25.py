#!/usr/bin/python

""" To continue, please consult the code grid in the manual.  Enter the code at row 2947, column 3029. """

# column:
def triangular(n):
	return sum(range(n+1))

rownum = 2947
colnum = 3029
colstart = triangular(colnum)
print colstart
sm = colstart
summator = colnum


for i in range(rownum - 1):
	sm += summator
	summator += 1

santas_codenum = sm
print santas_codenum

startcode = 20151125
newcode = 0

for i in range(santas_codenum-1):
	tm = startcode * 252533
	newcode = tm % 33554393
	startcode = newcode

print newcode
