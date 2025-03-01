from sbot import *
import time as zac
motors.set_power(0,-0.5)
motors.set_power(1,-0.5)
zac.sleep(1)
motors.set_power(0,0)
motors.set_power(1,0)
