"""
2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения
информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>,
<response_size>), например:

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0
"-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
Можно ли для них уточнить регулярное выражение?
"""

"""С созданием списка без присвоения переменных"""
# with open('nginx_logs.txt', 'r', encoding='utf-8') as logs:
#     parsed_raw = []
#     for line in logs:
#         line = line.split(" ")
#         parsed_raw.append(
#             (line[0],
#              line[3].strip("[") + " " + line[4].strip("]"),
#              line[5][1:],
#              line[6],
#              line[8],
#              line[9]
#              )
#         )
#     for i in parsed_raw:
#         print(i)
"""С созданием списка с присвоением переменных"""
# with open('nginx_logs.txt', 'r', encoding='utf-8') as logs:
#     parsed_raw = []
#     for line in logs:
#         line = line.split(" ")
#         remote_addr = line[0]
#         request_datetime = line[3].strip("[") + ' ' + line[4].strip("]")
#         request_type = line[5][1:]
#         requested_resource = line[6]
#         response_code = line[8]
#         response_size = line[9]
#         parsed_raw.append(
#             (remote_addr, request_datetime, request_type, requested_resource, response_code, response_size)
#         )
#     for i in parsed_raw:
#         print(i)
"""Построчно сразу в print"""
# with open('nginx_logs.txt', 'r', encoding='utf-8') as logs:
#     for line in logs:
#         line = line.split(" ")
#         parsed_raw = f'{line[0]}, ' \
#                      f'{line[3][1:]} {line[4][:-1:]}, ' \
#                      f'{line[5][1:]}, ' \
#                      f'{line[6]}, ' \
#                      f'{line[8]}, ' \
#                      f'{line[9]}'
#         print(parsed_raw)
"""
С использованием re.compile; обрабатываются все строки, в т.ч. строки вида 
2a01:7e00::f03c:91ff:fe70:a4cc - - [18/May/2015:16:05:29 +0000] "GET /downloads/product_1 ...
"""
import re

PAD = re.compile(r'([+\S]*) - - \[([0-9]{,2}/\w+/[0-9]{4}(?::[0-9]{,2}){3} \+[0-9]{4})]'
                 r' "(\w+) ([/\w+]*) +\S+" ([0-9]+) ([0-9]+)')
with open('nginx_logs.txt', 'r', encoding='utf-8') as logs:
    parsed_raw_ = []
    for arg in PAD.findall(logs.read()):
        addr, datetime, r_type, resource, code, size = arg
        parsed_raw_.append(arg)
for i in enumerate(parsed_raw_):
    print(i)
