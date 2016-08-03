import RPi.GPIO as GPIO
import time
import gsmbookcode
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(15,GPIO.IN)  	## GPIO FOR GSM
#GPIO.setup(15,GPIO.OUT)


def one():
	cnt = 0
	var = GPIO.input(15)
	if var== 1:
		pass
	else:
		if(0 == cnt):
			print "calling"
			#GPIO.output(15,GPIO.HIGH)
			cnt = 1
			print "Switch on"
			gsmbookcode.gsm_call()
			#switch_on()
			#exit()
		else:
			#GPIO.output(15,GPIO.LOW)
			print "Switch off"
			cnt = 0	
			gsmbookcode.gsm_hangup()
			#switch_off()
		time.sleep(0.2) 
	#gsmbookcode.gsm_call()
	
		