# 2. * (вместо задачи 1)
# Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы —
# результат тоже должен быть с заглавной.
# Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"
#
numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
           'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

# Вариант 1: числительное для перевода указывается непосредственно при обращении к функции


def num_translate(eng_num):
    if eng_num.istitle():
        print(numbers[eng_num.lower()].title())
    elif eng_num not in numbers:
        print('None')
    else:
        print(numbers[eng_num])


num_translate("Ten")

# Вариант 2: числительное передается в консоль пользователем

eng_num_1 = input('Enter the number: ')


def num_translate_adv():
    if eng_num_1.istitle():
        print(numbers[eng_num_1.lower()].title())
    elif eng_num_1 not in numbers:
        print('None')
    else:
        print(numbers[eng_num_1])


num_translate_adv()


def num_translate(eng_num):
    if eng_num.istitle():
        print(numbers.get(eng_num.lower()).title())
    else:
        print(numbers.get(eng_num, None))


num_translate('Two')
