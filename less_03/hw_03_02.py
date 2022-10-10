# Написать программу, которая получает имя и возраст пользователя, проверяет возраст и выдает приветственное сообщение
# в зависимости от возраста:
# - меньше нуля или ноль или не число: "Ошибка, повторите ввод"
# - больше 0 до 10 не включая: "Привет, малыш {имя}!"
# - от 10 до 18 включая: "Как дела {имя}?"
# - больше 18 и включая 120: "Что желаете {имя}?"
# - в противном случае: "{имя} вы лжете - столько не живут"


def get_user():
    name = input('Enter your name:')
    age = input('Enter your age:')

    if not age.isnumeric() or int(age) <= 0:
        return 'Error, repeat the entry'
    elif 10 <= int(age) <= 18:
        return f"What's up {name}"
    elif 18 < int(age) <= 120:
        return f"What would you like {name}?"
    else:
        return f"{name}, you're a liar"


print(get_user())
