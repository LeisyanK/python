1	day = int(input('Введите номер дня недели: '))
2	if day == 6 or day == 7:
3	    print('выходной')
4	elif day > 0 and day < 6:
5	    print('Будний день')
6	else:
7	    print('Вы ввели некорректное число')