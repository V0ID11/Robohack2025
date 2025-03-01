from sbot import *
import time as t

def turn(direction: str,time = -1):
    directionAsInt = 1
    if direction.lower() == "r":
        directionAsInt = -1
    motors.set_power(0,0.25*directionAsInt)
    motors.set_power(1,-0.25*directionAsInt)
    if time > -1:
        t.sleep(time)
        stop()   

def stop() -> None:
    motors.set_power(0,0)
    motors.set_power(1,0)