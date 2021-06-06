################################################################################ CHARACTERS

class Character:
	
	def __init__(self, name) -> None:
		self.name = name

	def __str__(self) -> str:
		return self.name


class Player(Character):
	
	def __init__(self, name, prison, strength, popularity) -> None:
		super().__init__(name)
		self.prison = prison
		self.strength = strength
		self.popularity = popularity


class Inmate(Character):
	
	def __init__(self, name, strength, influence, friendliness) -> None:
		super().__init__(name)
		self.strength = strength
		self.influence  = influence
		self.friendliness = friendliness


class Guard(Character):
	
	def __init__(self, name, friendliness) -> None:
		super().__init__(name)
		self.friendliness = friendliness


################################################################################ PRISON

class Prison:
	
	def __init__(self, rooms) -> None:
		self.rooms = rooms

	def room(self, name):
		return next(filter(lambda room: room.name == name, self.rooms), None)

	def move(self, character, location):
		for room in self.rooms:
			room.occupants.discard(character)
		self.room(location).occupants.add(character)

	def location(self, character):
		for room in self.rooms:
			if character in room.occupants:
				return room


class Room:
	def __init__(self, name) -> None:
		self.name = name
		self.occupants = set()

	def __str__(self) -> str:
		return self.name

	def get_occupants(self, exclude=None):
		room_occupants = self.occupants.copy()
		room_occupants.discard(exclude)
		return room_occupants


################################################################################ SCHEDULE

class Schedule:
	
	def __init__(self, events) -> None:
		self.events = events


class Event:
	
	def __init__(self, location, duration) -> None:
		self.location = location
		self.duration = duration


################################################################################# CONTROLLER

class Controller:

	def __init__(self, player) -> None:
		self.player = player

	def take_input(self):
		player_input = input("Input: ").lower().strip().split(" ")
		if len(player_input) == 1:
			return getattr(self, player_input[0])()
		elif len(player_input) == 2:
			return getattr(self, player_input[0])(player_input[1])

	def move(self, location):
		self.player.prison.move(self.player, location)

	def info(self, question):
		information = {
			"where": f"You are in the {self.player.prison.location(self.player)}",
			"who": f"You are with someone and someone else",
			"when": "The time is something o'clock"
		}
		print(information[question])