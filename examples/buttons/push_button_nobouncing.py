#!/usr/bin/python

#######1.IMPORTS###################################

import RPi.GPIO as GPIO
import time

#######END OF IMPORTS############################


######2.SCRIPT CONST###############################

PUSH_BUTTON = 24 # GPIO  assigned to push button. BCM 24 (physical pin 18)

#######END OF SCRIPT CONST######################

#######3.FUNCT DEFINITON##########################

###main
def main():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(PUSH_BUTTON,GPIO.IN)#LED pin setup
	current_state = True;
	
	while True:
	
		if (current_state == True):
			if (GPIO.input(PUSH_BUTTON) == False):
				current_state = False;
				time.sleep(0.05)
				print "button pressed"
		else:
			if (GPIO.input(PUSH_BUTTON) == True):
				current_state = True;
				time.sleep(0.05)

	#end of while

#######END OF FUNCT DEFINITION##################

#######SCRIPT EXECUTION#########################

main()		













