def gsm_call():
	import serial 
	import time 
	#import RPi.GPIO as GPIO 

	print"Emergency Situation. Help Needed."
	port = serial.Serial("/dev/ttyAMA0", 9600, timeout=3.0) 
 



	try:
		print"Contacting Help " 
		print"Waiting for network.." 
		#print"Commands		functions" 
		#print"AT	to check operations" 
		port.write('AT\r\n')		
		rcv = port.read(20) 
		print"GSM" + rcv
		#while True: 
		rcv = port.read(20) 
		print rcv
		time.sleep(2) 
		#keyin = raw_input("Want to call ? press y else n") 
		#if keyin== "y": 
		keyin = "9794486418" 
		#print keyin
		keyin2 = 'ATD '+keyin+';\r\n' 
		print"Dialing : " + keyin2 
		port.write(keyin2)
		#execfile(button.py)
	
		x=1 
		for x in range(0,9): 
			rcv= port.read(50) 
			print rcv
			x+=1
		port.close()
		exit()
	

	except:
		port.close()
 
		#else : 
			#if keyin == "n": 
			#	rcv= port.read(50) 
			#	print rcv
			#	time.sleep(2)

def gsm_hangup(): 
	try:	
		if rcv=='RING':			
			print 'ring' 
			port.write('ATH \r\n') 
 
	except:
		port.close() 

