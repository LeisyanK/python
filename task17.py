import random
poz1 = 1
poz2 = 3
num = int(input('Введите количество элементов списка: '))
list1 = []
for _ in range(num):
    list1.append(random.randrange(-num, num))
print(list1)
print(f'{list1[poz1-1]} * {list1[poz2-1]} = {list1[poz1-1] * list1[poz2-1]}')