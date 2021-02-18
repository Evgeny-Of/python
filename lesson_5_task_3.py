"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
file_three = open('file_task_3.txt', 'r', encoding='utf-8')
content = file_three.readlines()
surname = []
aver_list = []
for num in content:
    str_word = num.split()
    aver_list.append(int(str_word[1]))
    if int(str_word[1]) < 20000:
        surname.append(str_word[0])
average = sum(aver_list) / len(aver_list)
print('Список сотрудников, которые имеют оклад меньше 20 тыс. руб.: ', surname)
print('Средняя величина дохода сотрудников: ', average)
file_three.close()
