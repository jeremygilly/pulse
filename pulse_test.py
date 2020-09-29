import RPi.GPIO as GPIO
import time

def pulse(duty = 0.01):
	# turn on
	GPIO.output(18, GPIO.HIGH)
	time.sleep(duty)
	# turn off 
	GPIO.output(18, GPIO.LOW)
	time.sleep(1-duty)
	return 0

def pwm_test(duty = 0.01):
	''' Creates a PWM to create a pulse.
	This does not appear to work. The oscilloscope shows that the 
	'''
	pwm = GPIO.PWM(18, 50)
	pwm.start(duty)
	return 0	

def main():
	# ~ GPIO.setmode(GPIO.BOARD)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT)
	# ~ pwm_test(50) 
	while True:
		pulse(0.001)
		pass
	return 0
	
if __name__ == '__main__':
	main()
