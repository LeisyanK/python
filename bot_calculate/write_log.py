from datetime import datetime

def write_data(text):
    time = datetime.now()
    with open('data.log', 'a', encoding='utf-8') as file:
        file.write(f'{time}: {text}\n')