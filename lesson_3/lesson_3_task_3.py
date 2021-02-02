"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg_1, arg_2, arg_3):
    list_arg = [arg_1, arg_2, arg_3]
    list_arg.remove(min(list_arg))
    result = list_arg[0] + list_arg[1]
    return result


value1 = int(input('Введите первый аргумент: '))
value2 = int(input('Введите второй аргумент: '))
value3 = int(input('Введите третий аргумент: '))
print('Сумма наибольших двух аргументов равна: ', my_func(value1, value2, value3))
