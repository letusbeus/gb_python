"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку
конструктора класса (метод __init__()), который должен принимать
данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
Следующий шаг — реализовать перегрузку метода __str__() для
вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации
операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять
поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки
второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        s = ''
        for i in range(len(self.matr)):
            s = s + '\t'.join(map(str, self.matr[i])) + '\n'
        return s

    def __add__(self, other):
        if len(self.matr) != len(other.matr):
            return f'Сложение матриц разной величины невозможно'
        else:
            for i in self.matr:
                for j in other.matr:
                    if len(i) != len(j):
                        return f'Сложение матриц разной величины невозможно'
            import copy
            result = copy.deepcopy(self.matr)
            for i in range(len(self.matr)):
                for k in range(len(self.matr[i])):
                    result[i][k] = self.matr[i][k] + other.matr[i][k]
            return Matrix(result)

    def __sub__(self, other):
        if len(self.matr) != len(other.matr):
            return f'Вычитание матриц разной величины невозможно'
        else:
            for i in self.matr:
                for j in other.matr:
                    if len(i) != len(j):
                        return f'Вычитание матриц разной величины невозможно'
            import copy
            result = copy.deepcopy(self.matr)
            for i in range(len(self.matr)):
                for k in range(len(self.matr[i])):
                    result[i][k] = self.matr[i][k] - other.matr[i][k]
            return Matrix(result)


list_1 = Matrix([[1, 2, 4], [33, 41, 50], [5, 6, 6]])
list_2 = Matrix([[70, 12, 4], [56, 30, 22], [52, 6, 19]])
print(f'Матрица М1 \n{list_1}')
print(f'Матрица М2 \n{list_2}')
print(f'М1 + М2\n{Matrix.__add__(list_1, list_2)}')
print(f'М2 - М1\n{Matrix.__sub__(list_2, list_1)}')
