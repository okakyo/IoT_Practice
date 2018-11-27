from machine import Pin
import network,socket,time,urequests
import utime

class Network:
    def __init__(self,name='denx',pwd='roBota5o'):

        self.SSID_name=name
        self.SSID_pwd=pwd

    def setup(self,timeout=10):

        wifi=network.WLAN(network.STA_IF)

        if wifi.isconnected():
            print('Already connected. connect skip')
            return net
        else:
            wifi.active(True)
            wifi.connect(self.SSID_name,self.SSID_pwd)
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

    def post_data(self,data,style=None): 
        html=''
        if wifi.isconnected:
            urequests.post(html,data=data)


def motor(left,right):
    motor_left=Pin(15,Pin.OUT)
    motor_right=Pin(10,Pin.OUT)
    motor_left.value(left)
    motor_right.value(right)

if __name__=='__main__':
    Net=Network()
    Net.setup()
    while True:
        motor(1,0)
    
