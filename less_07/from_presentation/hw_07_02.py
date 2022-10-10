# Создать 2 класса truck и car, которые являются наследниками класса auto.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределенный метод move, перед появлением надписи 'move' выводит надпись 'attention',
# его реализацию сделать при помощи оператора super. А так же дополнительный метод load.
# При его вызове происходит пауза 1 сек., затем выдается сообщение 'load' и снова пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут 'max_speed is <max_speed>'.
# Создать по 2 обьекта для каждого из классов truck и car, проверить все их методы и атрибуты.
import time
from hw_07_01 import Auto


class Truck(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_load=0):
        Auto.__init__(self, brand, age, mark)
        self.max_load = max_load

    def move(self):
        print('Attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('Load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_speed=0):
        Auto.__init__(self, brand, age, mark)
        self.max_speed = max_speed


my_truck1 = Truck(brand='Toyota', age=2022, mark='Tacoma', max_load=1)
my_truck2 = Truck(brand='Nissan', age=2022, mark='Frontier', max_load=1)

my_truck1.move()
my_truck1.load()

my_car1 = Car(brand='BMW', age=2022, mark='X5', max_speed=1)
my_car2 = Car(brand='lamborghini', age=2022, mark='Urus', max_speed=1)
