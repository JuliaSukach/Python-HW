# При помощи функции filter() из кортежа слов отфильтровать только те, которые
# являются полиндромами (которые читаются одинаково в обе стороны).

from data import str_tuple


# first

def filter_with_lambda(data):
    return list(filter(lambda s: s.lower() == s[::-1].lower(), data))


filter_with_lambda(str_tuple)


# second

def filter_with_func(data):
    def check_palindrome(word):
        if word.lower() == word[::-1].lower():
            return True

    return list(filter(check_palindrome, data))


filter_with_func(str_tuple)
