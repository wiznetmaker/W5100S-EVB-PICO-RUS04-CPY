import time
import board

import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP0)

while True:
    try:
        result = sonar.distance
        print(("{} cm").format(result))
    except RuntimeError:
        print("Retrying!")
        pass
    time.sleep(0.1)