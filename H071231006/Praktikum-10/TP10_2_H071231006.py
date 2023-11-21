from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def calculate_area(self):
        pass

    def get_color(self):
        return self._color


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.__radius = radius

    def calculate_area(self):
        return 3.14 * self.__radius * self.__radius

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.__length = length 
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

def print_area(shape):
    if isinstance(shape, Shape):
        print(f"The area of the {shape.get_color()} shape is: {shape.calculate_area()}")

circle = Circle("Pink", 5)
rectangle = Rectangle("Blue", 4, 6)

print_area(circle)
print_area(rectangle)