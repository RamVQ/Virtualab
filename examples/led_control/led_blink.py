#!/usr/bin/python

#######1.IMPORTS###################################

import RPi.GPIO as GPIO
import time

#######END OF IMPORTS############################


######2.SCRIPT CONST###############################

LED = 4 #BCM GPIO  assigned to led

#######END OF SCRIPT CONST######################

#######3.FUNCT DEFINITON##########################

###main
def main():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED,GPIO.OUT)#LED pin setup

	while True:
		
		#testing
		
		GPIO.output(LED,GPIO.LOW)
		time.sleep(1) #delay in seconds	
		GPIO.output(LED,GPIO.HIGH)
		print "blinking"

	#end of while

#######END OF FUNCT DEFINITION##################

#######SCRIPT EXECUTION#########################

main()		













