"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, volume, height):
        super().__init__(_length, _width)
        self.volume = volume
        self.height = height

    def mass_count(self):
        return self._length * self._width * self.volume * self.height


r = MassCount(5000, 20, 25, 5)
print(f'Для покрытия дороги длиной {r._length} м., шириной {r._width} м., толщиной {r.height} см. '
      f'при расходе асфальта {r.volume} кг. на 1 кв.м. потребуется {int(r.mass_count()/1000)} т. асфальта')
