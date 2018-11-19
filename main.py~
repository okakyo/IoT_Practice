from machine import Pin,pwd
import network,socket,time,urequests
import utime

ml_pin=15
mr_pin=10
led_1=1
led_2=2

sensor_1=3
sensor_2=4
sensor_3=5
sensor_4=6
sensor_5=7

SSID_name='denx'
SSID_pwd='roBota5o'

def wifi(name,pwd,timeout=10):

    net=network.WLAN(network.STA_IF)
    if wifi.isconnected():
        print('Already connected. connect skip')
        return net
    else:
        wifi.active(True)
        wifi.connect(name,pwd)
        while not wifi.isconnected() or timeout>0:
            print('.')
            utime.sleep(1)
            timeout-=1
    if wifi.isconnected():
        print('Connected !')
        return wifi
    else:
        print ('Connection Failed !')
        return null


motor_left=Pin(ml_pin,Pin.OUT)
motor_right=Pin(mr_pin,Pin.OUT)
led1=Pin(led_1,Pin.OUT)
led2=Pin(led_2,Pin.OUT)

def motor(left,right):
    motor_left.value(left)
    motor_right.value(right)
    time.sleep(1)

def servo(value):
    pass    

def micro_wave(value):
    pass

def red_wave(value):
    pass

class Send_data:

    def __init__(self):
        self.url=''
        self.json=''

    def send_data(self):
        pass
    
    def parse_data(self):
        pass 



if __name__=='__main__':
    pass

