# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11
def summa1(num):
    # получаем цифры
    # for el in num:
    #     print(el)
    summa = 0
    for el in num:
        if el.isdigit():
            summa += int(el)
    print('Сумма цифр числа =', summa)
    # return summa

def my_func(func, x):
    # return func(x)
    func(x)

def summa2(list1):
    summa = 0
    for el in list1:
        summa += el
    return summa

num = '12.3'
print('Передача функции аргументом другой функции:')
my_func(summa1, num)
print()

print('Используем List Comprehension:')
my_list = [int(el) for el in num if el.isdigit()]
print(my_list)
print(f'Сумма цифр числа = {summa2(my_list)}')
# print(list(map(summa, num)))

