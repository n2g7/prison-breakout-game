import gamedata
import gameclasses


prison = gameclasses.Prison(rooms=[gameclasses.Room(**room_data) for room_data in gamedata.rooms])
schedule = gameclasses.Schedule(events=[gameclasses.Event(**event_data) for event_data in gamedata.schedule])

player = gameclasses.Player(name="Andy", prison=prison, strength=100, popularity=0)
inmates = [gameclasses.Inmate(**inmate_data) for inmate_data in gamedata.inmates]
guards = [gameclasses.Guard(**guard_data) for guard_data in gamedata.guards]

controller = gameclasses.Controller(player)

while True:
	# print(" ".join([f"[{room.name}: {', '.join([inmate.name for inmate in room.occupants]) if room.get_occupants() else 'Empty'}]" for room in prison.rooms]))
	controller.take_input()