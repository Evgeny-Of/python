number_off = 'да'
products_end = []
num = 0
analytics = {}
name_list = []
cost_list = []
quantity_list = []
unit_list = []

"""
number_off - Дает возможность вводить новые товары, характеристики которых мы хотим учитывать в структуре данных: 
ответ: да - вводим еще товар, нет - больше нет товаров.
"""

while number_off == 'да':
    num += 1
    name = str(input('Введите название товара: '))
    cost = int(input('Введите стоимость товара: '))
    quantity = int(input('Введите количество товара: '))
    unit = str(input('Введите единицу измерения (ед / шт): '))
    number_off = str(input('Продолжить ввод товаров? (да / нет): '))

    products_dict = {'название': name, 'цена': cost, 'количество': quantity, 'ед.': unit}
    products_tur = (num, products_dict)
    products = [products_tur]
    products_end.extend(products)

    # Аналитика о введенных товарах

    name_list.append(name)
    cost_list.append(cost)
    quantity_list.append(quantity)
    unit_list.append(unit)
    analytics = {'название': name_list, 'цена': cost_list,
                 'количество': quantity_list, 'ед.': list(set(unit_list))}
    # Окончание аналитики

print('Структура данных "Товары": ', products_end)
print('Аналитика о товарах: ', analytics)
