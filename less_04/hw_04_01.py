# Есть список, содержащий кортежи [(1, 2), (3, 4), (5, 6)]
# Используя list comprehension получить список, содержащий сумму элементов кортежа

data = [(1, 2), (3, 4), (5, 6)]
result = [3, 7, 11]

assert [v[0] + v[1] for v in data] == result
assert [sum(v) for v in data] == result
