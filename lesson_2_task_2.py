list1 = input('введите несколько слов или чисел через пробел: ')
list2 = list1.split()
print(list1)
i = 1
while i < len(list2):
    if i > len(list2):
        break
    list2[i - 1], list2[i] = list2[i], list2[i - 1]
    i += 2
print('Результат после обмена соседними значениями:')
print(*list2)
