import random

def new_list(n):
    list1 = []
    for _ in range(n):
        list1.append((random.randint(-n, n)))
    return list1

def mult_elem(list1):
    list2 = []
    i_start = 0
    i_end = len(list1) - 1
    while i_start <= i_end:
        list2.append(list1[i_start] * list1[i_end])
        i_start += 1
        i_end -= 1
    return list2

num = int(input('Введите количество элементов списка: '))
my_list = new_list(num)
print(my_list)
print(mult_elem(my_list))