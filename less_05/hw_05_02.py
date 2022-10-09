# Дан список чисел. Вернуть список, где при помощи функции map() каждое число
# переведено строку. В качестве функции в map использовать lambda.

from data import num_list


# first
def convert_num_to_str(nums):
    return list(map(lambda n: str(n), nums))


# second
def convert_num_to_str_func(nums):
    return list(map(str, nums))


convert_num_to_str(num_list)
convert_num_to_str_func(num_list)
