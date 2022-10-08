# Ввести целое число N. Получить сумму кубов всех целых чисел от 1 до N (включая).
# Реализовать через while и for.

num = input('Enter integer number:')


# while
def sum_with_while(n):
    if not n.isnumeric() or int(n) == 0:
        return "number must be integer and more than 0"

    n = int(n)
    idx = 1
    sum_value = 0

    while n >= idx:
        sum_value += idx ** 3
        idx += 1

    return sum_value


print(sum_with_while(num))


# for
def sum_with_for(n):
    if not n.isnumeric() or int(n) == 0:
        return "number must be integer and more than 0"

    n = int(n)
    sum_value = 0

    for i in range(n + 1):
        sum_value += i ** 3

    return sum_value


print(sum_with_for(num))
