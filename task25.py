def num_in_bin(n):
    binary = ''
    while n:
        a = n % 2
        # print(a, end=' ')
        n //= 2
        # print(n)
        binary = str(a) + binary
    return binary


num = int(input('Введите число: '))
print('Число в двоичной системе счисления =', num_in_bin(num))
