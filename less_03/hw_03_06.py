# Написать программу в которой нужно будет угадывать число.
# Продумать диапазон чисел (будут жестко заданы или задаваться самим пользователем)
from random import randint


def guess_number():
    is_range = input('Do you want to set a range (yes or no)?').strip().lower()
    generated_num = randint(1, 2)
    if is_range == 'yes':
        def get_num():
            user_range = input('Enter the range (start, end):').replace(" ", "").split(',')

            def is_error(inp):
                if len(inp) != 2:
                    return True
                elif not inp[0].isnumeric() and not int(inp[0]):
                    return True
                elif not inp[1].isnumeric() and not int(inp[1]):
                    return True

                return False

            while is_error(user_range):
                get_num()
            else:
                return randint(int(user_range[0]), int(user_range[1]))

        generated_num = get_num()

    user_num = input('Guess number:')
    while user_num.isnumeric() or int(user_num):
        if int(user_num) == generated_num:
            return 'You are correct!'
        elif int(user_num) > generated_num:
            return "Generated number is less than you entered"
        else:
            return "Generated number is more than you entered"

    return "Please, enter the number"


print(guess_number())
