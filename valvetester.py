
def do():
	import framebuf
	import time
	import machine
	from ssd1306 import SSD1306_I2C

	class scale(hx711.HX711):

	    def __init__(self, d_out, pd_sck):
	        super(scale, self).__init__(d_out, pd_sck)
	        self.offset = 0

	    def value(self):
	        x = 0
	        for i in range(10):
	            time.sleep(0.01)
	            x += self.read()

	        x = (x/10-51300)/200
	        return x


	i2c = I2C(0, scl=Pin(4), sda=Pin(5), freq=200000)
	oled = SSD1306_I2C(128, 64, i2c)                  
	scale = scale(d_out=18, pd_sck=19)
	button = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_DOWN )
	tare = 0

	while True:
	    text = scale.value()    
	    if button.value() == 1:
	    	time.sleep(0.1)
	    	if button.value() == 1:
				tare = scale.value() 
				print(tare)

		text = text - tare
	    print(text)
		oled.fill(0)
		oled.text(text,10,40)
	    oled.show()

	    time.sleep(0.1)





