import random
import classes
import storydata

# Initialize variables
guard_count = 10

# Initialize prison
prison = classes.Prison(storydata.rooms)

# Initialize schedule
schedule = classes.Schedule(storydata.schedule)

# Initialize player and characters
player = classes.Player("Andy", prison)
guards = {number:classes.Guard(number, prison, random.randint(0,100)) for number in range(1, guard_count + 1)}
inmates = {name:classes.Inmate(name, prison, storydata.inmates[name]["strength"], storydata.inmates[name]["friendliness"], storydata.inmates[name]["dialogues"]) for name in storydata.inmates.keys()}

# Initialize controller
controller = classes.Controller(player)

# Initialize character positions
prison.rooms["cells"].occupants.append(player)
prison.rooms["cells"].occupants.extend(list(inmates.values()))

while True:
	action_counter = 0
	print(schedule.current_event())
	while action_counter < schedule.current_event().duration:
		if controller.get_input() in ["interacted", "bribed"]:
			action_counter += 1
	schedule.progress()