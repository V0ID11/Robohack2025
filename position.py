from sbot import vision
from sbot import marker as m


def get_markers_in_sight() -> tuple(list[m.Marker]):
    WallMarkers, BoxMarkers = [],[]
    markers = vision.detect_markers()
    for marker in markers:
        if marker.id<=27:
            WallMarkers.append(marker)
        else:
            BoxMarkers.append(marker)
    return WallMarkers,BoxMarkers

def find_closest(markers: list[m.Marker]):
    closest_marker = markers[0]
    for i in range(1,len(markers)-1):
        if markers[i].position.distance < closest_marker.position.distance:
            closest_marker = markers[i]
    return closest_marker

def direction_to_marker(marker: m.Marker) -> int:
    angle = marker.position.horizontal_angle
    if angle > 0:
        return "r", angle
    elif angle < 0:
        return "l", abs(angle)
    else:
        return "s", 0

        
def detect_and_save():
    vision.detect_markers(save="god.jpeg")