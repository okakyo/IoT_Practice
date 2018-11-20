from machine import Pin,pwd
import network,socket,time,urequests
import utime

class Network:
    def __init__(self,name='denx',pwd='roBota5o'):

        self.SSID_name=name
        self.SSID_pwd=pwd

    def setup(name,pwd,timeout=10):

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

    def post_data(self,data,style=None):
        pass


 def motor(self,left,right):
     motor_left.value(left)
     motor_right.value(right)
     time.sleep(1)

if __name__=='__main__':
    Net=Network()
    Net.setup()
    for i in range(4):
        motor(1,0)
    
