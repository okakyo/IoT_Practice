from machine import Pin,PWM
import time


pin_left=Pin(15,Pin.OUT)
pin_right=Pin(10,Pin.OUT)
pin_servo=Pin(8,Pin.OUT)
servo=PWM(pin_servo,freq=2000,duty=100)

def motor(left,right):

    pin_left.value(left)
    pin_right.value(right)
    time.sleep(1.0)

def servo():
    servo.pwm()
    time.sleep(1.0)

for i in range(3):
    motor(1,0)
    motor(0,0)
    motor(0,1)
    motor(0,0)

