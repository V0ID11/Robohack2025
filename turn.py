from sbot import *
import time as t

def turn(direction: str,angle=-1):
    directionAsInt = 1
    if direction.lower() == "c":
        directionAsInt = -1
    if angle > -1:
        totaltime = angle/360 * 1.5
        i = 5
        if totaltime/0.2 < 5:
            i = (totaltime/0.2) % 1
        totaltime = totaltime - 0.2*i
        for x in range(1,i+1):
            motors.set_power(0,0.1*x*directionAsInt)
            motors.set_power(1,0.1*x*directionAsInt)
            t.sleep(0.1)
        t.sleep(totaltime)
        for x in range(i,0,-1):
            motors.set_power(0,0.1*x*directionAsInt)
            motors.set_power(1,0.1*x*directionAsInt)
            t.sleep(0.1)
        stop()
    else:
        motors.set_power(0,0.5*directionAsInt)
        motors.set_power(1,-0.5*directionAsInt)

def stop() -> None:
    motors.set_power(0,0)
    motors.set_power(1,0)