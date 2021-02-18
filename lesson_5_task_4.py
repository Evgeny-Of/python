"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

file_four = open('file_task_4.txt', 'r')
content = file_four.readlines()
rus_word = []
russian = ['Один', 'Два', 'Три', 'Четыре']
i = 0
for num in content:
    str_word = num.split()
    str_word.insert(1, russian[i])
    str_word.pop(0)
    i += 1
    line = ' '.join(str_word)
    with open("file_task_4_russian.txt", "a", encoding='utf-8') as rus_list:
        rus_list.writelines(line + '\n')
file_four.close()
