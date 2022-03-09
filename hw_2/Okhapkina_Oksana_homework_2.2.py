# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных
# разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для
# чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']
new_list = []
for i in my_list:
    if i.isdigit():
        new_list.append('"')
        new_list.append(f'{i:>02}')
        new_list.append('"')
    elif (i[0] == '+' or i[0] == '-') and i[1:].isdigit():
        x = i.replace(i[0], '')
        new_list.append('"')
        new_list.append(f'{i[0]}{x:>02}')
        new_list.append('"')
    else:
        new_list.append(i)
print(*new_list, sep=' ')


