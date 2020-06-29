import evdev
from evdev import categorize,UInput, AbsInfo, ecodes as e

ui = UInput()
touch=evdev.InputDevice('/dev/input/event24')
for event in touch.read_loop():
	if(event.type==e.EV_ABS):
		absevent=categorize(event)
		if(e.bytype[absevent.event.type][absevent.event.code]=='ABS_X'):
			# print("X:{}",format(absevent.event.value))
			x=absevent.event.value
		if(e.bytype[absevent.event.type][absevent.event.code]=='ABS_Y'):
			y=absevent.event.value
			# print("Y:{}",format(absevent.event.value))
		if(event.value==-1):
			if(x<400 and y<300):
				ui.write(e.EV_KEY, e.KEY_7,1)
				ui.syn()
				ui.write(e.EV_KEY, e.KEY_7, 0)
				ui.syn()
			if(x>700 and y<200):
				ui.write(e.EV_KEY, e.KEY_8,1)
				ui.syn()
				ui.write(e.EV_KEY, e.KEY_8, 0)
				ui.syn()

						
