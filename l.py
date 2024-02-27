import math

class Shape:
    def get_area(self):
        raise NotImplementedError("Subclasses must implement get_area()")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def set_radius(self, radius):
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

def main():
    circle = Circle(5)
    print("Circle Area:", circle.get_area())

    rectangle = Rectangle(4, 6)
    print("Rectangle Area:", rectangle.get_area())

    triangle = Triangle(3, 7)
    print("Triangle Area:", triangle.get_area())

if __name__ == "__main__":
    main()
