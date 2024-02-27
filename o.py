import math

class Shape:
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

class ShapeCreation:
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == 'circle':
            return Circle(*args)
        elif shape_type == 'square':
            return Square(*args)
        elif shape_type == 'rectangle':
            return Rectangle(*args)
        else:
            raise ValueError("Invalid shape type")

if __name__ == "__main__":
    shapes = [
        ShapeCreation.create_shape('circle', 5),
        ShapeCreation.create_shape('square', 4),
        ShapeCreation.create_shape('rectangle', 3, 6)
    ]

    for shape in shapes:
        print("Area of", type(shape).__name__, ":", shape.get_area())
