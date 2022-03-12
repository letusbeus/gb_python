# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.
#
numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
           'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


# Вариант 1: числительное для перевода указывается непосредственно при обращении к функции


def num_translate(eng_num):
    if eng_num not in numbers:
        print('None')
    else:
        print(numbers[eng_num])


num_translate("one")

# Либо:


def num_translate(eng_num):
    print(numbers.get(eng_num, None))


num_translate('six')


# Вариант 2: числительное передается в консоль пользователем

eng_num_1 = input('Enter the number: ')


def num_translate_adv():
    if eng_num_1 not in numbers:
        print('None')
    else:
        print(numbers[eng_num_1])


num_translate_adv()
