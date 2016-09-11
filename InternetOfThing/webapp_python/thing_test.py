import time

import thing

piThing=thing.RPiThing()

switch=piThing.read_switch()

print ('Switch:{0}'.format(switch))

print ('Blinking.. press Ctrl-C to quit')

while True:

    piThing.set_led(True)
    time.sleep(1)
    piThing.set_led(False)
    time.sleep(1)


GPIO.cleanup()
