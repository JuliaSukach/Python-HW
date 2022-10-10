# Ввести предложение, состоящее из двух слов. Поменять местами слова, добавить "!" в начало и конец, слова разделить
# 3 символами (" ", "!", " ")
#
# Пример
# "hello world" --> "world ! hello"
# Задание выполнить разными способами форматирования.


# first implementation
sentence = input('Enter sentence:').strip()

parts = sentence.split(' ')
parts.reverse()

new_sentence = ' ! '.join(parts)

assert new_sentence == "world ! hello"

# second
sentence = input('Enter sentence:').strip()

parts = sentence.split(' ')
parts.reverse()

assert "{} ! {}".format(parts[0], parts[1]) == "world ! hello"

# third
sentence = input('Enter sentence:').strip()
part_one, part_two = sentence.split(' ')

assert f'{part_two} ! {part_one}' == "world ! hello"

# fourth
sentence = input('Enter sentence:').strip()
parts = sentence.split(' ')
parts.reverse()

new_sentence = ' ! '.join(parts)
assert new_sentence == "world ! hello"

# fifth
sentence = input('Enter sentence:').strip()
sentence = sentence.replace(' ', '!')

a, b, c = sentence.partition('!')
a, c = c, a

assert a + ' ' + b + ' ' + c == "world ! hello"

# sixth
sentence = input('Enter sentence:').strip()
parts = sentence.split(' ')

assert "{first_arg} ! {second_arg}".format(first_arg=parts.pop(), second_arg=parts[0]) == "world ! hello"

