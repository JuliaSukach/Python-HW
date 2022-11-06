# Сделать функцию которая на вход принимает строку. Анализирует ее
# исключительно методом .isdigit() без доп. библиотек и переводит строку в число.
# Функция умеет распознавать отрицательные числа и десятичные дроби. Примеры
# -6.7 → Вы ввели отрицательное дробное число: -6.7
# 5 → Вы ввели положительное целое число: 5
# 5.4r → Вы ввели не корректное число: 5.4r
# -0.777 → Вы ввели отрицательное дробное число: -0.777

def analyzer(string):
    stack = []

    positive = True
    integer = True
    for i, value in enumerate(string):
        if value == '-' and i == 0:
            positive = False
            stack.append(value)
        elif value == '.':
            integer = False
            stack.append(value)
        elif value.isdigit():
            stack.append(value)
        else:
            return print(f'You entered wrong number {string}')

    return print(f'You entered ' 
                 f'{"positive" if positive else "negative"} '
                 f'{"integer" if integer else "fractional"} number '
                 f'{"".join(stack)}')


analyzer('1997')

