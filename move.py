from sbot import *


def move(direction: str, speed=0.25) -> None:
    directionAsInt = 1
    if direction.lower() == "f":
        directionAsInt = -1

    motors.set_power(0,speed*directionAsInt)
    motors.set_power(1,speed*directionAsInt)

def stop() -> None:
    motors.set_power(0,0)
    motors.set_power(1,0)