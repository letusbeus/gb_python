"""
3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
какой тип данных лучше использовать в ответе функции?
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


currency_rates('EuR')
currency_rates('usd')
