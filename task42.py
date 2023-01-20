# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
# Пример:
# ABCABCABCDDDFFFFFF --> 1A1B1C1A1B1C1A1B1C3D6F --> -9ABCABCABC3D6F
# 256 символов "А" --> 127A127A2A (256=127+127+2)

# str1 = 'WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
# str2 = '9W3B24W1B14W'

# decompress = 'WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
decompress = 'ABCABCABCDDDFFFFFFABBC'
compress = ''
count = 1
count2 = 0
# for i, el in enumerate(decompress)
for i in range(len(decompress) - 1):
    # print(decompress[i], decompress[i + 1], end='; ')
    if decompress[i] == decompress[i+1]:
        if count2 != 0:
            if count2 == 1:
                #count2 *= count2 * (-1)  #  если только один символ не повторяется, а потом идет повтор другого - то -1 не пишем
                compress += str(count2) + decompress[i-1] # - count2: i]
            else:
                compress += str(count2 * (-1)) + decompress[i-count2 : i]
            count2 = 0
        count += 1
    else:
        if count != 1:
            compress += str(count) + decompress[i]
            count = 1
        else:
            count2 += 1
else:
    if count2 != 0:
        compress += str((count2 + 1) * (-1)) + decompress[len(decompress) - count2 - 1: ]
    else:
        compress += str(count) + decompress[i+1]
print(compress)

# первый вариант: без отрицательных чисел
# decompress = 'ABCABCABCDDDFFFFFF'
# compress = ''
# count = 1
# # for i, el in enumerate(decompress)
# for i in range(len(decompress) - 1):
#     if decompress[i] == decompress[i+1]:
#         count += 1
#     else:
#         compress += str(count) + decompress[i]
#         count = 1
# else:
#     compress += str(count) + decompress[i]
# print(compress)