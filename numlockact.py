import evdev
from evdev import categorize,UInput, AbsInfo, ecodes as e
import time
ui = UInput()
touch=evdev.InputDevice('/dev/input/event24')
x=int(0)
y=int(0)
numt1=time.time()
numl=False
for event in touch.read_loop():
	if(event.value==1):
		numt1=time.time()
	if(event.type==e.EV_ABS):
		absevent=categorize(event)
		if(e.bytype[absevent.event.type][absevent.event.code]=='ABS_X'):
			# print("X:{}",format(absevent.event.value))
			x=absevent.event.value
		if(e.bytype[absevent.event.type][absevent.event.code]=='ABS_Y'):
			y=absevent.event.value
			# print("Y:{}",format(absevent.event.value))
		diff=time.time()-numt1
		
		if(x<400 and y<300 and diff>2):
			diff=0
			numt1=0
			ui.write(e.EV_KEY, e.KEY_NUMLOCK,1)
			ui.syn()
			ui.write(e.EV_KEY, e.KEY_NUMLOCK, 0)
			ui.syn()
