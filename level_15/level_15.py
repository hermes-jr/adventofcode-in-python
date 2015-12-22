#!/usr/bin/python
import re
import numpy as np

RECIPE_SIZE = 100
MAXCALORIES = 500
ingreds = {}
scores1 = []
scores2 = []

def score(recipe, index):
	cap, dur, fla, tex, cal = 0
	for k,v in recipe.items():
		cap += v['cap']['i']

with open('in.txt', 'r') as f:
	for line in f:
		line = line.strip()
		if(not line): continue

		if __debug__: print(line)
		ingreds[line.split(':')[0]] = {k: int(v) for (k, v) in re.findall(r'([a-z]+) (-?\d+)', line)}

if __debug__: print('Ingredients parsed: {0}'.format(ingreds))

""" each recipe must contain exactly RECIPE_SIZE (100) spoons of ingredients total """
""" number of input ingredients is variable """
""" not the best solution, slow as hell, but it covers such options as: """
""" recipe has a missing ingredient, or there's only one ingredient. example: [50, 0, 0, 50] or [0, 0, 100, 0] """
#recipes = filter(lambda x: sum(x) == RECIPE_SIZE, np.ndindex((RECIPE_SIZE + 1, ) * len(ingreds)))
#recipes = [row for row in np.ndindex((RECIPE_SIZE + 1, ) * len(ingreds)) if sum(row) == RECIPE_SIZE] # seems a bit faster
for recipe in (row for row in np.ndindex((RECIPE_SIZE + 1, ) * len(ingreds)) if sum(row) == RECIPE_SIZE):
	if __debug__: print(recipe)
	props = {'cap': 0, 'dur': 0, 'fla': 0, 'tex': 0, 'cal': 0}
	for idx, amt in enumerate(recipe):
		ingred = ingreds[ingreds.keys()[idx]]
		if __debug__: print ('Amount of {0} is: {1}. props: {2}'.format(ingreds.keys()[idx], amt, ingred))
		props['cap'] += ingred['capacity'] * amt
		props['dur'] += ingred['durability'] * amt
		props['fla'] += ingred['flavor'] * amt
		props['tex'] += ingred['texture'] * amt
		props['cal'] += ingred['calories'] * amt

	props = {k: max(0, v) for k, v in props.items()}
	if(props['cal'] == MAXCALORIES):
		scores2.append(np.prod( {k: v for k, v in props.items() if k != 'cal'}.values() ))
	else:
		scores1.append(np.prod( {k: v for k, v in props.items() if k != 'cal'}.values() ))

print("Part 1 answer: {0}".format(max(scores1)))
print("Part 2 answer: {0}".format(max(scores2)))

r"""
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

    capacity (how well it helps the cookie absorb milk)
    durability (how well it keeps the cookie intact when full of milk)
    flavor (how tasty it makes the cookie)
    texture (how it improves the feel of the cookie)
    calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

    A capacity of 44*-1 + 56*2 = 68
    A durability of 44*-2 + 56*3 = 80
    A flavor of 44*6 + 56*-2 = 152
    A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?

--- Part Two ---

Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?
"""
