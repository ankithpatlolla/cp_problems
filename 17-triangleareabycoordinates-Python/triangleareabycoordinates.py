# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

import math


def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt((s) * (s - a) * (s - b) * (s - c))


def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + ((y2 - y1) ** 2))


def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
    a, b, c = dist(x1, y1, x2, y2), dist(x2, y2, x3, y3), dist(x3, y3, x1, y1)
    return (triangle_area(a, b, c))
