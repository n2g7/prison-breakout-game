import gamedata
import gameclasses


prison = gameclasses.Prison(
	rooms=[gameclasses.Room(
		name=room["name"]
	) for room in gamedata.rooms]
)

schedule = gameclasses.Schedule(
	events=[gameclasses.Event(
		location=event["location"],
		duration=event["duration"]
	) for event in gamedata.schedule]
)

player = gameclasses.Player(
	name="Andy", 
	prison=prison,
	strength=100, 
	popularity=0
)

controller = gameclasses.Controller(player)


inmates = [gameclasses.Inmate(
	name=inmate["name"],
	strength=inmate["strength"],
	friendliness=inmate["friendliness"],
	influence=inmate["influence"]
) for inmate in gamedata.inmates]


guards = [gameclasses.Guard(
	name=guard["name"],
	friendliness=guard["friendliness"]
) for guard in gamedata.guards]



while True:
	# print(" ".join([f"[{room.name}: {', '.join([inmate.name for inmate in room.occupants]) if room.get_occupants() else 'Empty'}]" for room in prison.rooms]))
	controller.take_input()