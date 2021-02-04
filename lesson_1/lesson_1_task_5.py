proceeds = float(input('Введите значение выручки фирмы: '))
cost = float(input('Введите значение издержек фирмы: '))
if proceeds > cost:
    profit = proceeds - cost
    eff = profit / proceeds
    print('Фирма имеет следующую прибыль:', profit)
    print('Рентабельность фирмы следующая:', eff)
    n = int(input('Введите численность сотрудников фирмы: '))
    profit_n = profit / n
    print('Прибыль фирмы в расчете на одного сторудника равна:', profit_n)
elif cost > proceeds:
    loss = cost - proceeds
    print('Фирма имеет убыток:', loss)
