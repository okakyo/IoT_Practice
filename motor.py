from machine import Pin,PWM
import utime
import cmath



pin_left=Pin(15,Pin.OUT)
pin_right=Pin(10,Pin.OUT)
pin_servo=Pin(8,Pin.OUT)
servo=PWM(pin_servo,freq=2000,duty=100)

def motor(left,right):
    pin_left.value(left)
    pin_right.value(right)
    time.sleep(1.0)

def servo():
    @pass 

if __name__=='__main__':
    pass

