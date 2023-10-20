import wifi
import usocket
import utime
from machine import Pin, ADC


pot = ADC(Pin(32))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

pd_host = '192.168.43.90'
pd_port = 8888
wifi.wifi_connect()
print('Executing code')
pd = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
pd.connect((pd_host, pd_port))
print('Connected to {}:{}'.format(pd_host, pd_port))
while True:
    pot_value = pot.read()
    pd.send(pot_value.to_bytes(8,"big"))
    utime.sleep_ms(200)
