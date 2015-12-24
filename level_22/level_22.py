#!/usr/bin/python
""" Works like a f%@$^ng WOPR! Awesome =) """
import random

HERO = {'hp': 50, 'dmg': 0, 'mana': 500, 'arm': 0}
BOSS={'hp': 58, 'dmg': 9}

""" test cases: """
#HERO = {'hp': 10, 'dmg': 0, 'mana': 250, 'arm': 0}
# 1
#BOSS={'hp': 13, 'dmg': 8} # test boss 1
#TESTSEQ = [3, 0] # Poison, Magic Missile
# 2
#BOSS={'hp': 14, 'dmg': 8} # test boss 2
#TESTSEQ = [4, 2, 1, 3, 0] # Recharge, Shield, Drain, Poison, Magic Missile

SPELLS = (
		{'name': 'Magic Missile', 'mana': 53, 'dmg': 4},
		{'name': 'Drain', 'mana': 73, 'dmg': 2, 'hp': 2},
		{'name': 'Shield', 'mana': 113, 'arm': 7, 'eff': 6},
		{'name': 'Poison', 'mana': 173, 'dmg': 3, 'eff': 6},
		{'name': 'Recharge', 'mana': 229, 'mb': 101, 'eff': 5}
)

""" Minimum 1 damage point per hit """
def clampdmg(var):
	return max(1, var)

def getspell(manaleft, active_effects):
	""" Method allows feeding test cases to battle """
	try:
		return SPELLS[TESTSEQ.pop(0)] if (len(TESTSEQ) > 0) else None # Test case
	except NameError: pass

	""" Attempt to return something unexpected first """
	for attempt in range(len(SPELLS) * 3):
		spell = random.choice(SPELLS)
		if(spell['mana'] <= manaleft and spell['name'] not in (k for k, v in active_effects.iteritems() if v > 0) ):
			return spell
	""" In case random missed many times, full scan: """
	for spell in SPELLS:
		if(spell['mana'] <= manaleft):
			return spell
	return None

def battle():
	hero = HERO.copy()
	boss = BOSS.copy()
	active_effects = {'Shield': 0, 'Poison': 0, 'Recharge': 0}
	manaspent = 0
	
	for turn in range(10000):
		""" Effects strike """
		if __debug__: print("Active effects: {}".format(active_effects))
		if(active_effects['Shield'] > 0):
			eff = 7 # FIXME: bad hardcode
			hero['arm'] = HERO['arm'] + eff
			if(active_effects['Shield'] - 1 == 0):
				if __debug__: print("Shield wears off leaving player with 0 defence")
				hero['arm'] = HERO['arm']
			active_effects['Shield'] -= 1
			if __debug__: print("Shield timer is now {}.".format(active_effects['Shield']))

		if(active_effects['Poison'] > 0):
			eff = 3
			boss['hp'] -= eff # FIXME: bad hardcode
			if(boss['hp'] <= 0):
				if __debug__: print("Poison deals {} damage. This kills the boss, and the player wins.".format(eff))
				return{'victory': True, 'mana': manaspent}
			active_effects['Poison'] -= 1
			if __debug__: print("Poison deals {} damage; its timer is now {}.".format(eff, active_effects['Poison']))

		if(active_effects['Recharge'] > 0):
			eff = 101
			hero['mana'] += eff# FIXME: bad hardcode
			active_effects['Recharge'] -= 1
			if __debug__: print("Recharge provides {} mana; its timer is now {}.".format(eff, active_effects['Recharge']))

		if(turn % 2 == 0):
			if __debug__: print("\n-- Player turn --\nHero: {}\nBoss: {}".format(hero, boss))
			""" Hero strikes """
			""" At each player's turn there is a reason to cast a spell that results lesser 'minspent', flee otherwise """
			spell = getspell(hero['mana'], active_effects)
			if(spell == None or hero['mana'] < 0):
				if __debug__: print("Can't afford any more spells. Flee")
				return {'victory': False, 'mana': manaspent}

			if __debug__: print("Hero casts a spell: {}".format(spell))
			hero['mana'] -= spell['mana']
			manaspent += spell['mana']

			if(spell['name'] in ('Shield', 'Recharge', 'Poison') ):
				active_effects[spell['name']] = spell['eff']

			elif(spell['name'] == 'Magic Missile'):
				eff = clampdmg(spell['dmg'])
				boss['hp'] -= eff
				if __debug__: print("Hero deals {} damage; the boss goes down to {} hit points.".format(eff, boss['hp']))

			elif(spell['name'] == 'Drain'):
				eff = clampdmg(spell['dmg'])
				boss['hp'] -= eff
				hero['hp'] += spell['hp']
				if __debug__: print("Hero casts Drain dealing {} damage and gaining {} HP; the boss goes down to {} hit points.".format(eff, spell['hp'], boss['hp']))

			if(boss['hp'] <= 0):
				if __debug__: print("Hero wins :)")
				return {'victory': True, 'mana': manaspent}

			"""
			if(manaspent > minspent and minspent != -1):
				if __debug__: print("No reason to fight any more, could be done better.")
				return{'victory': False, 'mana': manaspent}
			"""
		else:
			if __debug__: print("\n-- Boss turn --\nHero: {}\nBoss: {}".format(hero, boss))
			""" Boss' turn """
			eff = clampdmg(boss['dmg'] - hero['arm'])
			hero['hp'] -= eff
			if __debug__: print("Boss deals {} damage; the hero goes down to {} hit points.".format(eff, hero['hp']))
			if(hero['hp'] <= 0):
				if __debug__: print("Boss wins :(")
				return {'victory': False, 'mana': manaspent}


minspent = -1
for attempt in range(1000000):
	result = battle()
	if((result['victory'] and result['mana'] < minspent) or minspent == -1):
		minspent = result['mana']

print minspent

r"""
--- Day 22: Wizard Simulator 20XX ---

Little Henry Case decides that defeating bosses with swords and stuff is boring. Now he's playing the game with a wizard. Of course, he gets stuck on another boss and needs your help again.

In this version, combat still proceeds with the player and the boss taking alternating turns. The player still goes first. Now, however, you don't get any equipment; instead, you must choose one of your spells to cast. The first character at or below 0 hit points loses.

Since you're a wizard, you don't get to wear armor, and you can't attack normally. However, since you do magic damage, your opponent's armor is ignored, and so the boss effectively has zero armor as well. As before, if armor (from a spell, in this case) would reduce damage below 1, it becomes 1 instead - that is, the boss' attacks always deal at least 1 damage.

On each of your turns, you must select one of your spells to cast. If you cannot afford to cast any spell, you lose. Spells cost mana; you start with 500 mana, but have no maximum limit. You must have enough mana to cast a spell, and its cost is immediately deducted when you cast it. Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.

    Magic Missile costs 53 mana. It instantly does 4 damage.
    Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
    Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
    Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
    Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

Effects all work the same way. Effects apply at the start of both the player's turns and the boss' turns. Effects are created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they have, their timer is decreased by one. If this decreases the timer to zero, the effect ends. You cannot cast a spell that would start an effect which is already active. However, effects can be started on the same turn they end.

For example, suppose the player has 10 hit points and 250 mana, and that the boss has 13 hit points and 8 damage:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 13 hit points
Player casts Poison.

-- Boss turn --
- Player has 10 hit points, 0 armor, 77 mana
- Boss has 13 hit points
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 damage.

-- Player turn --
- Player has 2 hit points, 0 armor, 77 mana
- Boss has 10 hit points
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 2 hit points, 0 armor, 24 mana
- Boss has 3 hit points
Poison deals 3 damage. This kills the boss, and the player wins.

Now, suppose the same initial conditions, except that the boss has 14 hit points instead:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 14 hit points
Player casts Recharge.

-- Boss turn --
- Player has 10 hit points, 0 armor, 21 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 4.
Boss attacks for 8 damage!

-- Player turn --
- Player has 2 hit points, 0 armor, 122 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 3.
Player casts Shield, increasing armor by 7.

-- Boss turn --
- Player has 2 hit points, 7 armor, 110 mana
- Boss has 14 hit points
Shield's timer is now 5.
Recharge provides 101 mana; its timer is now 2.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 211 mana
- Boss has 14 hit points
Shield's timer is now 4.
Recharge provides 101 mana; its timer is now 1.
Player casts Drain, dealing 2 damage, and healing 2 hit points.

-- Boss turn --
- Player has 3 hit points, 7 armor, 239 mana
- Boss has 12 hit points
Shield's timer is now 3.
Recharge provides 101 mana; its timer is now 0.
Recharge wears off.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 2 hit points, 7 armor, 340 mana
- Boss has 12 hit points
Shield's timer is now 2.
Player casts Poison.

-- Boss turn --
- Player has 2 hit points, 7 armor, 167 mana
- Boss has 12 hit points
Shield's timer is now 1.
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 167 mana
- Boss has 9 hit points
Shield's timer is now 0.
Shield wears off, decreasing armor by 7.
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 1 hit point, 0 armor, 114 mana
- Boss has 2 hit points
Poison deals 3 damage. This kills the boss, and the player wins.

You start with 50 hit points and 500 mana points. The boss's actual stats are in your puzzle input. What is the least amount of mana you can spend and still win the fight? (Do not include mana recharge effects as "spending" negative mana.)
"""
