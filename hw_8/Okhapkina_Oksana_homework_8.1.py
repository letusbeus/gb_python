"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
и почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError.
Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
"""


def email_parse(email):
    email_dict = {}
    err_msg = f'wrong email: {email}'
    for _ in email:
        if '@' in email and email.split('@')[1].__contains__('.'):
            email_dict.setdefault('username', email.split('@')[0])
            email_dict['domain'] = email.split('@')[1]
        else:
            raise ValueError(err_msg)
    print(email_dict)


import re

EMAIL = re.compile(r'([a-z0-9_\.]+)@([a-z0-9]+\.[a-z]+)')


def email_parse_re(email):
    email_dict = {}
    err_msg = f'wrong email: {email}'
    found_info = EMAIL.findall(email)
    if found_info:
        name, addr = found_info[0]
        email_dict.setdefault('username', name)
        email_dict['domain'] = addr
    else:
        raise ValueError(err_msg)
    print(email_dict)


email_parse_re('someone@geekbrains.ru')
email_parse_re('qwety@geekbrains.ru')
email_parse_re('123@geekbrains.ru')
# email_parse_re('someone@geekbrainsru')
# email_parse_re('qwertyqwerty.ru')
email_parse('someone@geekbrains.ru')
email_parse('qwety@geekbrains.ru')
email_parse('123@geekbrains.ru')
# email_parse('someone@geekbrainsru')
# email_parse('qwertyqwerty.ru')
