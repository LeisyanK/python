# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
# Пример:
# ABCABCABCDDDFFFFFF --> 1A1B1C1A1B1C1A1B1C3D6F --> -9ABCABCABC3D6F
# 256 символов "А" --> 127A127A2A (256=127+127+2)

# str1 = 'WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
# str2 = '9W3B24W1B14W'

# decompress = 'WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
decompress = ''
compress = '-9ABCABCABC3D6F'
# print(len(compress))
pos = 0
i = 0
# for i in range(len(compress)):
while i < len(compress):
    # print(compress[i])
    if not compress[i].isdigit() and compress[i] != '-':
        # print('число =',compress[pos:i])
        num = int(compress[pos:i])
        #print(num)
        if num < 0:
            decompress += compress[i:i + num * (-1)]
            i += num * (-1)
            pos = i
            # print('i=',i)
        else:
            for j in range(num):
                decompress += compress[i]
            i += 1  #num
            # print('i=',i)
            pos = i
    else:
        i += 1
print(compress, ' --> ', decompress)
