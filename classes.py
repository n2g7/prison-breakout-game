import random
import utilities

# Player class
class Player:
	strength = 100
	popularity = 10
	static_inventory = []
	mobile_inventory = []

	def __init__(self, name, prison, schedule) -> None:
		self.name = name
		self.prison = prison
		self.schedule = schedule

	def __str__(self) -> str:
		return self.name

	def get_location(self):
		for room in self.prison.rooms.values():
			if self in room.occupants:
				return room

	def move(self, new_room):
		if new_room in self.prison.rooms:
			self.get_location().occupants.remove(self)
			self.prison.rooms[new_room].occupants.append(self)
			return "moved"
		else:
			print("No such room")

	def bribe(self):
		print("How's 'bout I make you an offer you can't refuse?")
		return "bribed"

	def interact(self):
		if len(self.get_location().other_occupants(self)) > 0:
			other_inmate = random.choice(self.get_location().other_occupants(self))
			print("You: Hey")
			print(f"{other_inmate.name}: {random.choice(other_inmate.dialogues)}")
			return "interacted"
		else:
			print("I'm alone")


# Inmate class
class Inmate:

	def __init__(self, name, prison, strength, friendliness, dialogues) -> None:
		self.name = name
		self.prison = prison
		self.strength = strength
		self.friendliness = friendliness
		self.dialogues = dialogues

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

	def other_occupants(self, person):
		other_occupants = self.occupants.copy()
		other_occupants.remove(person)
		return other_occupants


# Controller class
class Controller:

	def __init__(self, player) -> None:
		self.player = player

	def get_input(self):
		player_input = input("Input: ").lower().strip().split(" ")
		try:
			if len(player_input) == 1:
				return getattr(self, player_input[0])()
			elif len(player_input) == 2:
				return getattr(self, player_input[0])(player_input[1])
		except:
			print("Error")
	
	
	def goto(self, location):
		return self.player.move(location)

	def talk(self, person):
		if person == "guard":
			return self.player.bribe()
		elif person == "inmate":
			return self.player.interact()
		else: 
			print("No such person")

	def info(self, information):
		if information == "when":
			event = self.player.schedule.current_event()
			print(f"{self.player.schedule.action_counter} of {event.duration} units")
		elif information == "where":
			print(f"You are in the {self.player.get_location()}")
		else: 
			print("No such information")


# Schedule class
class Schedule:
	event_counter = 0
	action_counter = 0

	def __init__(self, events) -> None:
		self.events = [Event(event["location"], event["duration"]) for event in events]

	def current_event(self):
		return(self.events[self.event_counter])

	def increment_event(self):
		self.event_counter = utilities.loopback_increment(self.event_counter, len(self.events) - 1)
		print(self.current_event())

	def increment_action(self):
		self.action_counter = utilities.loopback_increment(self.action_counter, self.current_event().duration)
		

# Eent class
class Event:

	def __init__(self, location, duration) -> None:
		self.location = location
		self.duration = duration

	def __str__(self) -> str:
		return f"{self.location} for {self.duration} units"