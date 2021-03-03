class MyError(Exception):
    def __init__(self, text):
        self.text = text


try:
    number1 = input('Введите делимое: ')
    number2 = input('Введите делитель: ')
    if int(number2) == 0:
        raise MyError('Ошибка! Деление на ноль!')
    func = int(number1) / int(number2)
except ValueError:
    print('Ошибка! Вы ввели не числа!')
except MyError as error:
    print(error)
else:
    print('Результат деления введенных чисел: ', func)
