"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("file_task_5.txt", "w") as file_five:
    numbers = input('Введите набор чисел, разделенных пробелами: ')
    file_five.write(numbers)
with open("file_task_5.txt", "r") as file_sum_numbers:
    content = file_sum_numbers.readlines()
    for num in content:
        str_numbers = num.split()
num_list = []
for el in str_numbers:
    num_list.append(int(el))
print('Сумма чисел в файле равна: ', sum(num_list))
