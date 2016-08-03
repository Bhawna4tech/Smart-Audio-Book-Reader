#!/usr/bin/python

# Import the modules to send commands to the system and access GPIO pins
import RPi.GPIO as gpio
import os

#Set pin numbering to board numbering
gpio.setmode(gpio.BOARD)

#Set up pin 15 as an input
gpio.setup(13, gpio.IN)  ###GPIO PIN FOR SHUT DOWN

# Set up an interrupt to look for pressed button
gpio.wait_for_edge(13, gpio.FALLING) 
def shut_down():
# Shutdown
	os.system('shutdown now -h')
