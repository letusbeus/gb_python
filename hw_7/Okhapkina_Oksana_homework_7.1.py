"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""

import os

temp = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in temp.items():
    if os.path.exists(root):
        exit('Папка "my_project" уже существует!')
    else:
        for folder in folders:
            new_struct = os.path.join(root, folder)
            os.makedirs(new_struct)
