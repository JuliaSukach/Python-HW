# Импортировать из base.py класс Shape и унаследовать класс Circle.
# Реализовать конструктор (__init__) (подумать, какие параметры нужны при создании объекта) и
# метод get_area.
# Реализовать методы сложения и вычитания объектов,
# результатом которых будет новое значение площади (объекты при этом не меняются).
# Написать проверки.

import math
from base import Shape


class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def __sub__(self, other):
        return self.get_area() - other.get_area()

    def __add__(self, other):
        return self.get_area() + other.get_area()


circle1 = Circle(5)
circle2 = Circle(10)
subtraction = circle2 - circle1
sum_of_areas = circle1 + circle2
assert circle1.get_area() == math.pi * 5 ** 2
assert subtraction == math.pi * 10 ** 2 - math.pi * 5 ** 2
assert sum_of_areas == math.pi * 10 ** 2 + math.pi * 5 ** 2