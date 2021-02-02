# Функция (для задания 1) рассчитывает заработную плату сотрудника по формуле:
# [выработка в часах (work) * ставка в час (rate) + премия (bonus)]


def wage(work, rate, bonus):
    result = int(work) * int(rate) + int(bonus)
    return result


#  Вычисление произведения всех элементов списка (для задания 5).


def multiplication(arg_1, arg_2):
    return arg_1 * arg_2
