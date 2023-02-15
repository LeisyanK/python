# первоначальный простой вариант
# def calc(text):
#     text = text.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').split()
#     if text[1] == '+':
#         # await update.message.reply_text(int(text[0]) + int(text[2]))
#         return update.message.reply_text(int(text[0]) + int(text[2]))
#     elif text[1] == '-':
#         return update.message.reply_text(int(text[0]) - int(text[2]))
#     elif text[1] == '*':
#         return update.message.reply_text(int(text[0]) * int(text[2]))
#     else:
#         return update.message.reply_text(int(text[0]) / int(text[2]))

import write_log as wl


def calc_first(s):
    if not s:
        s = '12*(10+12)*23/2*((34-2*5)+(56-23))'
    old_list = s.replace('+', ' + ')\
        .replace('-', ' - ')\
        .replace('*', ' * ')\
        .replace('/', ' / ')\
        .replace('(', '( ')\
        .replace(')', ' )')\
        .replace('i', 'j')\
        .split()
    new_list = list()
    for el in old_list:
        if 'j' in el:
            new_list.append(complex(el))
        elif el.isdigit():
            new_list.append(int(el))
        else:
            new_list.append(el)
    # return old_list, new_list
    # print(new_list)
    wl.write_data(f'Разбили выражение на список:\n {new_list}')

    while '(' in new_list:
        first_i = len(new_list) - new_list[::-1].index('(') - 1
        second_i = first_i + new_list[first_i + 1:].index(')') + 1

        new_list = new_list[:first_i] + calc(new_list[first_i + 1:second_i]) + new_list[second_i+1:]
        # print('текущее состояние выражения:', new_list) 
        
    new_list = calc(new_list)   # отправляем выражение на вычисление
    # print(*new_list)
    wl.write_data(f'Вычислили результат: {new_list[0]}\nКонец работы программы.')
    return str(new_list[0])     # возвращаем вычисленный результат в виде строки!!, т.к. бот затем отправляет сообщение пользователю в виде строки!!

def calc(my_list):

    while '*' in my_list or '/' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '*':
                result = my_list.pop(i+1) * my_list.pop(i-1)
                my_list[i-1] = result
                break
            elif my_list[i] == '/':
                result = my_list.pop(i-1) / my_list.pop(i)
                my_list[i-1] = result
                break

    while '+' in my_list or '-' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '-':
                result = my_list.pop(i-1) - my_list.pop(i)
                my_list[i-1] = result
                break
            elif my_list[i] == '+':
                result = my_list.pop(i+1) + my_list.pop(i-1)
                my_list[i-1] = result
                break
    
    return my_list


# print(calc_first('3i+5+2i'))