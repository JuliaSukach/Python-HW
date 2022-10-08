# Дан словарь. Создать новый словарь, поменяв местами ключ и значение
data = {
    'Yulia': 24,
    'Alesia': 25,
    'Pinsk': 'Brest',
    'Warsaw': 'Poland'
}

result = {
    24: 'Yulia',
    25: 'Alesia',
    'Brest': 'Pinsk',
    'Poland': 'Warsaw'
}

keys = list(data.keys())
values = list(data.values())
assert dict(zip(values, keys)) == result
assert {k: keys[values.index(k)] for k in values} == result
assert {val: item for (item, val) in data.items()} == result


