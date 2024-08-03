import json
from flask import Flask, render_template, request, redirect, url_for
from models import get_all_cars, get_car, get_db_connection

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cars')
def car_list():
    cars = get_all_cars()
    car_list = []
    for car in cars:
        car_dict = dict(car)
        car_dict['features'] = json.loads(car_dict['features'])
        car_list.append(car_dict)
    return render_template('car_list.html', cars=car_list)


@app.route('/purchase/<int:car_id>', methods=['GET', 'POST'])
def purchase(car_id):
    car = get_car(car_id)
    car_dict = dict(car)
    car_dict['features'] = json.loads(car_dict['features'])

    if request.method == 'POST':
        # Здесь можно добавить логику для обработки покупки
        return redirect(url_for('car_list'))

    return render_template('purchase.html', car=car_dict)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Здесь можно добавить логику для обработки отправки формы
        return redirect(url_for('index'))
    return render_template('contact.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


if __name__ == '__main__':
    app.run(debug=True)
