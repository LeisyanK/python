import random

num = int(input('Введите количество элементов списка: '))
list1 = []
for _ in range(num):
    list1.append((random.randint(-num, num)))
print(list1)

index = 1
summa = 0
while index <= num:
    summa += list1[index]
    index += 2
print('Сумма нечетных элементов = ', summa)