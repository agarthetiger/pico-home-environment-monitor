# Utility code for using a single button with a Raspberry Pico
from machine import Pin
import time

button = None
debounce_time = 0
button_down = False

def init(gpio_pin, pin_type):
    global button
    button = Pin(gpio_pin, Pin.IN, pin_type)
    return button

def click():
    global debounce_time
    global button_down
    
    # Is the button pressed down, and has it been pressed for the debounce time (mS)?
    if ((button.value() is 0) and (time.ticks_ms()-debounce_time) > 500):
        debounce_time = time.ticks_ms()
        #print("Button Down")
        # For the first time through this loop, when the button is first pressed for longer than the debounce time, set the click event, 
        # Ignore other presses until the button is released
        if (button_down == False): 
            button_down = True
            #print("Button Click event")
            return True
    else:
        #print("Button released")
        button_down = False
        
    return False
