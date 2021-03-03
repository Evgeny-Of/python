class MyError(Exception):
    def __init__(self, text):
        self.text = text


num = True
list_numbers = []
while num == True:
    number = input('Введите число и нажмите ввод. Для завершения программы наберите stop: ')
    if number == 'stop':
        num = False
    else:
        try:
            list_numbers.append(int(number))
        except:
            print('Ошибка! Вы ввели не число! Введите число!')
    print('Полученный список чисел: ', list_numbers)
