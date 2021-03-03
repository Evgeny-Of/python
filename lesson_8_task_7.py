class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        print(f"Имеется комплексное число: {self.real}+{self.imaginary}j")

    def __add__(self, other):
        return print(f'Результат сложения двух комплексных чисел: \n'
                     f'{self.real + other.real}+{self.imaginary + other.imaginary}j')

    def __mul__(self, other):
        return print(f'Результат умножения двух комплексных чисел: \n'
                     f'{self.real * other.real - self.imaginary * other.imaginary}+'
                     f'{self.real * other.imaginary + self.imaginary * other.real}j')


mc = ComplexNumber(2, 1)
mc1 = ComplexNumber(3, 4)
mc + mc1
mc * mc1
