"""
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
задания.
Примечания: спамер — это клиент, отправивший больше всех запросов;
код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

with open('nginx_logs.txt', 'r', encoding='utf-8') as logs:
    logs = logs.readlines()
    spamer = {}
    for line in logs:
        remote_addr = str(*line.split(' ')[0:1])
        if remote_addr in spamer:
            spamer[remote_addr] += 1
        else:
            spamer.setdefault(remote_addr, 1)
print(f'IP-адрес: {max(spamer, key=spamer.get)}, отправлено запросов: {max(spamer.values())}')
