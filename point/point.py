class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x, y, z)

    def __sub__(self, other):
        return self.__add__(Point(-other.x, -other.y, -other.z))

    def __mul__(self, other):
        return Point(other*self.x, other*self.y, other*self.z)

    def __rmul__(self, other):
        return self*other

    def __iter__(self):
        return iter([self.x, self.y, self.z])
