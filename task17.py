# # # ПЕРВЫЙ СПОСОБ # # #

# import random
# poz1 = 1
# poz2 = 3
# num = int(input('Введите количество элементов списка: '))
# list1 = []
# for _ in range(num):
#     list1.append(random.randrange(-num, num))
# print(list1)
# print(f'{list1[poz1-1]} * {list1[poz2-1]} = {list1[poz1-1] * list1[poz2-1]}')

# # # ВТОРОЙ СПОСОБ # # #

# создаем файл
# data = open('text.txt', 'a')
# data.write('2\n')
# data.write('7\n')
# data.write('4\n')
# data.close()

import random

# находим максимальный индекс, записанный в файле
max_num = ''
data = open('text.txt', 'r')
for line in data:
    if line > max_num:
        max_num = line
data.close()
print(max_num)
max_num = int(max_num)

# запрашиваем количество элементов списка, превышающее максимальный индекс
num = 0
while num < max_num:
    num = int(input('Введите количество элементов списка: '))
print(num)

# заполняем список случайными числами
my_list = []
for _ in range(num):
    my_list.append(random.randint(-2 * num, 2 * num))
    #print(i, end=' ')
print(my_list)

# считаем произведение чисел
multipl = 1
data = open('text.txt', 'r')
for line in data:
    el = my_list[int(line) - 1]
    multipl *= el
    print(el, '*', sep=' ', end=' ')
data.close()
print('= ',multipl)