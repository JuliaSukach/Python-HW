# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# Итогом в файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

str_1 = input('Enter first string: ').strip()
str_2 = input('Enter second string: ').strip()
str_3 = input('Enter third string: ').strip()
str_4 = input('Enter fourth string: ').strip()

new_file = open("text.txt", "w")
new_file.write(f'{str_1}\n{str_2}')
new_file.close()

created_file = open("text.txt", "a")
created_file.write("\n{third_line}\n{fourth_line}".format(third_line=str_3, fourth_line=str_4))
created_file.close()
