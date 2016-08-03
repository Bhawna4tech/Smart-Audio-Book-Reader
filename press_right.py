import RPi.GPIO as GPIO
import time
import global_var
import button_interface
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.IN)		##  GPIO FOR RIGHT BUTTON
#GPIO.setup(15,GPIO.OUT)


def button_right():
	cnt_r = 0
	var_r = GPIO.input(11)
	if var_r== 1:
		pass
	else:
		if(0 == cnt_r):
			print "RIGHT Button is pressed"
			#GPIO.output(15,GPIO.HIGH)
			cnt_r = 1
			print "Switch on"
			button_interface.pitch_up()
			
		else:
			#GPIO.output(15,GPIO.LOW)
			print "Switch off"
			cnt_rs = 0	
			
		time.sleep(0.2) 
	
		
