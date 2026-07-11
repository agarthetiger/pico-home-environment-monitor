# Utility code for using a single button with a Raspberry Pico
from machine import Pin
import time

button = None
debounce_time = 0
button_down = False

def init(gpio_pin, pin_type):
    # Buttons are always inputs
    global button
    button = Pin(gpio_pin, Pin.IN, pin_type)
    return button

def button_click():
    global debounce_time
    global button_down
    
    if ((button.value() is 0) and (time.ticks_ms()-debounce_time) > 300):
        debounce_time = time.ticks_ms()
        #print("Button Down")
        if (button_down == False): 
            button_down = True
            #print("Button Click event")
            return True
    else:
        #print("Button released")
        button_down = False
        
    return False
