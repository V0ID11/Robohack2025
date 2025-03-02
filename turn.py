from sbot import *
import time as t

def turn(direction: str,angle=-1):
    directionAsInt = 1
    if direction.lower() == "c":
    if direction.lower() == "c":
        directionAsInt = -1
    if angle > -1:
        totaltime = angle/360 * 3.41
        motors.set_power(0,0.25*directionAsInt)
        motors.set_power(1,-0.25*directionAsInt)
        t.sleep(totaltime)
        stop()
    else:
        motors.set_power(0,0.25*directionAsInt)
        motors.set_power(1,-0.25*directionAsInt)
    else:
        motors.set_power(0,0.25*directionAsInt)
        motors.set_power(1,-0.25*directionAsInt)

def stop() -> None:
    motors.set_power(0,BRAKE)
    motors.set_power(1,BRAKE)
    motors.set_power(0,BRAKE)
    motors.set_power(1,BRAKE)