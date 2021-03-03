class WareHouse:
    def __init__(self, *args):
        self.args = args

    def equip(self):
        return print('На сегодняшний день на складе имеется следующая продукция: ', self.args)


class Equipment:
    def __init__(self, name, year, price, quantity):
        self.name = name
        self.year = year
        self.quantity = quantity
        self.price = price
        self.inform = [{'Модель устройства': self.name, 'Год выпуска': self.year,
                        'Количество': self.quantity, 'Цена за ед': self.price}]

    def equipments(self):
        num = True
        while num == True:
            print('Мы получили данные о новой оргтехнике, поступающей на склад: \n', self.inform)
            number = input('Имеется ли еще оргтехника, которую необходимо оприходовать на складе? (да/нет) ')
            if number == 'нет':
                num = False
            else:
                try:
                    name = input(f'Введите модель устройства: ')
                    year = input('Введите год выпуска продукта: ')
                    price = int(input(f'Введите цену за ед: '))
                    quantity = int(input(f'Введите количество устройств: '))
                    new_equip = {'Модель устройства': name, 'Год выпуска': year,
                                 'Количество': quantity, 'Цена за ед': price}
                    self.inform.append(new_equip)
                except ValueError:
                    print('Введены неверные данные!')

    def transfer(self):
        print('Склад передает подразделению качества следующие товары: \n', self.inform)

    def subdivision(self):
        print('Подразделение качества принимиет следующий список товаров: \n', self.inform)


class Printer(Equipment):
    def __init__(self, name, price, quantity, year, type_devise, color):
        super().__init__(name, price, quantity, year)
        self.type_devise = type_devise
        self.color = color
        print('Уникальные особенности товара (Принтер), находящегося на складе:')
        print('Тип принтера: ', self.type_devise)
        print('Цвет принтера: ', self.color)


class Scanner(Equipment):
    def __init__(self, name, price, quantity, year, type_devise, color):
        super().__init__(name, price, quantity, year)
        self.type_devise = type_devise
        self.color = color
        print('Уникальные особенности товара (Сканер), находящегося на складе:')
        print('Тип сканера: ', self.type_devise)
        print('Цвет сканера: ', self.color)


class Copier(Equipment):
    def __init__(self, name, price, quantity, year, type_devise, color):
        super().__init__(name, price, quantity, year)
        self.type_devise = type_devise
        self.color = color
        print('Уникальные особенности товара (Ксерокс), находящегося на складе:')
        print('Тип ксерокса: ', self.type_devise)
        print('Цвет ксерокса: ', self.color)


mc1 = WareHouse('Принтер', 'Сканер', 'Ксерокс')
mc1.equip()
wer1 = Printer('Принтер HP', 200, 2021, 22, 'Лазерный', 'Черный')
wer2 = Copier('Ксерокс Canon', 180, 2020, 12, 'Лазерный', 'Серый')
qqq = Equipment('Принтер HP', 200, 2021, 23)
qqq.equipments()
qqq.transfer()
qqq.subdivision()
