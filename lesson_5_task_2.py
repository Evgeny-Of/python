"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""

file_two = open(r'file_task_2.txt', 'r', encoding='utf-8')
content = file_two.readlines()
number_word = 1
for num in content:
    str_word = (num.split())
    print(f'Количество слов в {number_word} строке: ', len(str_word))
    number_word += 1
file_two.seek(0)
number_line = 0
for el in file_two:
    number_line += 1
print()
print(f'Количество строк в файле: ', number_line)
file_two.close()
