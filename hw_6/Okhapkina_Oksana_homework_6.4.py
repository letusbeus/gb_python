"""
4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество для пользователей и
название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге.
В словаре должны храниться данные, полученные в результате парсинга.
"""
from itertools import zip_longest

u = open('users.csv', 'r', encoding='utf-8')
users = u.readlines()
h = open('hobbies.csv', 'r', encoding='utf-8')
hobbies = h.readlines()
with open('users_hobby.txt', 'w', encoding='utf-8') as uh:
    if len(hobbies) > len(users):
        exit(1)
    for user, hobby in zip_longest(users, hobbies, fillvalue=None):
        user_hobby = str(user).strip() + ': ' + str(hobby).strip() + '\n'
        uh.write(user_hobby)
u.close()
h.close()
