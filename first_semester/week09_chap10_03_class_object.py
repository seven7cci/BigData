import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * self.radius * self.radius


class Cylinder(Circle):
    def __init__(self, radius, height):
        #self.radius = radius
        super().__init__(radius)
        self.height = height

    def get_volume(self) -> float:
        # return math.pi * self.radius * self.radius * self.height
        return super().get_area() * self.height


cy1 = Cylinder(10.0, 5)
print(cy1.get_volume())

c1 = Circle(10.0)
print(c1.get_area())