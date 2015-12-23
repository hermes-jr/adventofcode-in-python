#!/usr/bin/python
import random

#HERO = {'hp': 50, 'dmg': 0, 'mana': 500, 'arm': 0}
#BOSS={'hp': 58, 'dmg': 9}

""" test cases: """
HERO = {'hp': 10, 'dmg': 0, 'mana': 250, 'arm': 0}
# 1
BOSS={'hp': 13, 'dmg': 8} # test boss 1
TESTSEQ = [3, 0] # Poison, Magick Missile
# 2
#BOSS={'hp': 14, 'dmg': 8} # test boss 2
#TESTSEQ = [4, 2, 1, 3, 0] # Recharge, Shield, Drain, Poison, Magic Missile

SPELLS = (
		{'name': 'Magic Missile', 'mana': 53, 'dmg': 4},
		{'name': 'Drain', 'mana': 73, 'dmg': 2, 'hp': 2},
		{'name': 'Shield', 'mana': 113, 'arm': 7, 'eff': 6},
		{'name': 'Poison', 'mana': 173, 'dmg': 3, 'eff': 6},
		{'name': 'Recharge', 'mana': 229, 'mb': 101, 'eff': 3}
)

""" Minimum 1 damage point per hit """
def clampdmg(var):
	return max(1, var)

""" Method allows feeding test cases to battle """
def getspell(manaleft, active_effects):
	#return SPELLS[TESTSEQ.pop(0)] if (len(TESTSEQ) > 0) else None # Test case
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

	while(True):
		""" Effects strike """

		""" Hero strikes """
		""" At each player's turn there is a reason to cast a spell that results lesser 'minspent', flee otherwise """
		#active_effects['Poison'] = 3
		spell = getspell(HERO['mana'], active_effects)
		if(spell == None):
			print("Can't cast more spells. Flee")
			return {'victory': False, 'mana': manaspent}
			#continue

		if __debug__: print("Hero casts spell: {}".format(spell))
		manaspent += spell['mana']
		if(manaspent >= minspent and minspent != -1):
			if __debug__: print("Hero flees, could spend less mana.")
			return{'victory': False, 'mana': manaspent}
		#eff = clampdmg(hero['dmg'])
		#boss['hp'] -= eff
		#if __debug__: print("Hero deals {} damage; the boss goes down to {} hit points.".format(eff, boss['hp']))
		if(boss['hp'] <= 0):
			if __debug__: print("Hero wins :)")
			return {'victory': True, 'mana': manaspent}

		""" Boss' turn """
		eff = clampdmg(boss['dmg'] - hero['arm'])
		hero['hp'] -= eff
		if __debug__: print("Boss deals {} damage; the hero goes down to {} hit points.".format(eff, hero['hp']))
		if(hero['hp'] <= 0):
			if __debug__: print("Boss wins :(")
			return {'victory': False, 'mana': manaspent}

minspent = -1
for attempt in range(1, 5):
	result = battle()
	print(result)
