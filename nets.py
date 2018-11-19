import socket,network,urequests

SSID_ID=''
SSID_PWD=''

def connected(name,pwd,timeout=10):
    net=network.WLAN(network.STA_IF)
    if net.isconnected():
        print('Already connected.')
        return net
    else:
        net.active(True)
        net.connect(name,pwd)
        while not net.isconnected() or timeout>0:
            print('.')
            utime.sleep()
            timeout-=1
    if net.isconnected():
        print('Connected!')
        return net
    else:
        print('Connection Failed!')
        return null

def slacker():
    pass

if __name__=='__main__':
    connected(SSID_ID,SSID_PWD):
    slacker():
