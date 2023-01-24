list1 = ['abc', '45', 'def', 'kmds', 'def', '875']
num = input('Введите число: ')
if num in list1:
    print('Есть!')
else:
    print('Нет!')

# функция lambda
def exists(op, x, str):
    return op(x, str)

ex = exists((lambda n, str: n in str), num, list1)
print(ex)
# list1 = ['abc', '45', 'def', 'kmds', 'def', '875']
# num = input('Введите число: ')
# for i in range(len(list1)):
#     if list1[i] == num:
#         print('Число есть в списке')
#         break
#     # elif i == len(list1) - 1:
# # if i == len(list1) - 1 and list1[i] != num:
# else:
#     print('Числа нет в списке')

# list1 = ['abc', '45', 'def', 'kmds', 'def', '875']
# num = input('Введите число: ')
# flag = 0
# i = 0
# while not flag and i < len(list1):
#     if list1[i] == num:
#         flag = 1
#         print('Число присутствует в списке')
#     i = i + 1
# if not flag:
#     print('Числа нет в списке')