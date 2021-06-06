import random
import classes
import storydata

# Initialize variables
guard_count = 10

# Initialize prison
prison = classes.Prison(["Cells", "Cafeteria", "Yard", "Laundry", "Library", "Solitary", "Office"])

# Initialize player and characters
player = classes.Player("Andy", prison)
guards = {number:classes.Guard(number, prison, random.randint(0,100)) for number in range(1, guard_count + 1)}
inmates = {name:classes.Inmate(name, prison, storydata.inmates[name]["strength"], storydata.inmates[name]["friendliness"]) for name in storydata.inmates.keys()}