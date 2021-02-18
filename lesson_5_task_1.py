"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

first_file = open('file_task_1.txt', 'w')
while True:
    str_list = input('Введите данные: ')
    if str_list == '':
        break
    else:
        first_file.writelines(str_list + '\n')
first_file.close()
