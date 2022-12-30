def main():
    import math
    # pi = 3.1415926535897
    d = input('Введите точность числа Пи: ')
    # acc = len(d[d.find('.') + 1:])
    acc = len(d) - 2
    # print(len(d))
    # print(len(d[d.find('.') + 1:]))
    # print(acc)
    print(round(math.pi, acc))

    # второй способ
    num = input('Введите вещественное число: ')
    d = input('Введите точность: ')
    print(num[: num.find('.') + len(d) - 1])


# if __name__ == "__name__":
main()