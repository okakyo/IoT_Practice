from machine import Pin,PWM
import time

class Motor:
    def __init__(self,pin1,pin2,kind='dc'):
        self.kind=kind
        if kind=='dc' or kind=='step':
            self.left=Pin(pin1,Pin.OUT)
            self.right=Pin(pin2,Pin.OUT)
        elif kind=='servo':
            self.left=PWM(Pin(pin1),freq=50,duty=77)
            self.right=None
        else:
            raise()

    def main(self,v1,v2,wtime=5):
        if self.kind=='dc' or self.kind=='step':
            self.left.value(v1)
            self.right.value(v0)
        
        elif self.kind=='servo':
            self.left.duty()
        
        time.sleep(wtime)

    def __del__(self):
        if self.kind=='dc' or self.kind=='step':
            self.main(0,0)

if __name__=='__main__':
    #最後に書かれたmotor(0,1)は、下のように書かれている場合、一秒実行されることはないから注意。 
    motor=Motor(15,9)
    motor.move(1,0)
    motor.move(0,1)

    del motor
    
