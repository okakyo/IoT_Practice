from machine import Pin
import math,time

#いかに赤外センサーを使えるようにするかについて記述する必要がある。
# => クラスにした方が、それぞれのセンサーに対応できる。

class Base_Sensors:
    def __init__(self,pin,w_time=10):
        self.w_time=w_time
        self.sensor=Pin(pin,Pin.IN)

    def calculate(self):
        pass

    def main(self):
        pass

class Sonic(Base_Sensors):
    def __init__(self,pin):
        super().__init__(pin)
    
    def calculate(self):
        

    def main(self):
        pass

class Light(Base_Sensors):
    def __init__(self,pin):
        super().__init__(pin)

class Temperature(Base_Sensors):
    def __init__(self,pin):
        super().__init__(pin)

class Gyro(Base_Sensors):
    def __init__(self,pin):
        super().__init__(pin)

class Accel(Base_Sensors):
    def __init__(self,pin):
        super().__init__(pin)


def main():
    pin=10
    sensor=Sonic(pin)
    while True:

        print(send_pin)

if __name__=='__main__':
   main()


