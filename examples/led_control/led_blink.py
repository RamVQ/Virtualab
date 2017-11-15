#!/usr/bin/python

#######1.IMPORTS###################################

import RPi.GPIO as GPIO
import time

#######END OF IMPORTS############################


######2.SCRIPT CONST###############################

LED = 7 #GPIO  assigned to led

#######END OF SCRIPT CONST######################

#######3.FUNCT DEFINITON##########################

###main
def main():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED,GPIO.OUT)#LED pin setup

	while True:
		
		#testing

		time.sleep(3) #delay in seconds	
		GPIO.output(LED,GPIO.HIGH)

	#end of while

#######END OF FUNCT DEFINITION##################

#######SCRIPT EXECUTION#########################

if __name__=='__main__':

	try:main()
	except KeyboardInterrupt:pass
	finally:
		GPIO.cleanup()			













