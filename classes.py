# Player class
class Player:
	strength = 100
	popularity = 10
	static_inventory = []
	mobile_inventory = []

	def __init__(self, name) -> None:
		self.name = name


# Inmate class
class Inmate:

	def __init__(self, name, strength, friendliness) -> None:
		self.name = name
		self.strength = strength
		self.friendliness = friendliness


# Prison guard class
class Guard:

	def __init__(self, number, friendliness) -> None:
		self.number = number
		self.friendliness = friendliness
