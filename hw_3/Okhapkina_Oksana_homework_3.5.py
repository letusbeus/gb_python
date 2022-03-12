# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
#
import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера был", "завтра будет", "позавчера был", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    """Возвращает заданное пользователем количество n фраз, состоящих из произвольных (random) элементов списка
    (по одному элементу из каждого списка в каждой фразе)"""
    for n in range(0, n):
        random_noun = random.choice(nouns)
        random_adverbs = random.choice(adverbs)
        random_adjectives = random.choice(adjectives)
        print(f'{random_noun} {random_adverbs} {random_adjectives}', end=', ')


get_jokes(2)
print('\n')

"""Решение через создание списка"""


def get_jokes(n):
    """Возвращает заданное пользователем количество n фраз, состоящих из произвольных (random) элементов списка
    (по одному элементу из каждого списка в каждой фразе)"""
    joke = []
    for n in range(0, n):
        joke.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    print(joke)


get_jokes(3)


def get_jokes(n):                                 # Oneline solution
    print([f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}' for _ in range(0, n)])


get_jokes(5)
