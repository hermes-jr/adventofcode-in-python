#!/usr/bin/python
import re
import collections
import operator

deerstats = dict()
race = dict() # {deername -> [bool_running, distance, countdown, pointswon]}
stats = collections.namedtuple('stats', 'topspeed, endurance, resttime')

f = open('in.txt', 'r')
for line in f:
	line = line.strip()
	if(not line): continue

	if __debug__: print line

	# parse deer stats
	name = line.split(' ')[0]
	topspeed,endurance,resttime = re.findall(r'-?\d+', line)
	deerstats[name] = stats(int(topspeed), int(endurance), int(resttime))
	race[name] = {'running': True, 'distance': 0, 'countdown': deerstats[name].endurance, 'pointswon': 0}

if __debug__: print deerstats

if __debug__: print race # default state

maxdist = 0
for cursec in range(2503):
	for deer in race:
		if(race[deer]['running']):
			race[deer]['distance'] += deerstats[deer].topspeed # make step
			if(race[deer]['distance'] >= maxdist): 	maxdist = race[deer]['distance']

		if(race[deer]['countdown'] > 1):
			race[deer]['countdown'] -= 1
		else:
			# countdown zeroed. swap action and reset timer
			race[deer]['running'] ^= True
			race[deer]['countdown'] = deerstats[deer].endurance if(race[deer]['running']) else deerstats[deer].resttime
	for deer in race:
		if(race[deer]['distance'] == maxdist): race[deer]['pointswon'] += 1

	if __debug__: print "\n%4d: %s" % (cursec + 1, race)

leaderboard = sorted(race, key = lambda deer: race[deer]['distance'], reverse=True)

print "\n\nLEADERBOARD - distance"
for key in leaderboard:
	print key, race[key]

leaderboard = sorted(race, key = lambda deer: race[deer]['pointswon'], reverse=True)

print "\n\nLEADERBOARD - points"
for key in leaderboard:
	print key, race[key]

r"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

    Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?

--- Part Two ---

Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?

"""
