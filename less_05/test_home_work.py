from hw_05_02 import convert_num_to_str, convert_num_to_str_func
from hw_05_03 import filter_with_lambda, filter_with_func
from hw_05_04 import fibonacci_num, func_binet
from hw_05_05 import analyzer, check_num_type
from hw_05_06 import fibonacci
from hw_05_07 import fib
from hw_05_08 import sum_with_filter_and_lambda, sum_with_filter_and_func, sum_with_reduce, sum_with_reduce_and_filter


def test_convert_num_to_str():
    assert convert_num_to_str([1, 2, 3]) == ['1', '2', '3']


def test_convert_num_to_str_func():
    assert convert_num_to_str_func([1, 2, 3]) == ['1', '2', '3']


def test_filter_with_lambda():
    assert filter_with_lambda(['home', 'noon', 'pop', 'Anna']) == ['noon', 'pop', 'Anna']


def test_filter_with_func():
    assert filter_with_func(['home', 'noon', 'pop', 'Anna']) == ['noon', 'pop', 'Anna']


def test_fibonacci_num():
    assert fibonacci_num(4) == 3


def test_func_binet():
    assert func_binet(4) == 3


def test_check_num_type():
    assert check_num_type('-199.4') == 'You entered negative fractional number -199.4'


def test_analyzer():
    assert analyzer('w3985ksj') is None


def test_fibonacci():
    assert fibonacci(10, []) == 55


def test_fib():
    assert fib(10) == 55


def test_sum_with_filter_and_lambda():
    assert sum_with_filter_and_lambda([2, 4, 6, 1, 3, 5]) == 14


def test_sum_with_filter_and_func():
    assert sum_with_filter_and_func([2, 4, 6, 1, 3, 5]) == 14


def test_sum_with_reduce():
    assert sum_with_reduce([2, 4, 6, 1, 3, 5]) == 14


def test_sum_with_reduce_and_filter():
    assert sum_with_reduce_and_filter([2, 4, 6, 1, 3, 5]) == 14
