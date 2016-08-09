import RPi.GPIO as GPIO
import time
# blinking function


GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)


while True:
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(1)
        



GPIO.cleanup() 
