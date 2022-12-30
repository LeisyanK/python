import random


def new_polynom(n):
    polynom = ''
    for degree in range(n, 1, -1):
        k = random.randint(0, 100)
        if k:
            polynom += str(k) + '*x^' + str(degree) + ' + '
    k = random.randint(0, 100)  # первая степень
    if k:
        polynom += str(k) + '*x'
    k = random.randint(0, 100)  # нулевая степень
    if k:
        polynom += ' + ' + str(k)
    polynom += ' = 0'
    # print(polynom)
    return polynom


def write_in_file(polynom):
    new_file = open('file_polynom.txt', 'a')
    new_file.write(polynom + '\n')
    new_file.close()


num = int(input('Введите натуральную степень: '))
# pol = new_polynom(num)
# print(pol)
write_in_file(new_polynom(num))

