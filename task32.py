import random


def fill_list(list1, n):
    for _ in range(n):
        list1.append(random.randint(0, n // 2))
    # return list1


def single_nums(list1):
    new_list = []
    for i in range(len(list1)):
        flag = True  # число не повторяется
        for j in range(0, i):
            if list1[i] == list1[j]:
                flag = False  # число повторяется
                break
        for j in range(i + 1, len(list1)):
            if list1[i] == list1[j]:
                flag = False  # число повторяется
                break
        if flag:
            new_list.append(list1[i])
    return new_list


def main():
    num = 20   # количество элементов в исходном списке
    my_list = []
    fill_list(my_list, num)
    print(my_list)
    print(single_nums(my_list))


# if __main__ == "__main__":
main()