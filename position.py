from sbot import vision
from sbot import marker as m
import turn as t
import move as mov
import time as zac
import math
import numpy as np
from scipy.optimize import least_squares

def get_markers_in_sight() -> tuple(list[m.Marker]):
    mov.stop()
    WallMarkers, BoxMarkers = [],[]
    zac.sleep(1)
    markers = vision.detect_markers()
    zac.sleep(1)
    for marker in markers:
        if marker.id<=27:
            WallMarkers.append(marker)
        else:
            BoxMarkers.append(marker)
    return WallMarkers,BoxMarkers

def find_marker_of_id(id: int) -> m.Marker:
    mov.stop()
    marker_found = False
    while True:
        markers_in_sight = get_markers_in_sight()
        for marker in markers_in_sight[1]:
            if marker.id == id:
                return marker
        
        t.turn("c", 45)
    
def get_angle_to_enemy_wall(own_team: int):
    if own_team == 0:
        enemy_wall_markers = [i for i in range(7, 14)]
    else:
        enemy_wall_markers = [i for i in range(21, 28)]

    for i in range(6):
        markers: list[m.Marker] = get_markers_in_sight()[0]
        for marker in markers:
            if marker.id in enemy_wall_markers:
                return marker.position.horizontal_angle
        t.turn("c", 60)
    
    return 0

def find_closest(markers: list[m.Marker]) -> m.Marker:
    closest_marker = markers[0]
    for i in range(1,len(markers)-1):
        if markers[i].position.distance < closest_marker.position.distance:
            closest_marker = markers[i]
    return closest_marker

def direction_to_marker(marker: m.Marker) -> float:
    rad_angle = marker.position.horizontal_angle
    deg_angle = rad_angle * (180/math.pi)
    return deg_angle
        
    
def go_to_cube():
    box_markers = get_markers_in_sight()[1]
    #Find closest cube 
    closest_marker = find_closest(box_markers)
    if direction_to_marker(closest_marker)>0:
        d = "c"
    else:
        d = "ac"
    id = closest_marker.id
    #Distance here is done in cm
    while closest_marker.position.distance/10 > 1:
        detect_and_save()
        try:
            box_markers = get_markers_in_sight()[1]
            closest_marker = find_closest(box_markers)
        except: 
            find_marker_of_id(id)
            box_markers = get_markers_in_sight()[1]
            closest_marker = find_closest(box_markers)
        #Find closest cube 
       
        print(closest_marker.position.distance)
        if direction_to_marker(closest_marker)>0:
            d = "c"
        else:
            d = "ac"

        if closest_marker.position.distance < 700:
            t.turn(d,abs(direction_to_marker(closest_marker)))
            mov.move("f", speed = 0.5, time=1,distance=(closest_marker.position.distance/20))
        else:
            t.turn(d,abs(direction_to_marker(closest_marker)))
            mov.move("f", time=1,distance=(closest_marker.position.distance/20))
    return closest_marker


    

def detect_and_save(n) -> None:
    vision.detect_markers(save="god"+ str(n) + ".jpeg")
    print("God has been saved")

def getWallMarkerLocation(id):
    spacing = 675
    wall = id//7
    y = 0
    x = 0
    if wall == 0:
        y = 0
        x = (id+1)*spacing 
    elif wall == 1:
        y = ((id % 7)+1) *spacing
        x = spacing *8
    elif wall == 2:
        y = spacing*8
        x = ((7-(id%7)))*spacing 
    else:
        y = ((7-(id%7)))*spacing 
        x = 0
    return (x,y)




def getLocation(wallMarkers):
    marker1 = wallMarkers[0]
    marker2 = wallMarkers[len(wallMarkers) -1]
    loc1 = getWallMarkerLocation(marker1.id)
    loc2 = getWallMarkerLocation(marker2.id)
    roboloc = calculate_robot_position((loc1[0],loc1[1],marker1.position.horizontal_angle,marker1.position.distance),(loc2[0],loc2[1],marker2.position.horizontal_angle,marker2.position.distance))
    return roboloc

def calculate_robot_position(marker1, marker2):
    # Unpack marker data: (x, y, angle, distance)
    (x1, y1, theta1, d1) = marker1
    (x2, y2, theta2, d2) = marker2

    # Function to compute the error based on robot's estimated position and orientation
    def error(params):
        x0, y0, theta0 = params

        # Predicted positions of markers based on the robot's position and orientation
        pred_x1 = x0 + d1 * np.cos(theta0 + theta1)
        pred_y1 = y0 + d1 * np.sin(theta0 + theta1)

        pred_x2 = x0 + d2 * np.cos(theta0 + theta2)
        pred_y2 = y0 + d2 * np.sin(theta0 + theta2)

        # Calculate errors between predicted and actual marker positions
        error1 = pred_x1 - x1
        error2 = pred_y1 - y1
        error3 = pred_x2 - x2
        error4 = pred_y2 - y2

        # Return combined errors (for least-squares optimization)
        return [error1, error2, error3, error4]

    # Initial guess for (x0, y0, theta0)
    initial_guess = [2500, 2500, 0]  # assuming robot starts at origin and facing upwards (angle 0)

    # Solve the system of equations to minimize error
    result = least_squares(error, initial_guess)

    # Return the robot's estimated position (x0, y0) and orientation (theta0)
    x0, y0, theta0 = result.x
    return (x0, y0, theta0)