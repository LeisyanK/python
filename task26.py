def fib_num(n, f):
    # f += '0'
    # f += '1'
    f.append(0)
    f.append(1)
    if n >= 2:
        for i in range(2, n):
            # f[i] = f[i-1] + f[i-2]
            f.append(f[i-1] + f[i-2])
    return f

def nega_fib(n, f):
    f.insert(0, 1)
    f.insert(0, -1)
    if n > 2:
        for _ in range(3, n):
            f.insert(0, f[1] - f[0])
            #f[i] = [f[i+2] - f[i+1]]
    return f


num = int(input('Введите число: '))
f = []
fib_num(num, f)
nega_fib(num, f)
print(f)