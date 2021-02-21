"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed != 0:
            if self.is_police == False:
                return print(f'Автомобиль {self.name} цвета {self.color} поехал')
            else:
                return print(f'Автомобиль полиции цвета {self.color} поехал')

    def stop(self):
        if self.speed == 0:
            if self.is_police == False:
                return print(f'Автомобиль {self.name} остановился')
            else:
                return print(f'Автомобиль полиции цвета {self.color} поехал')

    def turn(self, direction):
        self.direction = direction
        if self.is_police == False:
            return print(f'Автомобиль {self.name} повернул {self.direction}')
        else:
            return print(f'Автомобиль полиции повернул {self.direction}')

    def show_speed(self):
        if self.is_police == False:
            return print(f'Текущая скорость автомобиля {self.name} равна: {self.speed}')
        else:
            return print(f'Текущая скорость автомобиля полиции равна: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print(f'У Вас фиксируется превышение скорости!')
        else:
            return print(f'Текущая скорость автомобиля {self.name} равна: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return print(f'У Вас фиксируется превышение скорости!')
        else:
            return print(f'Текущая скорость автомобиля {self.name} равна: {self.speed}')


class PoliceCar(Car):
    pass


ms = TownCar(30, 'синий', 'ВАЗ', False)
ms.go(), ms.stop(), ms.turn('направо'), ms.show_speed()

mq = SportCar(0, 'красный', 'BMW', False)
mq.go(), mq.stop(), mq.turn('направо'), mq.show_speed()

ms = WorkCar(60, 'белый', 'Audi', False)
ms.go(), ms.stop(), ms.turn('направо'), ms.show_speed()

ms = PoliceCar(80, 'синий', 'Ford', True)
ms.go(), ms.stop(), ms.turn('направо'), ms.show_speed()
