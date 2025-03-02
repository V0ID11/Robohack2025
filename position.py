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
    counter = 0
    marker_found = False
    while counter < 6:
        markers_in_sight = get_markers_in_sight()
        for marker in markers_in_sight[1]:
            if marker.id == id:
                return marker
        counter += 1
        
        t.turn("c", 60)
    
def get_angle_to_enemy_wall(own_team: int):
    if own_team == 0:
        enemy_wall_markers = [i for i in range(7, 14)]
    else:
        enemy_wall_markers = [i for i in range(21, 28)]

    for i in range(4):
        markers: list[m.Marker] = get_markers_in_sight()[0]
        for marker in markers:
            if marker.id in enemy_wall_markers:
                return marker.position.horizontal_angle
        t.turn("c", 90)
    
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
        
def detect_and_save() -> None:
    vision.detect_markers(save="god.jpeg")
    print("God has been saved")