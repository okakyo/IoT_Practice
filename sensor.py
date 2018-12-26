from machine import Pin
import math,time
"""

 いかに赤外センサーを使えるようにするかについて記述する必要がある。
   => クラスにした方が、それぞれのセンサーに対応できる。

今後の目標：
    ・'sensor'ベースクラスに 子クラスを継承させていく。
    ・ラズパイをメインサーバーをして、ESPより逐次データを送信させていく。
    ・受信したデータをCSV,json でまとめていく。

"""
class Base:
    def __init__(self,p1,p2):
        self.p1=Pin(p1,Pin.In)
        self.p2=Pin(p2,Pin.Out)

    def calculate(self):
        
        return 


    def main(self):
        pass


class Observe:
    def __init__(self,p1):


    def calculate(self):
        pass

    def main(self):
        pass

class Redsensor:
    def __init__(self):
        pass
    def calculate(self):
        pass
    def main():
        pass
class Pressure:
    def __init__(self,p1,p2):
        pass
    def calclate(self):
        pass
    def main():
        pass


class Meteograph:
    def __init__(self):
        pass
    def observe(self):
        pass
    def main(self):
        pass

class Sounds:
    def __init__(self):
        pass
    def teardown(self):
        pass
    def play(self):
        pass
    
    def raise(self):
        pass

    def failing(self):
        pass

    def main(self):
        pass


class Wave:
    
    def __init__(self,p1,p2):
        
        self.trig=Pin(p1,Pin.OUT)
        self.echo=Pin(p2,Pin.IN)

    def calculate(self):
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
                print(selfcalculate())
            except RuntimeError:
                pass
            time.sleep(1)

if __name__=='__main__':
    wave=Wave(6,7)
    wave.main()
