# Написать декоратор к 2-м любым функция, который бы считал и выводил время
# их выполнения. Подсказка:
# from datetime import datetime
# time = datetime.now()

from datetime import datetime

factorial_num = 20


def calc_fibonacci_num(func):
    start_time = datetime.now()

    def inner(n):
        result = func(n)
        if factorial_num == n:
            print((datetime.now() - start_time) * 1000000.0)
        return result

    return inner


@calc_fibonacci_num
def fibonacci_num(n):
    if n in (1, 2):
        return 1
    return fibonacci_num(n - 1) + fibonacci_num(n - 2)


def calc_func_binet(func):
    def inner(num):
        start_time = datetime.now()
        result = func(num)
        print((datetime.now() - start_time) * 1000000.0)
        return result

    return inner


@calc_func_binet
def func_binet(n):
    const = (1 + 5 ** 0.5) / 2
    return round((const ** n - (-const) ** (-n)) / (2 * const - 1))


fibonacci_num(factorial_num)
func_binet(factorial_num)
