"""
Chapitre 11.1
"""

import random

import utils

class Weapon:
	UNARMED_POWER = 20
	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property  #sert a acceder aux variable pcq il est prives (getter)
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
	
	@property
	def name(self):
		return self.__name

	@property
	def weapon(self):
		return self.__weapon
	
	@weapon.setter  #setter sert a changer la valeur
	def weapon(self, value): #value du self.__weapon (c'est un weapon en tant que telle)
		if value is None:
			value = Weapon.make_unarmed()
		if value.minlevel > self.level:
			raise ValueError(Weapon) #raise sort une erreur ValueError = bon truc mais mauvaise valeur
		self.__weapon = value
	
	@property
	def hp(self):
		return self.__hp
	
	@hp.setter   #sert a restraindre la valeur du hp (essayer de le faire sans le utilis.clamp)
	def hp(self, val):
		self.__hp = utils.clamp(val, 0, self.max_hp)

	def compute_damage(self, other):
		parametrelevel = ((2/5)*self.level) + 2
		attackanddefense = self.attack/other.defense
		rand = random.uniform(0.85,0.1)
		if random.randint(0,100) < 6.25:
			crit = 2
		else:
			crit = 1
		modifier = rand * crit
		damage = round((((parametrelevel * self.weapon.power * attackanddefense) /50 ) + 2) * modifier)
		return damage, crit #self.weapon.power on est dans le character c pour ca

def deal_damage(Character1, Character2):
	damage, crit = Character.compute_damage(Character1, Character2)
	Character2.hp -= damage
	if crit == 2:
		print("Critical Hit!")
	print (f'{Character1.name} used {Character1.weapon.name} \n {Character2.name} took {damage} dmg')

def run_battle (C1, C2):
	attacker = C1
	defender = C2
	turns = 0
	print (f'{C1.name} starts a battle with {C2.name}')
	while defender.hp != 0:
		turns +=1 
		deal_damage(attacker, defender)
		attacker, defender = defender, attacker
	print (f'{defender.name} is sleeping with the fishes')
	return turns


c1 = Character("Äpik", 200, 150, 70, 70)
c2 = Character("Gämmor", 250, 100, 120, 60)

c1.weapon = Weapon("BFG", 100, 69)
c2.weapon = Weapon("Deku Stick", 120, 1)

turns = run_battle(c1, c2)
print(f"The battle ended in {turns} turns.")
	
		
		
	

		

