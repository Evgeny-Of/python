class Cell:
    def __init__(self, number_of):
        self.number_of = int(number_of)

    def __add__(self, other):
        return print(f' Число ячеек общей клетки: {self.number_of + other.number_of}')

    def __sub__(self, other):
        sub_result = self.number_of - other.number_of
        return print(f'Результат операции вычитания: {sub_result}' if sub_result > 0 else f'Результат меньше нуля!')

    def __mul__(self, other):
        return print(f'Результат умножения ячеек: {self.number_of * other.number_of}')

    def __truediv__(self, other):
        return print(f'Результат деления ячеек: {self.number_of // other.number_of}')

    def make_order(self, row_length: int):
        for i in range(self.number_of // row_length):
            print("*" * row_length + '\\n', end='')
        print('*' * (self.number_of % row_length))


c1 = Cell(5)
c2 = Cell(24)
c1 + c2
c2 - c1
c1 * c2
c1 / c2
c1.make_order(3)
c2.make_order(5)
