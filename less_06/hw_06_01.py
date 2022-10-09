# Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'. Затем результат
# преобразовать в байтовый вид в кодировке `Latin1` и затем результат снова декодировать в строку
# результаты всех преобразований выводить на экран).

value = b'r\xc3\xa9sum\xc3\xa9'

decode_value_with_UTF8 = value.decode()
print(decode_value_with_UTF8)

encode_value_with_latin1 = str.encode(decode_value_with_UTF8, encoding='latin1')

print(encode_value_with_latin1)

decode_value_with_latin1 = encode_value_with_latin1.decode('latin1')

print(decode_value_with_latin1)
