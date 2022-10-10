# Есть список NUMBERS, содержащий повторяющиеся целые числа.
# С помощью словаря (dict) отфильтровать его и получить новый список с уникальными числами.

numbers = [1, 4, 6, 3, 4, 3, 5, 10, 200, 17, 6]

uniq = [1, 4, 6, 3, 5, 10, 200, 17]

# the first way
d = dict.fromkeys(numbers)

assert list(d.keys()) == uniq

# the second way
d = {a: '' for a in numbers}

assert list(d.keys()) == uniq

# the third way
d = dict(zip(numbers, [i for i in numbers]))

assert list(d.keys()) == uniq

