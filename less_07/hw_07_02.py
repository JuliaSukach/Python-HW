# Импортировать из base.py класс Shape и унаследовать класс Rectangle.
# Реализовать конструктор (__init__) (подумать, какие параметры нужны при создании объекта) и
# метод get_area.
# Реализовать методы сложения и вычитания объектов,
# результатом которых будет новое значение площади (объекты при этом не меняются).
# Написать проверки.

from base import Shape


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def __sub__(self, other):
        return self.get_area() - other.get_area()

    def __add__(self, other):
        return self.get_area() + other.get_area()


rect1 = Rectangle(10, 5)
rect2 = Rectangle(20, 10)
subtraction = rect2 - rect1
sum_of_areas = rect1 + rect2
assert rect1.get_area() == 50
assert subtraction == 150
assert sum_of_areas == 250