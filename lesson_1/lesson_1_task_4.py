number = int(input('Введите целое положительное число: '))
greatest = 0
while number > 0:
    remain = number % 10
    if remain > greatest:
        greatest = remain
    number //= 10
print(greatest)
