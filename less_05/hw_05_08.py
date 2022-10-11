# Дан список чисел. Найти сумму чисел, кратных 3 и 5.
# Реализовать через filter/reduce
# Написать тесты.
from functools import reduce
from data import num_list
import operator


# first

def sum_with_filter_and_lambda(nums):
    return sum(list(filter(lambda n: n % 3 == 0 or n % 5 == 0, nums)))


sum_with_filter_and_lambda(num_list)


# second

def sum_with_filter_and_func(nums):
    def filter_func(num):
        return num % 3 == 0 or num % 5 == 0

    return sum(tuple(filter(filter_func, nums)))


sum_with_filter_and_func(num_list)


# third
def sum_with_reduce(nums):
    return reduce(
        lambda acc, ch: acc + (ch if ch % 3 == 0 or ch % 5 == 0 else 0),
        nums,
        0
    )


sum_with_reduce(num_list)


# fourth

def sum_with_reduce_and_filter(nums):
    return reduce(
        operator.add,
        filter(lambda n: n % 3 == 0 or n % 5 == 0, nums),
        0
    )


sum_with_reduce_and_filter(num_list)
