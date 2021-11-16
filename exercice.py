"""
Chapitre 11.1
"""


import math
from inspect import *
import random
from game import *

class Weapon:
	def __init__(self, nom, niveau_dattaque, niveau_minimal):
		self.__nom = nom
		self.niveau_dattaque = niveau_dattaque
		self.niveau_minimal = niveau_minimal
		
	def make_unarmed(self):
		self.__nom = "Unarmed"
		self.niveau_dattaque = 20

class Character:
	def __init__(self, nom, max_hp, attack, defense, level, weapon):
		self.nom = nom
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.hp = max_hp
		if weapon == None:
	
	def compute_damage(self, damage, c1, weapon, c2):
		self.damage = (((((( 2 * c1.level) / 5) + 2) * weapon.niveau_dattaque * (c1.attaque/c2.defense)) / 50 ) + 2)
		if random.random < 0.0625:
			self.damage *= 2
		

# class Game:
# 	def __init__(self, c1, c2):


# def main():
# 	c1 = Character("Äpik", 200, 150, 70, 70)
# 	c2 = Character("Gämmor", 250, 100, 120, 60)

# 	c1.weapon = Weapon("BFG", 100, 69)
# 	c2.weapon = Weapon("Deku Stick", 120, 1)

# 	turns = run_battle(c1, c2)
# 	print(f"The battle ended in {turns} turns.")

# if __name__ == "__main__":
# 	main()

