import move as m
import time as zac
import turn as t
import position as p

# m.move(direction="f", time = 5, distance = 500)

marker = p.find_marker_of_id(106)
angle = p.direction_to_marker()
print("ANGLE: " + str(angle))