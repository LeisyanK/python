def simple_nums(num):
    flag = True
    # for i in range(2, num):
    #     if not(num % i):
    #         flag = False
    #         print(f'{num} % {i} => {num % i} {flag}')
    #         break
    #     else:
    #         flag = True
    #         print(f'{num} % {i} => {num % i}')
    # return flag

    i = 2
    while flag and i < num:
        if not (num % i):
            flag = False
            # print(f'{num} % {i} => {num % i} {flag}')
            # break
        # else: # чтоб простись по всему ряду чисел и проверить выполнение условия
        #     flag = True
        #     print(f'{num} % {i} => {num % i} {flag}')
        # print('i =', i)
        i += 1
    return flag


def simple_multiplier(simple_list, num):
    print('Простые множители числа', num, ':')
    for el in simple_list:
        if not(num % el):
            print(el, end=' ')


def main():
    n = int(input('Введите число N: '))
    my_list = []
    if n > 2:
        my_list.append(2)
    for nums in range(3, n, 2):  # шаг = 2, чтобы не рассматривать четные числа
        if simple_nums(nums):
            my_list.append(nums)
            # print(simple_nums(n))
    print('Простые числа в промежутке [1,', n, ']:')
    print(my_list)
    simple_multiplier(my_list, n)



# if __main__ == "__main__":
main()