# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки?
# Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?


def thesaurus(*names):   # Выдает на выходе словарь ключ (первая буква имени): значение (имя)
    names_dict = {}
    for name in names:
        if name[0] not in names_dict:
            names_dict.setdefault(name[0], [name])
        else:
            names_dict[name[0]].append(name)
    print(names_dict)


thesaurus("Иван", "Мария", "Петр", "Илья", "Денис", "Сергей", "Семен")


def thesaurus(*names):   # Выдает на выходе отсортированный по ключам словарь
    names_dict = {}
    for name in names:
        if name[0] not in names_dict:
            names_dict.setdefault(name[0], [name])
        else:
            names_dict[name[0]].append(name)
    print(dict(sorted(names_dict.items())))


thesaurus("Иван", "Мария", "Петр", "Илья", "Денис", "Сергей", "Семен")




















