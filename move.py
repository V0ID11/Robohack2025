from sbot import *
def move(direction,speed=0.25):
    directionAsInt = 1
    if direction == "f":
        directionAsInt = -1
    motors.set_power(0,speed*directionAsInt)
    motors.set_power(1,speed*directionAsInt)

def stop():
    motors.set_power(0,0)
    motors.set_power(1,0)