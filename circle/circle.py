# python morsels https://www.pythonmorsels.com/exercises/ac9f7d60d95d493f9e354f18a3ea9d82/
from math import pi


class Circle:
    def __init__(self, rad=1):
        self.radius = rad

    def __repr__(self):
        return "Circle(%.0f)" % self.radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, rad):
        if rad < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self._radius = rad

    @property
    def diameter(self):
        return 2*self.radius

    @property
    def area(self):
        return pi*self.radius**2

    @diameter.setter
    def diameter(self, diam):
        self.radius = diam/2

    @area.setter
    def area(self, a):
        raise AttributeError



