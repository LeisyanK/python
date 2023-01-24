import random


def new_list(n):
    list1 = []
    for _ in range(n):
        list1.append((random.randint(-n, n)))
    return list1


def summa(x):
    sum1 = 0
    for i in x:
        sum1 += i
    return sum1


def func(op, x):
    return op(x)


# num = int(input('Введите количество элементов списка: '))
num = 10
my_list = new_list(num)
print(my_list)
# list2 = list(range(-num, num))
# print(list2)

list2 = [my_list[i] for i in range(len(my_list)) if my_list[i] % 2 != 0]
print('через List Comprehension: ', list2)
res = list(filter(lambda x: x % 2 != 0, my_list))
print('через filter и lambda: ', res)
print(func(summa, list2))
