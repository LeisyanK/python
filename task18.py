import random

n = int(input('Введите размерность списка: '))
list1 = list(range(n))   #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)
for i in range(n):  #range(len(list1)):
    poz = random.randrange(n)
    list1[poz], list1[i] = list1[i], list1[poz]
print(list1)