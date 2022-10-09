# Написать декоратор к 2-м любым функция, который бы считал и выводил время
# их выполнения. Подсказка:
# from datetime import datetime
# time = datetime.now()

from datetime import datetime


def calc_time(func):
    def inner():
        start_time = datetime.now()
        result = func
        print((datetime.now() - start_time) * 1000000.0)
        return result

    return inner


def fibonacci_num(n):
    if n in (1, 2):
        return 1
    return fibonacci_num(n - 1) + fibonacci_num(n - 2)


def func_binet(n):
    const = (1 + 5 ** 0.5) / 2
    return int((const ** n - (-const) ** (-n)) / (2 * const - 1))


func_binet_time = calc_time(func_binet(40))
func_binet_time()

fibonacci_time = calc_time(fibonacci_num(40))
fibonacci_time()
