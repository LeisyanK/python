import telebot
from telebot import types
from datetime import datetime
import calc

worker_list = {}
worker = []
chat_id =''

bot = telebot.TeleBot('6277873420:AAFnQMKtaWc1umP6iYujHazyghtl_id54J4')

@bot.message_handler(commands=['start'])    # фильтр хэндлера: commands
def send_welcome(message):
    global chat_id
    chat_id = message.chat.id
    bot.reply_to(message, """\
Привет, {message.from_user.first_name}!
Отправьте одну из команд:
/start - запуск приложения
/help - помощь
/calc - запустить калькулятор для вычисления выражения
/workers - работа с базой данных сотрудников
\
""")
    log_data('Запуск приложения.')

@bot.message_handler(commands=['help'])    # фильтр хэндлера: commands
def send_welcome(message):
    bot.reply_to(message, """\
Функции приложения:
/start - запуск приложения
/help - вызов помощи по работе в приложении
/calc - чтобы посчитать математическое выражение, наберите команду /calc, затем отправьте боту выражение
/workers - возможность добавлять, удалять сотрудников, распечатать список сотрудников, импортировать и экспортировать список сотрудников
\
""")
    log_data('Пользоатель запросил вывод справки.')

@bot.message_handler(commands=['calc'])    # фильтр хэндлера: commands
def calculator(message):
    bot.reply_to(message, 'Введите математическое выражение')
    log_data('Пользователь выбрал калькулятор.')
    bot.register_next_step_handler(message, calc1)
    

def calc1(message):
    result = calc.calc_first(message.text)
    answer = message.text + ' = ' + str(result[0])
    log_data(f'Пользователь ввел выражение: {message.text}. Результат равен {result[0]}.')
    bot.reply_to(message, answer)

@bot.message_handler(commands=['workers'])    # фильтр хэндлера: commands
def workers(message):
    global chat_id
    chat_id = message.chat.id
    bot.reply_to(message, """\
Выберите действие:
/new_worker  - добавить сотрудника
/print_workers - распечатать список сотрудников
/delete_workers - удалить сотрудника
/import_workers - импортировать список сотрудников из файла
/export_workers - экспортировать список сотрудников в файл
\
""")
    log_data('Пользователь выбрал работу с базой данных.')
    global worker_list
    worker_list = {'1':['Петров', 'Иван', 'Игоревич', '01.05.2000', '8-928-123-45-67', 'IT'], 
                   '2':['Федоров', 'Павел', 'Иванович', '21.12.2002', '8-929-963-52-87', 'Counting']}

@bot.message_handler(commands=['new_worker'])    # фильтр хэндлера: commands
def new_worker(message):
    surname = bot.reply_to(message, 'Введите фамилию сотрудника')
    log_data('Ввод нового сотрудника. Начало.')
    bot.register_next_step_handler(surname, new_name)

def new_name(message):  # получили фамилию
    global worker
    worker.append(message.text)
    name = bot.reply_to(message, 'Введите имя сотрудника')
    log_data(f'Пользователь ввел фамилию: {message.text}')
    bot.register_next_step_handler(name, new_middle_name)
    
def new_middle_name(message): # получили имя
    global worker
    worker.append(message.text)
    log_data(f'Пользователь ввел имя: {message.text}')
    middle_name = bot.reply_to(message, 'Введите отчество сотрудника')
    bot.register_next_step_handler(middle_name, birth_date)

def birth_date(message): # получили отчество
    global worker
    worker.append(message.text)
    log_data(f'Пользователь ввел отчество: {message.text}')
    birthDay = bot.reply_to(message, 'Введите дату рождения сотрудника')
    bot.register_next_step_handler(birthDay, phone)

def phone(message): # получили дату рождения
    global worker
    worker.append(message.text)
    log_data(f'Пользователь ввел дату рождения: {message.text}')
    tel = bot.reply_to(message, 'Введите номер телефона сотрудника')
    bot.register_next_step_handler(tel, work_place)

def work_place(message): # получили номер телефона сотрудника
    global worker
    worker.append(message.text)
    log_data(f'Пользователь ввел номер телефона: {message.text}')
    dep = bot.reply_to(message, 'Введите отдел сотрудника')
    bot.register_next_step_handler(dep, worker_data)

def worker_data(message): # получили отдел сотрудника
    global worker
    worker.append(message.text)
    log_data(f'Пользователь ввел отдел: {message.text}')
    global worker_list
    worker_list[str(len(worker_list) + 1)] = worker
    log_data(f'Внесли данные нового сотрудника в базу данных: {worker}')
    bot.send_message(message.chat.id, print_data(worker_list))
    log_data(f'Вывели список сотрудников на экран: {worker_list}')

def print_data(data):
    mess = ''
    for key in data:
        mess += f'{key}. '
        mess += ' '.join(data[key])  #.values())
        mess += '\n'
    return mess
    

@bot.message_handler(commands=['print_workers'])    # фильтр хэндлера: commands
def print_workers(message):
    global worker_list
    log_data(f'Пользователь запросил вывод списка сотрудников на экран.')
    bot.send_message(message.chat.id, print_data(worker_list))

@bot.message_handler(commands=['delete_workers'])    # фильтр хэндлера: commands
def delete_workers(message):
    global worker_list
    bot.send_message(message.chat.id, print_data(worker_list))
    log_data(f'Пользователь запросил удаление данных сотрудника.')
    number = bot.send_message(message.chat.id, 'Введите номер сотрудника, которого нужно удалить')
    bot.register_next_step_handler(number, del_worker)

def del_worker(message):
    global worker_list
    log_data(f'Номер сотрудника: {message.text}')
    del worker_list[message.text]
    bot.send_message(message.chat.id, 'Сотрудник удален')

@bot.message_handler(commands=['import_workers'])    # фильтр хэндлера: commands
def import_workers(message):
    file = bot.send_message(message.chat.id, 'Отправьте файл для импорта')
    log_data(f'Пользователь выбрал импорт документа.')
    bot.register_next_step_handler(file, import_db)

def import_db(message):
    global chat_id

    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    src = 'G:/GEEK_BRAINS/Quarter2/python/seminar9_hw/' + message.document.file_name
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    import_data(src)
    log_data('Импорт данных завершен.')
    bot.reply_to(message, "Импорт данных завершен")

def import_data(src):
    flag = True
    with open(src, 'r', encoding='utf-8') as file:
        while flag:
            record = file.readline()
            if not record:
                flag = False
            else:
                record = record.split(';')
                record[-1] = record[-1].replace('\n', '')
                global worker_list
                worker_list[len(worker_list)+1] = record


@bot.message_handler(commands=['export_workers'])    # фильтр хэндлера: commands
def export_workers(message):
    # сохраняем данные в файл и отправляем его
    log_data('Пользователь запросил экспорт данных.')
    global worker_list
    mess = ''
    for key in worker_list:
        mess += ';'.join(worker_list[key])  #.values())
        mess += '\n'
    with open('export.txt', 'w', encoding='utf-8') as file:
        file.write(mess)
    bot.send_document(message.chat.id, open(r'G:/GEEK_BRAINS/Quarter2/python/seminar9_hw/export.txt', 'rb'))
    log_data('Экспорт файла завершен.')

def log_data(message):
    time = datetime.now()
    with open('data.log', 'a', encoding='utf-8') as file:
        file.write(f'{time}: {message}\n')

bot.infinity_polling()