import math

from .geom_shape import GeomShape
from .shape_color import ShapeColor


class Circle(GeomShape):
    NAME = 'Круг'

    def __init__(self, radius: float, color: str):
        self._radius = radius
        self._color = ShapeColor(color)

    def square(self) -> float:
        return math.pi * self._radius * self._radius

    @classmethod
    def name(cls) -> str:
        return cls.NAME

    def __repr__(self):
        return f"<Shape: {self.NAME}, radius: {self._radius}, color: {self._color.color_ppt}, square: {self.square()}>"
