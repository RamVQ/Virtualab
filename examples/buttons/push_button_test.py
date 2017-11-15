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

	while True:
		
		#testing
		time.sleep(1) #delay in seconds	
		if (GPIO.input(PUSH_BUTTON) == True)
			print "button has been pressed"
			#end of  if		

	#end of while

#######END OF FUNCT DEFINITION##################

#######SCRIPT EXECUTION#########################

main()		













