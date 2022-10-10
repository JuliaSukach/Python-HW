# Для рассмотренного на уроке класса Circle реализовать метод производящий вычитание
# двух окружностей вычитание радиусов произвести по модулю. Если вычитаются две окружности с одинаковым значением
# радиуса то результатом вычитания будет точка класса Point

class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def __sub__(self, other):
        if self.radius == other.radius:
            return Point()

        return abs(self.radius - other.radius)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


circle1 = Circle(10)
circle2 = Circle(20)

subtraction = circle1 - circle2
assert subtraction == 10
