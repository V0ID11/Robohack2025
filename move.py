from sbot import *
import time as t

def move(direction: str, speed=0.25,time=-1, distance=-1) -> None:
    directionAsInt = 1
    time = distance/36.6
    rightMotor = speed + 0.15
    leftMotor = speed
    if direction.lower() == "f":
        directionAsInt = -1

    motors.set_power(0,speed*directionAsInt)
    motors.set_power(1,speed*directionAsInt)
    if time > -1:
        t.sleep(time)
        stop()


def stop() -> None:
    motors.set_power(0,BRAKE)
    motors.set_power(1,BRAKE)

