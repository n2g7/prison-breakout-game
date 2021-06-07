import gamedata
import gameclasses


prison = gameclasses.Prison(rooms=[gameclasses.Room(**room_data) for room_data in gamedata.rooms])
schedule = gameclasses.Schedule(events=[gameclasses.Event(**event_data) for event_data in gamedata.schedule], prison=prison)

player = gameclasses.Player(name="Andy", prison=prison, schedule=schedule, strength=100, popularity=0)
prison.inmates = [gameclasses.Inmate(**inmate_data) for inmate_data in gamedata.inmates] + [player]
prison.guards = [gameclasses.Guard(**guard_data) for guard_data in gamedata.guards]

controller = gameclasses.Controller(player)


for inmate in prison.inmates:
	prison.move(inmate, "cells")


while True:
	controller.take_input()
	schedule.next_action()