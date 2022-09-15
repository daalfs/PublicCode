from machine import Pin, ADC
import utime

def blink(n=9):
    for i in range(n):
        p = Pin('LED',Pin.OUT) #'LED' voor picow
        
        p.value(1)
        utime.sleep(0.2)
        p.value(0)
        utime.sleep(0.3)

