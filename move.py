from sbot import *
import time as t

def move(direction: str, speed=0.25,time=-1) -> None:
    directionAsInt = 1
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

