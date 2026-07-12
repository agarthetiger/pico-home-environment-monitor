# Raspberry Pico W home environment monitor

This project contains the source code for the Raspberry Pico W at the heart of my home environment monitors. The basic version could be built with a non-WiFi enabled Pico, and simply display the air temperature, humidity or air pressure on the integrated oled display. My Pico-W based version also connects to my WiFi and expose a simple web page which can be scraped by Prometheus for longer term metrics storage and analysis.

# Code

Prototype code is being tested along with the final 3D printed parts and will be uploaded here when complete.

# Part list

The parts required to make this project are as follows:

* Raspberry Pico (Pico W for the Wifi-enabled version)
* 0.96" OLED display. This should be one using the ssd1306 driver chip.
* 6x6x11 push button switch
* M2 x 6mm screws (x4 for fixing the Raspberry Pico)
* M3 x 16mm screws (x2 to secure the button)
* M3 x 8mm screws (x2 to secure the display)
* M3 x 20mm bolts (x2 to secure the clamshell halves together) 
* M3 x Xmm bolts (x4 to secure the clamshell to the base)
* M3 heatset inserts (x6 for the M3 bolts)
* BME280 sensor
* Micro-USB cable and USB power supply

# 3D printing files

The Fusion 360 files as well as step files will be available on thingiverse once the final (first) release version has been confirmed.

# Flashing the Pico

You will need to add your WiFi SSID and password to the `wifi.py` file prior to copying this onto your Pico W in order to scrape the metrics. If these are not set the WiFi setup will be skipped and the unit will act as a local device.

# To Do

* Button press cycles through IP and MAC address
* Button press does not repeat when holding the button down
* Update README with complete hardware
* Add secrets.txt file as an example of how to add WiFi credentials and update README
* Upload stl and fusion files to Printables and link to them from here
* Add links and thanks to all the sources of code and tutorials used during this project
* Update metrics html with raw sensor values as well as new lines and check with Prometheus the scrape is still working afterwards
