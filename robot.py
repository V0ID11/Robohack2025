import move as m
import time as zac
import turn as t
import position as p
import math 
# m.move(direction="f", time = 5, distance = 500)

#marker = p.find_marker_of_id(106)
#angle = p.direction_to_marker()
#print("ANGLE: " + str(angle))
n = 1
while True:
    markers = []
    loc = (0,0,0)
    while int(loc[0]) == 0:
        while len(markers) < 2:
            markers = p.get_markers_in_sight()[0]
            p.detect_and_save(n)
            n = n + 1
            t.turn("c",90)
            zac.sleep(1)
            print(markers)
        loc = p.getLocation(markers)
    dest = (100,100)
    deltax = dest[0]-loc[0]
    deltay = dest[1]-loc[1]
    dist = math.sqrt(deltax*deltax + deltay*deltay)
    angle = math.atan(deltay/deltax)
    if dest[1] > loc[1] and dest[0] > loc[0]:
        angle = math.pi*2 - angle
    elif dest[1] < loc[1] and dest[0] < loc[0]:
        angle = math.pi - angle
    elif dest[1] > loc[1] and dest[0] < loc[0]:
        angle = math.pi + angle
    print(angle)
    angleToMove = (angle - loc[2]) % (math.pi * 2)
    angleToMove = angleToMove *(180 /math.pi)
    t.turn("c",angle=angleToMove)
    print(loc)
    print(angleToMove)
    print(dist)  
    m.move("f",distance=dist)
    zac.sleep(1)


