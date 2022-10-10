# Ф-я принимает список целых чисел и возвращает минимальное число, максимальное число, среднее-арифметическое.
import statistics


def math_func(nums):
    return min(nums), max(nums), sum(nums) / len(nums)


def math_func_with_stat(nums):
    return min(nums), max(nums), statistics.mean(nums)


math_func([1, 3, 6, -1, 5]) == -1, 6, 2.8
math_func_with_stat([1, 3, 6, -1, 5]) == -1, 6, 2.8
