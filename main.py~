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

class DCmotor:
    def __init__(self,left,right,time=10):
        self.left=   Pin(left,Pin.OUT)
        self.right = Pin(right ,Pin.OUT)

    def move(left,right,mtime=10):
        self.left.value(left)
        self.right.value(right)
        time.sleep(10)

    def __del__(self):
        self.move(0,0)


if __name__=='__main__':
    Net=Network()
    Net.setup()
    while True:
        motor(1,0)
    
