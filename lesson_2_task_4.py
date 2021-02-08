str_list = input('Введите несколько слов или чисел через пробел: ').split()
print(str_list)
num = 0
for elem in str_list:
    num += 1
    print(num, elem[:10])
