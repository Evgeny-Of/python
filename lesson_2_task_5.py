rating = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
while rating:
    rat = int(input('Введите новый элемент рейтинга: '))
    print('Задан рейтинг:   ', rating)
    rating.reverse()
    if rating.count(rat) != 0:
        rat_index = rating.index(rat)
        rating.insert(int(rat_index), rat)
        rating.reverse()
        print('Получен рейтинг: ', rating)
    else:
        rating.append(rat)
        rating.reverse()
        print('Получен рейтинг: ', rating)
