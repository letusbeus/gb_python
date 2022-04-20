from random import randint


def card():
    def gen_unique_nums():
        loto_nums = []
        while len(loto_nums) < 15:
            unique_num = randint(1, 90)
            if unique_num not in loto_nums:
                loto_nums.append(unique_num)
        return loto_nums

    unique_nums = gen_unique_nums()
    card_nums = []
    empty_char = '  '
    delimiter = '--------------------------'
    row_1 = sorted(unique_nums[:5])
    while len(row_1) < 9:
        row_1.insert(randint(0, len(row_1)), empty_char)
    row_2 = sorted(unique_nums[5:10])
    while len(row_2) < 9:
        row_2.insert(randint(0, len(row_2)), empty_char)
    row_3 = sorted(unique_nums[10:])
    while len(row_3) < 9:
        row_3.insert(randint(0, len(row_3)), empty_char)
    card_nums.extend(
        [delimiter, ' '.join(map(str, row_1)), ' '.join(map(str, row_2)), ' '.join(map(str, row_3)), delimiter])
    loto_card = '\n'.join(map(str, card_nums))
    return loto_card


user_card = card()
pc_card = card()
print(f'------ Ваша карточка -----\n{user_card}')
print(f'-- Карточка компьютера ---\n{pc_card}')


def keg():
    unique_keg_num = randint(1, 90)
    if unique_keg_num not in keg_used_nums:
        keg_used_nums.append(unique_keg_num)
    return f'Новый бочонок: {unique_keg_num}, осталось бочонков: {90 - len(keg_used_nums)}'


keg_used_nums = []
# print(keg())
