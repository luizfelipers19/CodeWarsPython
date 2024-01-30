# This series of katas will introduce you to basics of doing geometry with computers.

# Point objects have x, y attributes. Circle objects have center which is a Point, and radius, which is a number.

# Write a function calculating circumference of a Circle.

# Tests round answers to 6 decimal places.


from math import pi

def circle_circumference(circle):
    # your solution here
    radius = circle.radius
    return  2 * pi * radius