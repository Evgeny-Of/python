"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы
сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from function_les_4 import wage
from sys import argv

name, work, rate, bonus = argv
print('Название скрипта: ', name)
print('Заработная плата сотрудника составляет: ', wage(work, rate, bonus))
