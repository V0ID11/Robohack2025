from sbot import *
import time as t

def turn(direction: str,angle=-1):
    directionAsInt = 1
    if direction.lower() == "r":
        directionAsInt = -1
    motors.set_power(0,0.5*directionAsInt)
    motors.set_power(1,-0.5*directionAsInt)
    if angle > -1:
        t.sleep(angle/360 * 1.5)
        stop()

def stop() -> None:
    motors.set_power(0,0)
    motors.set_power(1,0)