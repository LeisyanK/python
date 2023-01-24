# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# def mult(x):
#     mult_x = 1
#     for

num = int(input('Введите число: '))
# list1 = [1]
# proizv = 1
# for el in range(2, num + 1):
#     proizv *= el
#     list1.append(proizv)
# print(list1)

def f(x):
    mult = 1
    # print(x)
    for i in range(1, x + 1):
        mult *= i
    return mult


list2 = [el for el in range(1, num+1)]
print(list2)
# list2 = [lambda el: el for el in range(1, num+1)]
list2 = list(map(f, list2))
# list2 = list(map(lambda el: el*list2[el-1], list2))
print(list2)