# Raspberry Pico W home environment monitor

This project contains the source code for the Raspberry Pico W at the heart of my home environment monitors. The basic version could be built with a non-WiFi enabled Pico, and simply display the air temperature, humidity or air pressure on the integrated oled display. My Pico-W based version also connects to my WiFi and expose a simple web page which can be scraped by Prometheus for longer term metrics storage and analysis.

# Code

Prototype code is being tested along with the final 3D printed parts and will be uploaded here when complete.

# Part list

The parts required to make this project are as follows:

* Raspberry Pico (Pico W for the Wifi-enabled version)
* 0.96" OLED display. This should be one using the ssd1306 driver chip.
* 6x6x11 push button switch
* M2 screws
* M3 screws
* M3 hex bolts
* M3 heatset inserts
* BME280 sensors
* Micro-USB cable and power supply

# 3D printing files

The fusion 360 files as well as step files will be available on thingiverse once the final version has been comfirmed.

# Flashing the Pico

You will need to add your WiFi SSID and password to the `wifi.py` file prior to copying this onto your Pico W in order to scrape the metrics. If these are not set the WiFi setup will be skipped and the unit will act as a local device.
