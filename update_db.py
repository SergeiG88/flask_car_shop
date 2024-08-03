import sqlite3
import json

def update_db():
    # Открытие соединения с базой данных
    conn = sqlite3.connect('car_dealership.db')
    cursor = conn.cursor()

    # Очистка существующих данных в таблице cars
    cursor.execute('DELETE FROM cars')

    # Загрузка данных из файла JSON
    with open('data/cars.json', 'r', encoding='utf-8') as file:
        cars = json.load(file)

    # Вставка новых данных в таблицу cars
    for car in cars:
        cursor.execute('''
            INSERT INTO cars (id, make, model, year, price, description, features, image)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (car['id'], car['make'], car['model'], car['year'], car['price'], car['description'], json.dumps(car['features']), car['image']))

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()

if __name__ == '__main__':
    update_db()
