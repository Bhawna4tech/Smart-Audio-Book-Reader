import RPi.GPIO as GPIO
import time
import global_var
import button_interface
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.IN)		##  GPIO FOR LEFT BUTTON
#GPIO.setup(15,GPIO.OUT)


def button_left():
	cnt_l = 0
	var_l = GPIO.input(7)
	if var_l== 1:
		pass
	else:
		if(0 == cnt_l):
			print "Left Button is pressed"
			#GPIO.output(15,GPIO.HIGH)
			cnt_l = 1
			print "Switch on"
			button_interface.pitch_down()
			
		else:
			#GPIO.output(15,GPIO.LOW)
			print "Switch off"
			cnt_l = 0	
			
		time.sleep(0.2) 
	
		
