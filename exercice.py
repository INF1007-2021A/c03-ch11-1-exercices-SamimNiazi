"""
Chapitre 11.1
"""


import math
from inspect import *
import random
from game import *



class Weapon:
	UNARMED_POWER = 20
	def __init__(self, name: str, power, min_level):
		self.__name = name
		self.power = power
		self.minlevel = min_level

	@property  #sert a acceder aux variable pcq il est prives
	def name(self):
		return self.__name

	@classmethod #ca sert a quoi???
	def make_unarmed(cls):
		return cls("Unarmed", cls.UNARMED_POWER, 1 ) #pk cls????

class Character:
	def __init__(self, name, max_hp, attack, defense, level): #pas mettre Weapon
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = None   #erreur ici
		self.hp = max_hp

		

