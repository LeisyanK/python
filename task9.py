num = int(input('Введите номер четверти: '))
if num == 1:
    print('0 < x < +oo, 0 < y < +oo')
elif num == 2:
    print('-oo < x < 0, 0 < y < +oo')
elif num == 3:
    print('-oo < x < 0, -oo < y < 0')
elif num == 4:
    print('0 < x < +oo, -oo < y < 0')
else:
    print('нет такой четверти')