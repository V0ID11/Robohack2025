from sbot import arduino

def get_top_distance():
    return arduino.measure_ultrasound_distance(2,3)

def get_bottom_distance():
    return arduino.measure_ultrasound_distance(8,9)

def isBox():
    """Returns True if Box is detected otherwise False"""
    if get_bottom_distance() < 50:
        return True
    else:
        return False