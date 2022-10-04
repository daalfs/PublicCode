


import time
import machine

def do()

	button 		= machine.Pin(2, machine.Pin.IN)
	flowmeter 	= machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)
	grinder 	= machine.Pin(0, machine.Pin.OUT)


	while True: 
		if button.value() == 1:
			print(f'grinding for {grindtime} seconds')
			time.sleep(0.1)
			if button.value() == 1:
				grinder.value(1)
				time.sleep(8)
				grinder.value(0)
		time.sleep(0.1)


