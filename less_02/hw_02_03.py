# Есть список NUMBERS, содержащий повторяющиеся целые числа.
# С помощью множества (set) отфильтровать его и получить новый список с уникальными числами.

numbers = [1, 4, 6, 3, 4, 3, 5, 10, 200, 17, 6]

uniq = [1, 4, 6, 3, 5, 10, 200, 17]

uniq.sort()

# first way
new_list = list(set(numbers))
new_list.sort()
assert new_list == uniq

# second way
new_list = list({i for i in numbers})
new_list.sort()
assert new_list == uniq

