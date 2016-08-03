import RPi.GPIO as GPIO
import time
import button_interface
import global_var
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.IN)		##  GPIO FOR UP BUTTON
#GPIO.setup(15,GPIO.OUT)


def button_up():
	cnt_u = 0
	var_u = GPIO.input(21)
	if var_u== 1:
		pass
	else:
		if(0 == cnt_u):
			print "Up Button is pressed"
			#GPIO.output(15,GPIO.HIGH)
			cnt_u = 1
			print "Switch on"
			button_interface.speed_up()
			
		else:
			#GPIO.output(15,GPIO.LOW)
			print "Switch off"
			cnt_u = 0	
			
		time.sleep(0.2) 
	
		
