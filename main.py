from machine import Pin
import time

pi=Pin(15,Pin.OUT)

while (True):
    pi.value(1)
    time.sleep(0.1)
    pi.value(0)
    time.sleep(0.1)
