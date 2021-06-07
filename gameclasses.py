import signal

################################################################################ CHARACTERS

class Character:
	
	def __init__(self, name) -> None:
		self.name = name

	def __str__(self) -> str:
		return self.name


class Player(Character):
	
	def __init__(self, name, schedule, prison, strength, popularity) -> None:
		super().__init__(name)
		self.prison = prison
		self.schedule = schedule
		self.strength = strength
		self.popularity = popularity

	def talk(self, inmate):
		print(f'"Hey, {self.prison.inmate(inmate)}, how ya doin"')

	def bribe(self, guard):
		print(f'"Say, {self.prison.guard(guard)} - here\'s a proposish"')


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
		self.guards = set()
		self.inmates = set()

	def room(self, name):
		return next(filter(lambda room: room.name == name, self.rooms), None)

	def inmate(self, name):
		return next(filter(lambda inmate: inmate.name == name, self.inmates), None)

	def guard(self, name):
		return next(filter(lambda guard: guard.name == name, self.guards), None)

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
	
	def __init__(self, events, prison) -> None:
		self.events = events
		self.prison = prison
		self.event_counter = 0
		self.action_counter = 0

	def current_event(self):
		return self.events[self.event_counter]

	def next_event(self):
		self.event_counter = self.event_counter + 1 if self.event_counter < len(self.events) - 1 else 0
		for inmate in self.prison.inmates:
			self.prison.move(inmate, self.current_event().location)

	def next_action(self):
		self.action_counter += 1
		if self.action_counter >= self.current_event().duration:
			self.action_counter = 0
			self.next_event()


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

	def talk(self, inmate):
		self.player.talk(inmate)

	def bribe(self, guard):
		self.player.bribe(guard)

	def info(self, question):
		location = self.player.prison.location(self.player)
		other_inmates = self.player.prison.location(self.player).get_occupants(exclude=self.player)
		other_inmates_formatted = ", ".join([inmate.name for inmate in other_inmates]) if other_inmates else "no one else"
		information_strings = {
			"where": f"You are in the {location}",
			"who": f"You are with {other_inmates_formatted}",
			"when": f"{self.player.schedule.action_counter} of {self.player.schedule.current_event().duration} interactions left"
		}
		print(information_strings[question])