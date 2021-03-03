import re


class Data:
    def __init__(self, data_month_year):
        self.data_month_year = data_month_year
        print(self.data_month_year)

    @classmethod
    def type_int(cls, data_month_year):
        list_str = str(data_month_year)
        list1 = re.findall(r'\d+', list_str)
        list2 = list(map(int, list1))
        print(list2)

    @staticmethod
    def valid(data, month, year):
        if 1 <= data <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return print('Дата, месяц, год набраны верно')
                else:
                    return print('Неправильный год')
            else:
                return print('Неправильный месяц')
        else:
            return print('Неправильная дата')


ms = Data('24-10-2021')
Data.type_int('22-09-2021')
Data.valid(10, 10, 2021)
Data.valid(10, 10, 2031)
