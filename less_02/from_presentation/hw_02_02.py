# Создать 2 переменные с одинаковыми данными и с разными идентификаторами

# first
list_one = [1, 2, 3]
list_two = list_one.copy()

assert id(list_one) != id(list_two)

# second
list_one = [1, 2, 3]
list_two = list_one[:]

assert id(list_one) != id(list_two)

# third
set_one = {1, 2, 3}
set_two = {i + 1 for i in range(3)}

assert id(set_one) != id(set_two)

# fourth

tuple_one = 1, 2, 3
tuple_two = tuple([1, 2, 3])

assert id(tuple_one) != id(tuple_two)


