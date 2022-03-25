"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
"""
import requests
from lxml import etree


def currency_rates(cur):
    url = 'https://www.cbr.ru/currency_base/daily/'
    headers = {'Content-Type': 'text/html'}
    response = requests.get(url, headers=headers).text
    htmlparser = etree.HTMLParser()
    tree = etree.fromstring(response, htmlparser)
    cbr_cur = tree.xpath('//table/tbody/tr /td[2]/text()')
    cbr_rate = tree.xpath('//table/tbody/tr /td[5]/text()')
    dict_cur_rates = dict(zip(cbr_cur, cbr_rate))
    cur = cur.upper()
    if cur not in dict_cur_rates:
        print(None)
    else:
        print(dict_cur_rates.get(cur.upper()))


currency_rates('EuR')
currency_rates('usd')
