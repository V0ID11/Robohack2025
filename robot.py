from sbot import *
import time
motors.set_power(0,-0.5)
motors.set_power(1,-0.5)
time.sleep(1)
motors.set_power(0,0)
motors.set_power(1,0)
