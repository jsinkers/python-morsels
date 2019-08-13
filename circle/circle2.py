import math


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

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
        return self.radius * 2

    @diameter.setter
    def diameter(self, diam):
        self.radius = diam/2

    @property
    def area(self):
        return math.pi*self.radius**2
