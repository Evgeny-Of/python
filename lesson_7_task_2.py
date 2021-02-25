from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, size_height):
        self.size_height = size_height

    @property
    def square(self):
        return f'Площадь ткани общая: {(self.size_height / 6.5 + 0.5) + (self.size_height * 2 + 0.3)}'

    @abstractmethod
    def abstract_method(self):
        return print('Абстрактный метод')


class Coat(Cloth):
    def __init__(self, size_height):
        super().__init__(size_height)
        self.result_coat = self.size_height / 6.5 + 0.5

    def __str__(self):
        return print(f'Площадь ткани на пальто: {self.result_coat}')

    def abstract_method(self):
        return print('Абстрактный метод Coat')


class Costume(Cloth):
    def __init__(self, size_height):
        super().__init__(size_height)
        self.result_costume = round(self.size_height * 2 + 0.3)

    def __str__(self):
        return print(f'Площадь ткани на костюм: {self.result_costume}')

    def abstract_method(self):
        return print('Абстрактный метод Costume')


coat = Coat(7)
costume = Costume(10)
print(coat.square)
print(costume.square)
coat.abstract_method()
costume.abstract_method()
