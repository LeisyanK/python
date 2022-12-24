num = int(input('Введите количество чисел последовательности: '))
sum = 0
dict = {}
for n in range(1, num + 1):
    elem = (1 + 1/n) ** n
    dict[n] = elem
    sum += elem
# print(dict)
print('{', end = '')
for item in dict:
    print(f' {item} : {round(dict[item], 2)}', end = ',')
print(' }')
print(round(sum, 2))