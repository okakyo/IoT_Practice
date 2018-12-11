from machine import Pin
import math,time

#�����ɐԊO�Z���T�[���g����悤�ɂ��邩�ɂ��ċL�q����K�v������B
# => �N���X�ɂ��������A���ꂼ��̃Z���T�[�ɑΉ��ł���B

def setup():
    global trig,echo
    trig=Pin(7,Pin.OUT)
    echo=Pin(6,Pin.IN)

def read():
    global trig,echo
    t1=t2=None
    tick=0.0001
    trig.value(1)
    time.sleep(0.00001)
    trig.value(0)
    for _ in range(10000):
        if echo.value():
            t1=time.ticks_us()
            break
        time.sleep(tick)

    if not  t1:
        raise RuntimeError

    for _ in range(10000):
        if not echo.value():
            t2=time.ticks_us()
            break
        time.sleep(tick)
    if not t2:
        raise RuntimeError

    return float(0.017*(t2-t1))
        
def main():
    setup()
    while True:
        try:
            print(read())
        except RuntimeError:
            pass
        time.sleep(1)

