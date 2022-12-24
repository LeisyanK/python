num = input('Введите вещественное число: ')
summa = 0
for el in num:
    if el.isdigit():
        summa += int(el)
print('Сумма цифр числа =', summa)

# # num = input('Введите вещественное число: ')
# summa = 0
# for el in range(len(num)):
#     if num[el] != '.':
#         summa += int(num[el])
# print('Сумма цифр числа =', summa)

# num = '-123.4'
summa = 0
print('Второй способ')
if '.' in num:
    degree = len(num) - num.find('.')
    # print(degree)
    num = int(float(num) * 10 ** (degree - 1))
    # print(num)
if num < 0:
    num *= -1
while num:
    summa += num % 10
    num = num // 10
print('Сумма цифр числа =', summa)

# num = float(input())
# n1 = num % 1  # остаток
# n2 = num // 1 # целая чаcть
# sum = 0
# while n1:
#     n3 = int(n1 * 10 // 1)
#     # n4 = n3 // 1
#     sum += n3 #n1 * 10 // 1
#     n1 = n1 * 10 % 1
# print(num % 1)
# print(num // 1)

# num = [12.73, 9.45];
# result = list(map(lambda x: int(str(x).split('.')[1]),num))
# print(result)

# num = input()
# result = num.split('.')
# res1 = int(result[0])
# res2 = int(result[1])
# print(result)
# while res1:
#     # res1= result[0] % 10
#     sum = sum + res1 % 10
#     res1 = res1 // 10
# while result[1]:
#     res1= result[1] % 10
#     sum += res1
#     result[1] = result[1] // 10
# print(sum)