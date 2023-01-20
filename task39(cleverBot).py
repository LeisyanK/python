# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять
# первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# b) Подумайте как наделить бота "интеллектом"

import random

conf = 20  # всего конфет
step = 5   # макс число конфет при каждом ходе
move = step + 1  # количество конфет за 2 хода (комп + чел)

print(f'ВСЕГО КОНФЕТ: {conf}. МОЖНО ВЗЯТЬ НЕБОЛЬШЕ {step} КОНФЕТ. ИГРА НАЧАЛАСЬ!')
# num = conf + 1
player = random.randint(1, 2)
# print(player)
if player == 2:
    # начинает бот
    num = conf % move
    print(f'Берет компьютер: {num}')
    player = 1
    conf -= num
else:
    # начинает человек
    num = int(input('Возьми конфеты: '))
    while num < 1 or num > step or num > conf:
        if num > conf:
            print(f'Осталось только {conf} конфеты!')
        else:
            print(f'Вы можете взять не более {step} конфет! Осталось конфет: {conf}')
        num = int(input('Возьми конфеты: '))
    conf -= num
    # player = 2
    num = conf % move
    if not num:  # если компьютеру нужно взять 0 конфет по алгоритму
        num = random.randint(1, step)
        print(f'Берет компьютер: {num}')
    else:
        print(f'Берет компьютер: {num}')
    # player = 1
    conf -= num

# print(f'Осталось {conf} конфеты!')

while conf > 0:
    # print(player)
    print('Осталось конфет: ', conf)

    if player == 2:
        # играет бот
        # num = random.randint(1, step)
        num = move - num
        print(f'Берет компьютер: {num}')
        player = 1  # переход хода к игроку
    else:
        num = int(input('Возьми конфеты: '))
        while num < 1 or num > step or num > conf:
            if num > conf:
                print(f'Осталось только {conf} конфеты!')
            else:
                print(f'Вы можете взять не более {step} конфет! Осталось конфет: {conf}')
            num = int(input('Возьми конфеты: '))
        player = 2  # переход хода к боту
    conf -= num

if player == 2:
    print('Ты победил!')
else:
    print('Победил компьютер!')