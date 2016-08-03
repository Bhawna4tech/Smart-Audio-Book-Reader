import RPi.GPIO as GPIO
import time
import global_var
import button_interface
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.IN)		## GPIO FOR DOWN BUTTON
#GPIO.setup(15,GPIO.OUT)


def button_down():

	cnt_d = 0
	var_d = GPIO.input(23)
	if var_d== 1:
		pass
	else:
		if(0 == cnt_d):
			print "Down Button is pressed"
			#GPIO.output(15,GPIO.HIGH)
			cnt_d = 1
			print "Switch on"
			button_interface.speed_down()
			
		else:
			#GPIO.output(15,GPIO.LOW)
			print "Switch off"
			cnt_d = 0	
			
		time.sleep(0.2) 
	
		
