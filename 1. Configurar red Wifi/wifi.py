import network
import time

SSID = 'WRITE YOUR NAME NETWORK HERE'
PASS = 'WRITE YOUR PASSWORD NETWORK HERE'
CONNECTING_TRIES = 3

def wifi_connect():

    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    print('Connecting to "{}"'.format(SSID))
    wifi.connect(SSID, PASS)
    time.sleep(5)
    if wifi.isconnected():
        print('Connection Succesfully to "{}"'.format(SSID))
        return True
    wifi.disconnect()
    print('Connection Error')
    return False
