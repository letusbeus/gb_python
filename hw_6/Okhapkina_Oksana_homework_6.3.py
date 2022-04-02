"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями —
запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):

Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби (hobby.csv):

скалолазание,охота
горные лыжи
"""

from itertools import zip_longest
import json

u = open('users.csv', 'r', encoding='utf-8')
user = u.readlines()
h = open('hobbies.csv', 'r', encoding='utf-8')
hobby = h.readlines()
with open('user_hobby.csv', 'w', encoding='utf-8') as uh:
    if len(hobby) > len(user):
        exit(1)
    user_hobby = dict(zip_longest(user, hobby, fillvalue='None'))
    json.dump(user_hobby, uh, ensure_ascii=False)
print(user_hobby)
u.close()
h.close()
