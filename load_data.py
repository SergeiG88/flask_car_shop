import sqlite3
import json

def load_data():
    # Подключение к базе данных
    conn = sqlite3.connect('car_dealership.db')
    cursor = conn.cursor()

    # Создание таблицы, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            price INTEGER NOT NULL,
            description TEXT,
            features TEXT,
            image TEXT
        )
    ''')

    # Загрузка данных из JSON файла с правильной кодировкой
    with open('data/cars.json', encoding='utf-8') as f:
        cars = json.load(f)

    # Вставка данных в таблицу
    for car in cars:
        cursor.execute('''
            INSERT OR REPLACE INTO cars (id, make, model, year, price, description, features, image)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (car['id'], car['make'], car['model'], car['year'], car['price'],
              car['description'], json.dumps(car['features']), car['image']))

    # Сохранение изменений и закрытие подключения
    conn.commit()
    conn.close()

if __name__ == '__main__':
    load_data()
