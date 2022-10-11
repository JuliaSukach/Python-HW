# Сделать функцию которая на вход принимает строку. Анализирует ее
# исключительно методом .isdigit() без доп. библиотек и переводит строку в число.
# Функция умеет распознавать отрицательные числа и десятичные дроби. Примеры
# -6.7 → Вы ввели отрицательное дробное число: -6.7
# 5 → Вы ввели положительное целое число: 5
# 5.4r → Вы ввели не корректное число: 5.4r
# -0.777 → Вы ввели отрицательное дробное число: -0.777

def analyzer(string):
    stack = []

    for i, value in enumerate(string):
        if value == '-' and i == 0:
            stack.append(value)
        elif value == '.':
            stack.append(value)
        elif value.isdigit():
            stack.append(value)
        else:
            return

    return "".join(stack)


def check_num_type(data):
    if not data:
        return f'You have entered wrong number'

    positive = True
    integer = True
    if data[0] == '-':
        positive = False
    if '.' in data:
        integer = False

    return (f'You entered '
            f'{"positive" if positive else "negative"} '
            f'{"integer" if integer else "fractional"} number '
            f'{data}')


check_num_type(analyzer('-14.7'))
