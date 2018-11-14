from machine import Pin
import time


pin_left=Pin(15,Pin.OUT)
pin_right=Pin(10,Pin.OUT)


def motor(left,right):

    pin_left.value(left)
    pin_right.value(right)


for i in range(3):
    motor(1,0)
    time.sleep(0.5)
    motor(0,0)
    time.sleep(0.5)
    motor(0,1)
    time.sleep(0.5)
    motor(0,0)
    time.sleep(0.5)

