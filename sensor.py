from machine import Pin
import math

#いかに赤外センサーを使えるようにするかについて記述する必要がある。
# => クラスにした方が、それぞれのセンサーに対応できる。

class Base_Sensors:
    def __init__(self,pin,w_time=10):
        self.w_time=w_time
        self.sensor=Pin(pin,Pin.INPUT)

    def calculate(self):
        pass

    def main(self):
        pass

class Sonic(Base_Sensors):
    def __init__(self,pin):
        super().__init__(pin)
    
    def calculate(self):
        pass

    def main(self):
        pass

class Light(Base_Sensors):
    pass

class Temperature(Base_Sensors):
    pass

class Gyro(Base_Sensors):
    pass

class Accel(Base_Sensors):
    pass


def main():
    send_pin=Pin(10,Pin.INPUT)
    while True:

        print(send_pin)

if __name__=='__main__':
   main()


