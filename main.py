import asyncio

import network
import socket
import time

from machine import Pin

from micropy_bme280 import BME280
from enhanced_display import Enhanced_Display

import button
import html
import secrets
import wifi

# I2C pin assignments
I2C_SCL = 9
I2C_SDA = 8

# BME280 configuration
BME280_I2C_ADDRESS = 0x76

# OLED configuration
OLED_I2C_ADDRESS = 0x3C
OLED_WIDTH  = 128
OLED_HEIGHT = 64

# Input button pins
BUTTON_PIN = 10 # Change me appropriately

## Onboard package temperature
ONBOARD_TEMP = machine.ADC(4)
ONBOARD_TEMP_CONVERSION_FACTOR = 3.3 / (65535)

# Initialize variables
options = ['temp', 'humidity']
state = 0
# random_value = 0


def pico_package_temp():
    reading = ONBOARD_TEMP.read_u16() * ONBOARD_TEMP_CONVERSION_FACTOR
    return 27 - (reading - 0.706)/0.001721


def i2c_init():
    print(f'Initialising I2C using SDA GPIO pin {I2C_SDA} and SCL GPIO pin {I2C_SCL}')
    i2c=machine.I2C(0,sda=machine.Pin(I2C_SDA), scl=machine.Pin(I2C_SCL), freq=400000)
    i2c_devices = i2c.scan()
    print(f'Found I2C devices with addresses: {i2c_devices}')

    # Initialise BME280 sensor
    print('Initialising BME280...')
    bme = BME280(i2c=i2c)
    print('BME280 initialised')

    print('Initialising oled display...')
    display = Enhanced_Display()
    print('oled initialised')

    # Load the list of fonts to use
    display.load_fonts(['digits-30', 'digits-60', 'text-16', 'icons-32', 'icons-128'])    
    display.fill(0)
    print('I2C devices initialised')

    return bme, display


# Asynchronous function to handle client's requests
async def handle_client(reader, writer):
    print("Client connected")
    request_line = await reader.readline()
    print('Request:', request_line)
    
    # Skip HTTP request headers
    while await reader.readline() != b"\r\n":
        pass
    
    request = str(request_line, 'utf-8').split()[1]
    print('Request:', request)
    
    # Generate HTML response
    response = html.exporter_webpage(
        str(pico_package_temp()),
        bme.temperature, 
        bme.humidity, 
        bme.pressure
    )  

    # Send the HTTP response and close the connection
    writer.write('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    writer.write(response)
    await writer.drain()
    await writer.wait_closed()
    print('Client Disconnected')
    
async def check_button():
    global state
    
    while True:
        # Check button
        if (button.click()):
            if (state == 0):
                state = 1
            else:
                state = 0
            update_oled()
        await asyncio.sleep(0.1)  # Button check interval, seconds


async def update_oled():
    global display
    global bme
    
    while True:
        if (state == 1):
            integer, separator, decimal = bme.humidity.partition('.')
            display.display_humidity(integer)            
        else:
            integer, separator, decimal = bme.temperature.partition('.')
            temp_1dp = f'{integer}{separator}{decimal[0]}'
            display.display_temp(temp_1dp)
        await asyncio.sleep(1)


async def main():    
    print('Starting web server')
    server = asyncio.start_server(handle_client, "0.0.0.0", 80)
    asyncio.create_task(server)
    asyncio.create_task(update_oled())
    asyncio.create_task(check_button())
    
    while True:
        # Add other tasks that you might need to do in the main loop
        await asyncio.sleep(5)


# Main code execution
bme, display = i2c_init()
button.init(10, machine.Pin.PULL_UP)

display.show_msg('Connecting WiFi')
wifi.init(secrets.secrets['ssid'], secrets.secrets['password'])
display.show_msg('WiFi connected')

loop = asyncio.get_event_loop()
loop.create_task(main())

try:
    print('Inside try block')
    loop.run_forever()
except Exception as e:
    print('Error occurred: ', e)
except KeyboardInterrupt:
    print('Program Interrupted by the user')
finally:
    display.show_msg('Bye')
