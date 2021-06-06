# Player class
class Player:
	strength = 100
	popularity = 10
	static_inventory = []
	mobile_inventory = []

	def __init__(self, name, prison) -> None:
		self.name = name
		self.prison = prison


# Inmate class
class Inmate:

	def __init__(self, name, prison, strength, friendliness) -> None:
		self.name = name
		self.prison = prison
		self.strength = strength
		self.friendliness = friendliness


# Prison guard class
class Guard:

	def __init__(self, number, prison, friendliness) -> None:
		self.number = number
		self.prison = prison
		self.friendliness = friendliness


# Prison class
class Prison:

	def __init__(self, room_names) -> None:
		self.rooms = {name: {"occupants": [], "assets": []} for name in room_names}

	def __str__(self) -> str:
		return "Adironacks Correctional Facility"
