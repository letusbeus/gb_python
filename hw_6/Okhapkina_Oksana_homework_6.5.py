"""
5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к
обоим исходным файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая, когда все файлы
находятся в разных папках.
"""
import sys
from itertools import zip_longest

users_path, hobby_path, out_path = sys.argv[1:]
u = open(users_path, 'r', encoding='utf-8')
users = u.readlines()
h = open(hobby_path, 'r', encoding='utf-8')
hobbies = h.readlines()
with open(out_path, 'w', encoding='utf-8') as uh:
    if len(hobbies) > len(users):
        exit(1)
    for user, hobby in zip_longest(users, hobbies, fillvalue=None):
        user_hobby = str(user).strip() + ': ' + str(hobby).strip() + '\n'
        uh.write(user_hobby)
u.close()
h.close()

# python Okhapkina_Oksana_homework_6.5.py "users.csv" "hobbies.csv" "hobby.txt"
