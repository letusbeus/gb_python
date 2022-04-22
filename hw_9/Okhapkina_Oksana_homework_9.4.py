"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'The {self.name} started'

    def stop(self):
        return f'The {self.name} stopped'

    def right(self):
        return f'{self.name} turned right'

    def left(self):
        return f'{self.name} turned left'

    def show_speed(self):
        return f'{self.name}\'s current speed is {self.speed} kmH.'

    def police(self):
        if self.is_police:
            return f'{self.name} is a police car.'
        else:
            return f'{self.name} is not a police car.'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'CAUTION! {self.name} driver, you have exceeded the speed limit! '\
                   f'Your current speed is higher than allowed by {self.speed - 60} kmH, please slow down.'
        else:
            return f'{self.name} driver, your current speed is {self.speed} kmH.'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'CAUTION! {self.name} driver, you have exceeded the speed limit!\n' \
                   f'Your current speed is higher than allowed by {self.speed - 40} kmH, please slow down.'
        else:
            return f'{self.name} current speed is {self.speed} kmH.'


class PoliceCar(Car):
    pass


audi = SportCar(100, 'Red', 'Audi', False)
oka = TownCar(130, 'White', 'OKA', False)
lada = WorkCar(30, 'Баклажан', 'Лада Седан', False)
ford = PoliceCar(110, 'Blue', 'Ford', True)
print(lada.left())
print(f'{lada.go()} and moves with current speed {lada.show_speed().split()[-2]} kmH.')
print(f'{lada.name}\'s color is {lada.color}')
print(f'Is {audi.name} a police car? {audi.police()}')
print(f'Is {lada.name} a police car? {lada.police()}')
print(audi.show_speed())
print(oka.show_speed())
print(oka.police())
print(ford.police())
print(ford.show_speed())
