class Matrix:
    def __init__(self, matrix_param):
        self.matrix_param = matrix_param

    def __str__(self):
        return '\n'.join('  '.join(map(str, element)) for element in self.matrix_param)

    def __add__(self, other_param):
        for el in range(len(self.matrix_param)):
            for i in range(len(other_param.matrix_param[el])):
                self.matrix_param[el][i] = self.matrix_param[el][i] + other_param.matrix_param[el][i]
        return '\n'.join('  '.join(map(str, element)) for element in self.matrix_param)


mc1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mc2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Матрица1:')
print(mc1.__str__())
print('Матрица2:')
print(mc2.__str__())
print('Результат:')
print(mc1.__add__(mc2))
