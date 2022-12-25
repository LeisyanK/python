import random

def new_list(n):
    list1 = []
    for _ in range(n):
        list1.append((random.randint(-n, n)))
    return list1

def sum_odd_elem(list1):
    index = 1
    summa = 0
    while index < len(list1):
        summa += list1[index]
        index += 2
    return summa

num = int(input('Введите количество элементов списка: '))
my_list = new_list(num)
print(my_list)
print('Сумма нечетных элементов = ', sum_odd_elem(my_list))
