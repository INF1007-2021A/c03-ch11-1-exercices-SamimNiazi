class Nombre:
	multiplication = 5
	
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def somme(self):
		return self.x + self.y
	
	@classmethod
	def multiplie(cls, a):
		return a * Nombre.multiplication
	
	@staticmethod
	def soustrait(b, c):
		return b - c
	
	@property
	def x_y(self):
		return self.__x, self.__y
	
	def valeur(self):
		return (self.x, self.y)


liste = [("Jean", "tamere@gmail", 12), ("ouais", "maisnon@", 15), ("Karl", "maisoui@gmail.com", 19),("Marc", "maisoui@gmail.com", 16),("Marc", "maisoui@gmail.com", 16)]
dictionnaire = {}
for element in liste:
	if element[0] in dictionnaire:
		print ("Name Error")
	if element[2] != 16 or not int:
		print( "Value Error")
	else:
		dictionnaire[element[0]] = element[1]

print (dictionnaire)

