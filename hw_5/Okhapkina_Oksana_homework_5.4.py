# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# ```
# Подсказка: использовать возможности python, изученные на уроке.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# В лоб
result = []
for num in range(len(src) - 1):
    if src[num] < src[num + 1]:
        result.append(src[num + 1])
        num += 1

print(result)

# Оптимизировано
res = [src[num + 1] for num in range(len(src) - 1) if src[num] < src[num + 1]]
print(res)
