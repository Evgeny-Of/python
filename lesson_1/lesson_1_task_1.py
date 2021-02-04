perem1 = 1
perem2 = 'Переменная'
perem3 = True

print(perem1, perem2, perem3)
print(type(perem1), type(perem2), type(perem3))

perem4 = str(input('Введите строку: '))
perem5 = int(input('Введите число: '))
perem6 = float(input('Введите еще одно число: '))

print('Вот такие получились переменные:', perem4, perem5, perem6)

perem7 = perem1 + perem5
perem8 = int(perem6) + perem5 - perem1
perem9 = perem2 + str(perem7) + str(perem8)

print('.... и такие:', perem7, perem8, perem9)
