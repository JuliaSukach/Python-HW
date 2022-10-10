# Реализовать класс Box, который принимает в себя экземпляры класса Shape.
# Реализовать методы
# - add_shape - добавляет фигуру в текущую коллекцию
# - remove_shape - удаляет последн добавленную фигуру
# - get_common_area - возвращает общую площадь всех фигур

import math
from base import Shape
from hw_07_02 import Rectangle
from hw_07_03 import Circle


class Box:
    def __init__(self, shapes: list = None):
        self._shapes = shapes if shapes else []

    def add_shape(self, shape: Shape):
        self._shapes.append(shape)

    def remove_shape(self, shape: Shape):
        self._shapes.remove(shape)

    def get_common_area(self):
        return sum(list(map(lambda shape: shape.get_area(), self._shapes)))


box = Box()
my_shape = Circle(radius=5)
my_shape2 = Rectangle(width=5, height=10)
box.add_shape(my_shape)
box.add_shape(my_shape2)
assert box.get_common_area() == 5 * 10 + math.pi * 5 ** 2
