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


def calc_first(s=''):
    if not s:
        s = '12*(10+12)*23/2*((34-2*5)+(56-23))'
    old_list = s.replace('+', ' + ')\
        .replace('-', ' - ')\
        .replace('*', ' * ')\
        .replace('/', ' / ')\
        .replace('(', '( ')\
        .replace(')', ' )').split()
    old_list = [int(elem) if elem.isdigit() else elem for elem in old_list]
    # print(old_list)   
    # print('перевернутый список', old_list[::-1])

    while '(' in old_list:
        first_i = len(old_list) - old_list[::-1].index('(') - 1
        second_i = first_i + old_list[first_i + 1:].index(')') + 1

        old_list = old_list[:first_i] + calc(old_list[first_i + 1:second_i]) + old_list[second_i+1:]
        # print('текущее состояние выражения:', old_list) 
        
    old_list = calc(old_list)
    # print(*old_list)
    return old_list


# main()