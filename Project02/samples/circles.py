

from math import pi

def get_circle_area( radius ):

    if type(radius) not in [int, float]:
        raise ValueError("The radius must be a non-negative real number.")

    if radius < 0:
        raise ValueError("The value can not be negative.")
    return pi * pow(radius, 2)

