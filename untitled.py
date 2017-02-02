# Use Raspberry Pi to control Servo Motor motion
# Tutorial URL: http://osoyoo.com/?p=937

import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
# Set the layout for the pin declaration
GPIO.setmode(GPIO.BOARD)
# The Raspberry Pi pin 11(GPIO 18) connect to servo signal line(yellow wire)
# Pin 11 send PWM signal to control servo motion
GPIO.setup(11, GPIO.OUT)

print GPIO.BOARD

# Now we will start with a PWM signal at 50Hz at pin 18. 
# 50Hz should work for many servos very will. If not you can play with the frequency if you like.
Servo = GPIO.PWM(11, 50)						

# This command sets the left position of the servo
Servo.start(2.5)


print "move to the right position:"
Servo.ChangeDutyCycle(12.5)