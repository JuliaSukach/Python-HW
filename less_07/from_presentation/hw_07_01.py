# Создать родительский класс auto, у которого есть атрибуты: brand, age, color, mark и weight.
# А так же методы: move, birthday и stop. Методы move и stop выводят сообщение на экран "move" и "stop",
# а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при обьявлении обьекта.

class Auto:
    def __init__(self, brand: str, age: int, mark: str):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = None
        self.weight = None

    def move(self):
        print('Move')

    def birthday(self):
        self.age += 1

    def stop(self):
        print('Stop')


my_car = Auto(brand='audi', age=2000, mark='A6')

assert my_car.age == 2000
my_car.birthday()

assert my_car.age == 2001
