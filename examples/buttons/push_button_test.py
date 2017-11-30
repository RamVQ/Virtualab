#!/usr/bin/python

#######1.IMPORTS###################################

import RPi.GPIO as GPIO
import time

#######END OF IMPORTS############################


######2.SCRIPT CONST###############################

PUSH_BUTTON = 14 # GPIO  assigned to push button. BCM 14 (physical pin 8)

#######END OF SCRIPT CONST######################

#######3.FUNCT DEFINITON##########################

###main
def main():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(PUSH_BUTTON,GPIO.IN)#Button pin setup
	current_state = True;
	
	while True:

		#detecting if button was pressed
		if (GPIO.input(PUSH_BUTTON) == False):
			print "button has been pressed"
			time.sleep(1) #delay to prevent bouncing 

	#end of while

#######END OF FUNCT DEFINITION##################

#######SCRIPT EXECUTION#########################

main()		













