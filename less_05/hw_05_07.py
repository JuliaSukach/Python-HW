# Написать декоратор, который кэширует результат выполнения ф-и и
# при повторном вызове с такими же аргументами выдает результат из кэша

from functools import lru_cache


def fib_decorator(func):
    cash = {}

    def inner(n):
        if n in cash:
            return cash[n]

        result = func(n)
        cash[n] = result

        return result

    return inner


@fib_decorator
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


fib(10)


@lru_cache(maxsize=32)
def fib_with_lru_cache(n):
    if n < 2:
        return n
    return fib_with_lru_cache(n - 1) + fib_with_lru_cache(n - 2)


fib_with_lru_cache(10)
