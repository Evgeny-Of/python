"""
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания,
email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

"""


def func_data(email, surname, name, year, town, tel):
    data = [name, surname, year, town, email, tel]
    return data


arg_1 = (input('Введите имя: '))
arg_2 = (input('Введите фамилию: '))
arg_3 = int(input('Введите год рождения: '))
arg_4 = (input('Введите город проживания: '))
arg_5 = (input('Введите email: '))
arg_6 = int(input('Введите номер телефона: '))
print(*func_data(tel=arg_6, name=arg_1, surname=arg_2, town=arg_4, email=arg_5, year=arg_3))
