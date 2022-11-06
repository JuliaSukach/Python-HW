# Создать словать в качестве ключа которого будет 6-ти значное число (id),
# а в качетсве значений кортеж состоящий из 2-х элементов - имя(str), возраст(int).
# Сделать около 5-6 элементов словаря
# Записать данный словарь на диск в json-файл

import json
from random import randrange

info = [
    ('Yulia', 24),
    ('Alesia', 25),
    ('Dima', 27),
    ('Sonia', 24),
    ('Ilya', 26)
]


def generate_id():
    return randrange(100000, 1000000)


id_length = 6

data = {generate_id(): (v, i) for v, i in info}


with open('data.json', 'w') as write_file:
    json.dump(data, write_file)
