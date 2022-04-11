"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep
from colorama import Fore, Style

"""
Зацикленный вариант
"""


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Внимание! Загорелся {TrafficLight.__color[i]} цвет светофора')
            if i == 0:
                sleep(7)
                i += 1
            elif i == 1:
                sleep(2)
                i += 1
            elif i == 2:
                sleep(15)
                i = 0


# traffic_light = TrafficLight()
# traffic_light.running()


"""
Разовый запуск с цветовым выводом
"""


class TrafficLight_:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        i = 0
        while i < 3:
            if i == 0:
                print(f'{Fore.RED}{TrafficLight_.__color[i].upper()}{Style.RESET_ALL}')
                sleep(7)
            elif i == 1:
                print(f'{Fore.YELLOW}{TrafficLight_.__color[i].upper()}{Style.RESET_ALL}')
                sleep(2)
            elif i == 2:
                print(f'{Fore.GREEN}{TrafficLight_.__color[i].upper()}{Style.RESET_ALL}')
                sleep(15)
            i += 1


traffic_light_ = TrafficLight_()
traffic_light_.running()
