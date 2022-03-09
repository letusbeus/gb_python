# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# 1. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# 2. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# 3. * Решить задачу под пунктом 2, не создавая новый список.

my_list = []
total = 0
total_17 = 0
for i in range(1, 1000):
    my_list.append(i ** 3)
for number in my_list:
    my_sum = 0
    temp_number = number
    while temp_number != 0:
        my_sum += temp_number % 10
        temp_number //= 10
    if my_sum % 7 == 0:
        total += number
for number in my_list:
    my_sum = 0
    temp_number_17 = number + 17
    while temp_number_17 != 0:
        my_sum += temp_number_17 % 10
        temp_number_17 //= 10
    if my_sum % 7 == 0:
        total_17 += (number + 17)
print(total)
print(total_17)
