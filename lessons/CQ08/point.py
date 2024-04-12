"""CQ08."""

from __future__ import annotations


class Point:
    """Creating point."""

    def __init__(self, x_cord: float, y_cord: float) -> None:
        """Point creator with x and y floats."""
        self.x = x_cord
        self.y = y_cord

    def scale_by(self, factor: int) -> None:
        """Scale factor by point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point: 
        """Scale a point by a factor."""
        return Point(self.x * factor, self.y * factor)


__author__ = "730396719"