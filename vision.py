from sbot import vision

def get_markers():
    WallMarkers, BoxMarkers = [],[]
    markers = vision.detect_markers()
    for marker in markers:
        if marker.id<=27:
            WallMarkers.append(marker)
        else:
            BoxMarkers.append(marker)
    return WallMarkers,BoxMarkers
        
     
