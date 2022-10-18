# Сделать свое исключение и подключить к try/except

class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg


input_value = input("Input positive integer: ")


def some_foo(value):
    try:
        value = int(value)
        if value < 0:
            raise MyException("You gave negative!")
        return value
    except ValueError:
        print('Error type of value!')
    except MyException as exc:
        print(exc)


some_foo(input_value)
#assert some_foo(input_value) == int(input_value)
