"""
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и
выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


a = calc_cube(5)
125
a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
"""

from functools import wraps


def val_checker(decorator_check_func):
    def _val_checker(func_calc_cube):
        @wraps(func_calc_cube)
        def wrapped(x):
            err_msg = f'Введено неверное число: '
            if decorator_check_func(x):
                return func_calc_cube(x)
            else:
                raise ValueError(f'{err_msg}{x}')

        return wrapped

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """calc_cube вычисляет куб числа x"""
    return x ** 3


a = calc_cube(3)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)
print(calc_cube.__code__)
print(calc_cube.__closure__)
