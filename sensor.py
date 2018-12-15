from machine import Pin
import math,time

#いかに赤外センサーを使えるようにするかについて記述する必要がある。
# => クラスにした方が、それぞれのセンサーに対応できる。

class Wave:
    
    def __init__(self,p1,p2):
        self.trig=Pin(p1,Pin.OUT)
        self.echo=Pin(p2,Pin.IN)

    def __read(self):
        t1=t2=None
        tick=0.0001
        self.trig.value(1)
        time.sleep(0.00001)
        self.trig.value(0)
        for _ in range(10000):
            if self.echo.value():
                t1=time.ticks_us()
                break
            time.sleep(tick)

        if not  t1:
            raise RuntimeError

        for _ in range(10000):
            if not self.echo.value():
                t2=time.ticks_us()
                break
            time.sleep(tick)
        if not t2:
            raise RuntimeError

        return float(0.017*(t2-t1))
            
    def main(self):
        while True:
            try:
                print(self.__read())
            except RuntimeError:
                pass
            time.sleep(1)

if __name__=='__main__':
    wave=Wave(33,25)
    wave.main()
