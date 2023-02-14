# рабочая версия без lambda, filter и т.д.
import random
import emoji

def field(my_list):
    print('   | X1 | X2 | X3 |')
    print('-------------------')
    for i in 0, 1, 2:
        print(f'Y{i + 1} |', end='')
        for j in 0, 1, 2:
            print(f' {my_list[i][j]} |', end='')  # {my_list[0][1]} | {my_list[0][2]} |')
            # print(f' {i,j} |', end='')
        print()
        print('-------------------')


def answer(label):
    print()
    print(emoji.emojize(':1st_place_medal:', language='alias'), f'ВЫИГРАЛИ {label}', emoji.emojize(':red_exclamation_mark:', language='alias'))
    return False


def check(label, my_list):
    for i in 0, 1, 2:
        if my_list[0][i] == label and my_list[1][i] == label and my_list[2][i] == label:
            # print(f'Выиграли {label}!')
            # return False
            return answer(label)
        elif my_list[i][0] == label and my_list[i][1] == label and my_list[i][2] == label:
            # print(f'Выиграли {label}!')
            # return False
            return answer(label)
    else:
        if my_list[0][0] == label and my_list[1][1] == label and my_list[2][2] == label:
            # print(f'Выиграли {label}!')
            # return False
            return answer(label)
        elif my_list[2][0] == label and my_list[1][1] == label and my_list[0][2] == label:
            # print(f'Выиграли {label}!')
            # return False
            return answer(label)
        else:
            return True


# play = [[' 1',' 2',' 3'],[' 4',' 5',' 6'],[' 7',' 8',' 9']]
play = [['  ', '  ', '  '], ['  ', '  ', '  '], ['  ', '  ', '  ']]
field(play)

player = random.randint(1, 2)
counter = 0
flag = True
while flag:  # flag = True - никто не выиграл
    # print(player)
    if player == 2:
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        # print('Ход Бота:', end=' ')  # можно посмотреть все попытки Бота
        # print(x, y)
        if play[y-1][x-1] == '  ':
            print(f'Ход Бота: x = {x}, y = {y}')
            # play[y-1][x-1] = '0'
            play[y-1][x-1] = emoji.emojize(':hollow_red_circle:', language='alias')
            field(play)
            # flag = check('0', play)
            flag = check(emoji.emojize(':hollow_red_circle:', language='alias'), play)
            counter += 1
            player = 1
            # field(play)
    else:
        print('Твой ход:')
        x = int(input('Введите х: '))
        while 1 > x or x > 3:
            x = int(input('Введите верное значение х: '))
        y = int(input('Введите y: '))
        while 1 > y or y > 3:
            y = int(input('Введите верное значение y: '))
        # player = 2
        if play[y-1][x-1] != '  ':
            print('Поле уже занято')
        else:
            # play[y-1][x-1] = 'x'
            play[y-1][x-1] = emoji.emojize(':cross_mark:', language='alias')    # ':x:'
            field(play)
            # flag = check('x', play)
            # flag = check(':cross_mark:', play)
            flag = check(emoji.emojize(':cross_mark:', language='alias'), play)
            counter += 1
            player = 2
            # field(play)
    # field(play)
    if counter == 9 and flag:
    # if not(' ' in play):
        print('ХОДОВ НЕ ОСТАЛОСЬ!')
        flag = False


