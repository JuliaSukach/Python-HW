# Есть кортеж элементов CITIES = ('Minsk', 'Gomel', 'Mogivel', 'Orsha', 'Vitebsk', 'Grodno')
# На базе него создать список и добавить новый город.

cities = ('Minsk', 'Gomel', 'Mogivel', 'Orsha', 'Vitebsk', 'Grodno')

result = ['Minsk', 'Gomel', 'Mogivel', 'Orsha', 'Vitebsk', 'Grodno', 'Pinsk']

# first
new_list = list(cities)
new_list.append('Pinsk')
assert new_list == result

# second
new_list = list(cities)
new_list.extend(['Pinsk'])
assert new_list == result

# third
new_list = list(cities)
new_list.insert(1, 'Pinsk')
new_list.sort()
result.sort()
assert new_list == result

# fourth
new_tuple = cities + ('Pinsk',)
new_list = list(new_tuple)
new_list.sort()
result.sort()
assert new_list == result
