#!/usr/bin/python3

"""
shutdown(/power on) Raspberry Pi with pushbutton
"""

import subprocess
import time
import RPi.GPIO as GPIO

# pushbutton connected to this GPIO pin, using pin 5 also has the benefit of
# waking / powering up Raspberry Pi when button is pressed
SHUTDOWN_PIN = 5

def shutdown():
    """
    handling system shutdown
    """

    print("Running poweroff command")
    subprocess.run(['poweroff'])

def setup():
    """
    handling script setup
    """

    print("Setting up shutdown pin")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SHUTDOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # subscribe to button presses
    GPIO.add_event_detect(SHUTDOWN_PIN, GPIO.RISING, callback=shutdown, bouncetime=200)

setup()
print("Ready")
while True:
    # sleep to reduce unnecessary CPU usage
    time.sleep(5)
