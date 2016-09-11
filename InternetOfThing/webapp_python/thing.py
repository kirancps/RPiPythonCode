import RPi.GPIO as GPIO





class RPiThing(object):

    def __init__(self):
        """Initialization of Board"""
        GPIO.setwarnings(False)
        GPIO.setmode (GPIO.BOARD)
        GPIO.setup (11,GPIO.OUT)
        GPIO.setup(12,GPIO.IN)


    def read_switch(self):
        """reads switch state"""

        return GPIO.input(12)


    def set_led(self,value):
        """sets led"""

        GPIO.output(11,value)
