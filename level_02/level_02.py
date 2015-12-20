#!/usr/bin/python

"""
Material needed: 2*l*w + 2*w*h + 2*h*l + area of the smallest size
2*a*b + 2*b*c * 2*c*a + min(ab, bc, ca)
"""

f = open('in.txt', 'r')
total_paper = 0
total_ribbon = 0

for line in f:
	w, h, d = (int(x) for x in line.split("x"))
	planes = (w*h, h*d, w*d)
	area = 2*planes[0] + 2*planes[1] + 2*planes[2] + min(planes)
	total_paper += area

	perimeters = (2*(w+h), 2*(h+d), 2*(w+d))
	total_ribbon += w*h*d + min(perimeters)

print "total paper: %d" % total_paper
print "total ribbon: %d" % total_ribbon
