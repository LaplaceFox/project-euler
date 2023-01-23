from math import *

widths = [25*(sqrt(2)-1), 10, 10, 10, 10, 10, 25*(sqrt(2)-1)]
speeds = [10, 9, 8, 7, 6, 5, 10]

def angles_from_start(ang):
    angles = [ang]
    for i in range(6):
        ang = asin(speeds[i+1] * sin(ang) / speeds[i])
        angles.append(ang)
    return angles

def height_from_angles(angles):
    return sum([widths[i] * tan(angles[i]) for i in range(7)])

def time_from_angles(angles):
    return sum([widths[i] / (cos(angles[i]) * speeds[i]) for i in range(7)])

def solution():
    goal_height = 50 * sqrt(2)

    lo = 0
    hi = pi/2 - 0.01 # not quite vertical!

    height = 0

    while abs(height - goal_height) >= 1/10**10:
        mid = (lo+hi)/2
        angles = angles_from_start(mid)
        height = height_from_angles(angles)

        if height < goal_height:
            lo = mid
        else:
            hi = mid

    return time_from_angles(angles)