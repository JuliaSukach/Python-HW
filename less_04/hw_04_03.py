# На вход функции подается натуральное число n.
# Напишите программу, использующую списочное выражение, которая создает список содержащий квадраты чисел от 1 до n,
# а затем выводит его элементы построчно, то есть каждый на отдельной строке.

n = int(input('Enter a number'))


# first
def foo_print_with_sep(num):
    list_of_square = [x ** 2 for x in range(num + 1)]

    print(*list_of_square, sep='\n')


foo_print_with_sep(n)

print('='*10)


# second
def foo_print_with_for(num):
    list_of_square = [x * x for x in range(num + 1)]

    for x in list_of_square:
        print(x)


foo_print_with_for(n)

print('='*10)
# third

def foo_print_in_list(num):
    [print(x * x) for x in range(num + 1)]


foo_print_in_list(n)
