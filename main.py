from machine import Pin
import time



class DCmotor:
    def __init__(self,left,right,time=10):
        self.left=   Pin(left,Pin.OUT)
        self.right = Pin(right ,Pin.OUT)

    def move(left,right,mtime=10):
        self.left.value(left)
        self.right.value(right)
        time.sleep(10)

    def __del__(self):
        self.move(0,0,mtime=2)


if __name__=='__main__':
    while True:
        motor(1,0)
    
