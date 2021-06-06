# Player class
class Player:
	strength = 100
	popularity = 10
	static_inventory = []
	mobile_inventory = []

	def __init__(self, name, prison) -> None:
		self.name = name
		self.prison = prison

	def __str__(self) -> str:
		return self.name

	def move(self, new_room):
		if new_room in self.prison.rooms:
			for room in self.prison.rooms.values():
				if self in room.occupants:
					room.occupants.remove(self)
			self.prison.rooms[new_room].occupants.append(self)
		else:
			print("No such room")
		

# Inmate class
class Inmate:

	def __init__(self, name, prison, strength, friendliness) -> None:
		self.name = name
		self.prison = prison
		self.strength = strength
		self.friendliness = friendliness

	def __str__(self) -> str:
		return self.name


# Prison guard class
class Guard:

	def __init__(self, number, prison, friendliness) -> None:
		self.number = number
		self.prison = prison
		self.friendliness = friendliness

	def __str__(self) -> str:
		return self.number


# Prison class
class Prison:

	def __init__(self, room_names) -> None:
		self.rooms = {name:Room(name, [], []) for name in room_names}

	def __str__(self) -> str:
		return "Adironacks Correctional Facility"


# Room class
class Room:

	def __init__(self, name, assets, occupants) -> None:
		self.name = name
		self.assets = assets
		self.occupants = occupants

	def __str__(self) -> str:
		return self.name


# Controller class
class Controller:

	def __init__(self, player) -> None:
		self.player = player

	def get_input(self):
		player_input = input("Input: ").lower().strip().split(" ")
		try:
			if len(player_input) == 1:
				getattr(self, player_input[0])()
			elif len(player_input) == 2:
				getattr(self, player_input[0])(player_input[1])
			else:
				print("Invalid arguments")
		except TypeError:
			print("Invalid arguments")
		except AttributeError:
			print("Invalid command")
	
	def goto(self, location):
		self.player.move(location)