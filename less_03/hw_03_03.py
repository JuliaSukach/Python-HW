# Добавить в ex.2 бесконечный цикл.
# Выход из цикла сделать через ввод симолов "Q", "q"

def get_user():
    while True:
        name = input('Enter your name:')
        if name.lower() == 'q':
            break

        age = input('Enter your age:')

        if not age.isnumeric() or int(age) <= 0:
            print('Error, repeat the entry')
        elif 10 <= int(age) <= 18:
            print(f"What's up {name}")
        elif 18 < int(age) <= 120:
            print(f"What would you like {name}?")
        else:
            print(f"{name}, you're a liar")


get_user()

