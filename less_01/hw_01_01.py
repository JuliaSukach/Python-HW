# Даны 2 действительных числа.
# Получить их
# - сумму
# - разность
# - произведение
# - возвести в степень
# - поделить по модулю A на B
# - выполнить целочисленное деление A на B

x = 8
y = 3


def sum_of_two(a, b):
    return a + b


print(sum_of_two(x, y))


def diff_of_two(a, b):
    return a - b


print(diff_of_two(x, y))


def exp_of_two(a, b):
    return a ** b


print(exp_of_two(x, y))


def div_mod(a, b):
    return a % b


print(div_mod(x, y))


def div_of_two(a, b):
    return a // b


print(div_of_two(x, y))