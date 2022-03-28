"""
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.
"""
import requests
from lxml import etree


def currency_rates(cur):
    url = 'https://www.cbr.ru/currency_base/daily/'
    headers = {'Content-Type': 'text/html'}
    response = requests.get(url, headers=headers).text
    htmlparser = etree.HTMLParser()
    tree = etree.fromstring(response, htmlparser)
    cbr_date = tree.xpath('/html/body/main/div/div/div/div[2]/form/div/div/div/div/div/button/text()')
    cbr_cur = tree.xpath('//table/tbody/tr /td[2]/text()')
    cbr_rate = tree.xpath('//table/tbody/tr /td[5]/text()')
    dict_cur_rates = dict(zip(cbr_cur, cbr_rate))
    cur = cur.upper()
    if cur not in dict_cur_rates:
        print(None)
    else:
        print(dict_cur_rates.get(cur.upper()), *cbr_date, sep=', ')


def main():
    currency_rates('Eur')
    currency_rates('usd')


if __name__ == "__main__":
    main()
