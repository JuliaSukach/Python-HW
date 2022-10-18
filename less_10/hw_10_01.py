# Сделать калькулято
# обернуть его в try/except

import pytest

operation_list = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}


def type_error_handler(a, b):
    return f'first value = {a}, second value = {b}'


def get_calculation(a: int, b: int, op: str):
    foo = operation_list[op]
    return foo(a, b)


first_value = input('Enter first value: ')
second_value = input('Enter second value: ')
operation = input('Enter operation value: ')


def calculator(a, b, op):
    try:
        return get_calculation(a=int(a), b=int(b), op=op)
    except ZeroDivisionError:
        print(f'Second argument must be positive. {type_error_handler(a, b)}')
    except ValueError:
        print(f'Values should have integer type. {type_error_handler(a, b)}')
    except KeyError:
        print(f'There is no such operator as {op}')
    except Exception:
        print(f"Opps.. Something doesn't work")


assert calculator(first_value, second_value, operation) == 3


# @pytest.mark.parametrize(
#     "a, b, op, exp",
#     [
#         ('1', '2', '+', 3)
#     ]
# )
# def test_calculator(a, b, op, exp):
#     assert calculator(a, b, op) == exp
