"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

with open("file_task_7.txt", "r", encoding='utf-8') as file_seven:
    content = file_seven.readlines()
    dict_list_profit = {}
    dict_list_average_profit = {}
    average_profit = 0
    col = 1
    summa_profit = 0
    summa_loss = 0
    for el in content:
        number = el.split()
        for i in number:
            profit = float(number[2]) - float(number[3])
        if profit >= 0:
            summa_profit = summa_profit + profit
        else:
            summa_loss = summa_loss + profit
        average_profit = summa_profit / col
        col += 1
        key_profit = number[0]
        key_average_profit = 'average_profit'
        dict_list_profit.update({key_profit: profit})
        dict_list_average_profit.update({key_average_profit: average_profit})
result = [dict_list_profit, dict_list_average_profit]
print('Словарь с фирмами и их прибылями ("-" убытками): ', dict_list_profit)
print("Словарь со средней прибылью: ", dict_list_average_profit)
print('Результативный список: ', result)

with open("file_task_7_json.json", "w") as json_file_result:
    json.dump(result, json_file_result)
