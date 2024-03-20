from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        return (self.a * self.b) / 2


class AreaCalculator:

    def __init__(self, shapes: list):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter`
    def shapes(self, value):
        if not isinstance(self.shapes, list):
            raise AssertionError("`shapes` should be of type")

        self.__shapes = value

    @property
    def total_area(self):
        total = 0

        for shape in self.shapes:
            total += shape.calculate_area()

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6), Triangle(2, 3), Triangle(5, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
