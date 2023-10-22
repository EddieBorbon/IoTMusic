# Import necessary modules
import wifi  # Assuming this is a custom module for Wi-Fi (not standard MicroPython)
import usocket
import utime
from machine import Pin, ADC

# Configure Light Dependent Resistor (LDR)
ldr = ADC(Pin(32))
ldr.atten(ADC.ATTN_11DB)  # Set attenuation for full range (3.3v)

# Configure Pure Data host and port
pd_host = "127.0.0.1"
pd_port = 3333

# Connect to Wi-Fi
wifi.wifi_connect()  # Assuming this is a custom function for Wi-Fi connection
print('Executing code')

# Create a UDP socket and connect to Pure Data
pd = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
pd.connect((pd_host, pd_port))
print('Connected to {}:{}'.format(pd_host, pd_port))

# Continuously read LDR values, send to Pure Data, and print
while True:
    # Read LDR value
    ldr_value = ldr.read()

    # Convert LDR value to bytes and send to Pure Data
    pd.send(ldr_value.to_bytes(2, "big"))

    # Print LDR value
    print(ldr_value)

    # Sleep for 20 milliseconds
    utime.sleep_ms(20)
