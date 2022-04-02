"""
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
nginx_logs.txt (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

with open('nginx_logs.txt', 'r', encoding='utf-8') as logs:
    response = []
    for line in logs:
        remote_addr = line.split(' ')[0]
        request_type = line.split(' ')[5][1:]
        requested_resource = line.split(' ')[6]
        response.append((remote_addr, request_type, requested_resource))
print(*response, sep='\n')
