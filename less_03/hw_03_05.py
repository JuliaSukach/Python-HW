# Реализовать вычисление факториала с помощью цикла while и for.
# Продумать область допустимых значений.
# Добавить проверки, исключаютщие бесконечный цикл.
# Написать тесты на различные варианты.

import math


# while

def factorial_with_while(n):
    if type(n) != int:
        return "it's not an integer"

    if n < 0:
        return "value must be greater or equal to 0"

    result = 1
    while n > 0:
        result *= n
        n -= 1

    return result


assert factorial_with_while(4) == math.factorial(4)


# for

def factorial_with_for(n):
    result = 1

    if type(n) != int:
        return "it's not an integer"

    if n < 0:
        return "value must be greater or equal to 0"

    for i in range(1, n + 1):
        result *= i

    return result


assert factorial_with_for(4) == math.factorial(4)
