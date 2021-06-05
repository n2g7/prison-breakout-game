import random
import classes
import storydata

# Initialize player and characters
player = classes.Player("Andy")
guards = {number:classes.Guard(number, random.randint(0,100)) for number in range(1,11)}
inmates = {name:classes.Inmate(name, storydata.inmates[name]["strength"], storydata.inmates[name]["friendliness"]) for name in storydata.inmates.keys()}