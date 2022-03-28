# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

n = 19
print('Вариант 1')
for i in range(1, n + 1, 2):
    print(i)

odd_to_15 = [i for i in range(1, n + 1) if i % 2 != 0]
print('\nВариант 2', *odd_to_15, sep='\n')

print('\nВариант 3', *[i for i in range(1, n + 1) if i % 2 != 0], sep='\n')
