from machine import Pin

pin_left=Pin(15,Pin.OUT)
pin_right=Pin(10,Pin.OUT)

def motor(left,right):
    pin_left.value(left)
    pin_right.value(right)
    time.sleep(1.0)

if __name__=='__main__':
    motor(1,0)
