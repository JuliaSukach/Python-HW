# Написать реккурсивную ф-ю, вычисляющую N-е число ряда Фибоначчи.
# Продумать проверки + написать тесты.
# пример вызова
# assert fibonacci(10) == 55


def fibonacci(num, row=[]):
    if num < 0:
        return row[-1] if len(row) > 0 else 'Must be positive integer'
    elif len(row) <= 1:
        row.append(len(row))
    else:
        row.append(row[-1] + row[-2])

    num -= 1
    return fibonacci(num, row)


print(fibonacci(10))
