from sbot import vision
from sbot import marker as m
import turn as t
import move as mov
import time as zac
import math


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
    for i in range(8):
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

        t.turn(d,abs(direction_to_marker(closest_marker)))
        mov.move("f", time=1,distance=(closest_marker.position.distance/20))
    return closest_marker


    

def detect_and_save() -> None:
    vision.detect_markers(save="god.jpeg")
    print("God has been saved")