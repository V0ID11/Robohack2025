import move as m
import time as zac
import turn as t
import position as p
import math 
import ultrasonic as u
# m.move(direction="f", time = 5, distance = 500)

#marker = p.find_marker_of_id(106)
#angle = p.direction_to_marker()
#print("ANGLE: " + str(angle))




def goToPoint(dest,hasCube):
    n = 1
    markers = []
    loc = (0,0,0)
    while int(loc[0]) == 0:
        markers = []
        while len(markers) < 2:   
            markers = []
            t.turn("ac",30)
            markers = p.get_markers_in_sight()[0]
            n = n + 1
            zac.sleep(0.3)
            if hasCube == True and u.isBox() == False:
                return "fail"
        loc = p.getLocation(markers)
    deltax = abs(dest[0]-loc[0])
    deltay = abs(dest[1]-loc[1])
    dist = math.sqrt(deltax*deltax + deltay*deltay) /10
    angle = math.atan(deltay/deltax)
    if dest[1] < loc[1] and dest[0] > loc[0]:
        angle = math.pi*2 - angle
    elif dest[1] > loc[1] and dest[0] < loc[0]:
        angle = math.pi - angle
    elif dest[1] < loc[1] and dest[0] < loc[0]:
        angle = math.pi + angle
    print(angle)
    angleToMove = (angle - loc[2]) % (math.pi * 2)
    angleToMove = angleToMove *(180 /math.pi)
    if angleToMove / 180 > 1:
        t.turn("a",360 - angleToMove)
    else:
        t.turn("c",angle=angleToMove)
    if hasCube == True and u.isBox() == False:
                return "fail"
    print(loc)
    print(angleToMove)
    print(dist)  
    m.move("f",distance=dist)
    zac.sleep(1)
    return "helloooo"

def goToCube():
    cube = findClosestCube()
    while u.isBox() ==  False:
        if cube.position.horizontal_angle < 0:
            t.turn("ac",abs(cube.position.horizontal_angle * (180/math.pi)))
        else:
            t.turn("c",cube.position.horizontal_angle* (180/math.pi))
        if cube.position.distance >600:
            m.move("f",distance=60)
        else:
            m.move("f",distance=20)
        cube = findClosestCube(cube)
        
def findClosestCube(previous = 0):
    currentCubes = p.get_markers_in_sight()[1]
    counter = 1
    while len(currentCubes) < 1:
        if u.isBox() == True:
            return previous
        if counter % 2 == 0:
            t.turn("a",10*counter)
        else:
            t.turn("c",10*counter)
        counter = counter +1
        currentCubes = p.get_markers_in_sight()[1]
    return p.find_closest(currentCubes)
        




while True:
    goToCube()
    if goToPoint((3000,1300),True) == "fail":
        continue
    if goToPoint((20,1300),True) == "fail":
        continue
    m.move("r",distance=100)
    if goToPoint((3000,1300),False) == "fail":
        continue
    