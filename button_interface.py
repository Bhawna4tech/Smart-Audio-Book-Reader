#!/usr/bin/python

#import RPi.GPIO as GPIO
#import time
import global_var
#GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
#GPIO.setup(40,GPIO.IN)			#GPIO 40 for gsm , Change it
##GLOBAL VARIABLES (DEFAULT SPEED AND PITCH)


print "Speed b4 calling:"+ str(global_var.speed)
print "Pitch b4 calling:"+ str(global_var.pitch)



	
def speed_up():

	#global speed	
	if global_var.speed<200:
		global_var.speed=global_var.speed+30
		print "Spped UP Func"
		print "Speed after calling func:"+ str(global_var.speed)
		#return speed
	else:
		print "Speed after calling func:"+ str(global_var.speed)
		#return speed



def pitch_up():
	
	#global pitch
	if global_var.pitch<200:
		global_var.pitch=global_var.pitch+20
		print "Pitch UP Func"
		print "Pitch after calling func:"+ str(global_var.pitch)
		#return pitch
	else:
		print "Pitch after calling func:"+ str(global_var.pitch)
		#return pitch

def speed_down():

	#global speed	
	if global_var.speed>0 :
		global_var.speed=global_var.speed-30
		print "Speed down Func"
		print "Speed after calling func:"+ str(global_var.speed)
		#return speed
	else:
		print "Speed after calling func:"+ str(global_var.speed)
		#return speed



def pitch_down():
	
	#global pitch
	if global_var.pitch>0 :
		global_var.pitch=global_var.pitch-20
		print "Pitch down Func"
		print "Pitch after calling func:"+ str(global_var.pitch)
		#return pitch
	else:
		print "Pitch after calling func:"+ str(global_var.pitch)
		#return pitch



