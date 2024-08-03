import sqlite3

def get_db_connection():
    conn = sqlite3.connect('car_dealership.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_all_cars():
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM cars').fetchall()
    conn.close()
    return cars

def get_car(car_id):
    conn = get_db_connection()
    car = conn.execute('SELECT * FROM cars WHERE id = ?', (car_id,)).fetchone()
    conn.close()
    return car
