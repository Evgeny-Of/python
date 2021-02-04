a = float(input('a= '))
b = float(input('b= '))
k = 1
while a <= b:
    a = a + a / 10
    k += 1
    # print(a)
print('На', k, '- й день спортсмен достиг результата - не менее', int(b), 'км.')
