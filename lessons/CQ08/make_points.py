"""Making the points to test."""

from point import Point

p = Point(1.0, 2.0)

scaled_point = p.scale(3)
print("Scaled point:")
print("x coordinate:", scaled_point.x)
print("y coordinate:", scaled_point.y)

p.scale_by(2)
print("Scaled by point method:")
print("x coordinate:", p.x)
print("y coordinate:", p.y)

__author__ = "730396719"
