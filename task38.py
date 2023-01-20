# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".
text = 'пра прАБВ огнр длорпАБВовгв зщзыфшвщ вфыыАБВгыоы АБВывовдлыф'
def delword(text:str):
    if 'абв' in text.lower():
        text = text.replace(text, '')
    return text

#text = list(map(delword, text.split()))  # тоже работает
text = list(filter(delword, text.split()))
print(text)

print('The second variant')
text = 'пра прАБВ огнр длорпАБВовгв зщзыфшвщ вфыыАБВгыоы АБВывовдлыф'

text = list(filter(lambda el: 'абв' not in el.lower(), text.split()))
print(' '.join(text))

print('The third variant')
my_list = 'пра прАБВ огнр длорпАБВовгв зщзыфшвщ вфыыАБВгыоы АБВывовдлыф'.split()
#my_list = list(map(lambda x: 'АБВ' in x, my_list))  # map берет каждый элемент и проверяет условие для него
my_list = list(filter(lambda x: not 'АБВ' in x, my_list))
print(my_list)