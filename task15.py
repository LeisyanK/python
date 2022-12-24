num = int(input('Введите число: '))
list1 = [1]
proizv = 1
for el in range(2, num + 1):
    proizv *= el
    list1.append(proizv)
print(list1)