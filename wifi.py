import network
import machine
import socket
import rp2
import ubinascii
from time import sleep

def init(ssid, password):
    # Toggle an led based on the WiFi connection status
    led = machine.Pin("LED", machine.Pin.OUT)

    rp2.country('GB')
    wlan = network.WLAN(network.STA_IF) # Set as WiFi client, connects to access point.
    # wlan.config(dhcp_hostname = 'PicoW')
    wlan.active(True)
    wlan.config(pm = 0xa11140) # Disable power-saving for WiFi
    wlan.connect(ssid, password)

    # Wait for WiFi connection
    while True:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        sleep(1)
        led.toggle()

    led.on()
    print('WiFi connected.')
    status = wlan.ifconfig()
    print("IP = " + status[0] )
    # print("Hostname = " + str(wlan.config('dhcp_hostname')))
    print("MAC Address = " + ubinascii.hexlify(wlan.config('mac'),':').decode())
    print("Subnet Mask = " + status[1])
    print("Gateway = " + status[2])
    print("DNS Server = " + status[3])
    print("Wifi Channel = " + str(wlan.config('channel')))
    print("Network ESSID = " + str(wlan.config('essid')))
    print("Max Tx Power (dBm) = " + str(wlan.config('txpower')))


def socket_open():
    # Open socket on port 80
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)
    print("Socket opened")

    return s