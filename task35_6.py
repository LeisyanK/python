def polynom_koef(str1):
    i = 0
    d = {}
    deg = 0
    koef = 0

    # определяем высшую степень многочлена
    max_pow = str1.find('^')+1
    # print(max_pow)
    k = str1.find('^')+1
    while str1[k].isdigit():
        k+=1
    max_pow = int(str1[max_pow:k])
    # print('k=',k)
    # print(max_pow)
    # print()

    while i < len(str1) - 2:
        temp_str = ''
        temp = i
        while str1[i] != '*' and str1[i] != '+' and str1[i] != '-' and str1[i] != '=':
            temp_str += str1[i]
            i += 1
        if 'x' in temp_str:
            if 'x^' in temp_str:   # temp_str[:2] == 'x^':
                deg = int(temp_str[2:])    # len(temp_str)-1])
            else:   # temp_str[0] == 'x':
                deg = 1   # temp_str[2:]''  # len(temp_str)-1])
            d[deg] = koef
        elif str1[i] == '=' and not('x' in temp_str):
            koef = int(temp_str)
            deg = 0
            d[deg] = koef
        else:
            if str1[temp-1] == '-':
                koef = int('-' + temp_str)  # число умножаем на -1
            elif temp_str != '':
                koef = int(temp_str)
        i += 1
    for j in range(max_pow, -1, -1):
        if not(j in d.keys()):
            # print(j)
            d[j] = 0
    return d, max_pow


def from_file(path):
    data = open(path, 'r')
    str1 = data.read()
    data.close()
    return str1


def polynom_summa(dict1, dict2, pow1, pow2):
    d3 = {}
    pow3 = 0
    if pow1 > pow2:
        pow3 = pow1
        for i in range(pow1, pow2, -1):
            d3[i] = dict1[i]
            # print(f'd1[{i}]=',dict1[i])
        for i in range(pow2, -1 , -1):
            d3[i] = dict1[i] + dict2[i]
    else:
        pow3 = pow2
        for i in range(pow2, pow1, -1):
            d3[i] = dict2[i]
            # print(f'd2[{i}]=',dict2[i])
        for i in range(pow1, -1 , -1):
            d3[i] = dict1[i] + dict2[i]
    print(d3)
    return d3, pow3


def make_polynom(dict3, pow3):
    str3 = ''
    for i in range(pow3, 1, -1):
        if dict3[i] != 0:
            if dict3[i] > 0 and i != pow3:
                str3 += '+' + str(dict3[i]) + '*x^' + str(i)
            else:
                str3 += str(dict3[i]) + '*x^' + str(i)
    if 1 in dict3.keys():
        if dict3[1] > 0 and 1 != pow3:
            str3 += '+' + str(dict3[1]) + '*x'
        else:
            str3 += str(dict3[1]) + '*x'
    if 0 in dict3.keys():
        if dict3[0] > 0 and 0 != pow3:
            str3 += '+' + str(dict3[0])
        else:
            str3 += str(dict3[0])
    str3 += '=0'
    print(str3)
    data = open('file3.txt', 'w')
    data.writelines(str3)
    data.close()


str1 = from_file('file1.txt')
str2 = from_file('file2.txt')
d1, pow1 = polynom_koef(str1)
d2, pow2 = polynom_koef(str2)
# str3 = '-15*x^4-41*x^3+75*x-8=0'
# d3, pow3 = polynom_koef(str3)
# print(str3)
print(str1)
print(d1)
# print(pow1)
print(str2)
print(d2)
# print(pow2)

d3, pow3 = polynom_summa(d1, d2, pow1, pow2)
make_polynom(d3, pow3)