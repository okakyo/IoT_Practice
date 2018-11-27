from machine import Pin
import time


pin_left=Pin(15,Pin.OUT)
pin_right=Pin(9,Pin.OUT)

def motor(left,right):
    pin_left.value(left)
    pin_right.value(right)
    time.sleep(1)

if __name__=='__main__':
    #最後に書かれたmotor(0,1)は、下のように書かれている場合、一秒実行されることはないから注意。 

    motor(1,0)
    motor(0,1)
    time.sleep(1)
    
