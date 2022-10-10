# Создать список (list), содержащий числа, кратные 7 в диапазоне от 0 до 100.
# Выбрать первые 5 записей и записать в другой список с помощью среза.

numbers = [i for i in range(100) if i % 7 == 0]

sliced = numbers[:5]

print(numbers)
assert len(sliced) == 5