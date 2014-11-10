#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import subprocess
import os

GPIO.setmode(GPIO.BCM)

counter = 0

# set buttons as input, with pull-up resistor
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# set up backlight GPIO  
os.system("sudo sh -c 'echo 252 > /sys/class/gpio/export'")

oldButtonState = True
while True:
    buttonState1 = GPIO.input(23)
    buttonState2 = GPIO.input(18)
    buttonState3 = GPIO.input(27)
    buttonState4 = GPIO.input(22)

    # Enciende/Apaga la pantalla
    if buttonState1 != oldButtonState and buttonState1 == False :
       if (counter == 0):
          subprocess.call("sudo sh -c 'echo 'out' > /sys/class/gpio/gpio252/direction'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          counter = 1
          oldButtonState = buttonState1
          time.sleep(0.5)
       
       elif (counter == 1) or (counter == 3):
          subprocess.call("sudo sh -c 'echo '1' > /sys/class/gpio/gpio252/value'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          counter = 2
          oldButtonState = buttonState1
          time.sleep(0.5)
       
       elif (counter == 2):
          subprocess.call("sudo sh -c 'echo '0' > /sys/class/gpio/gpio252/value'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          counter = 3
          oldButtonState = buttonState1
          time.sleep(0.5)
    
    # print "Apaga la Raspberry Pi" 
    if buttonState2 != oldButtonState and buttonState2 == False :
       subprocess.call("sudo poweroff", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    oldButtonState = buttonState2
    time.sleep(.1)

    if buttonState3 != oldButtonState and buttonState3 == False :
        # print "Button 2 pressed"
       subprocess.call("service amule-daemon start", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    oldButtonState = buttonState3
    time.sleep(.1)

    if buttonState4 != oldButtonState and buttonState4 == False :
        # print "Button 3  pressed"
       subprocess.call("echo boton4 >> /tmp/aa", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    oldButtonState = buttonState4
    time.sleep(.1)
