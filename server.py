from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return f"""
    <h1>Добро пожаловать на сервер flask-server</h1>
    Ссылка на <a href="{url_for('index')}">index</a> страницу<br>
    """


@app.route('/index')
def index():
    user = {'username': 'dim-akim'}
    return render_template('index.html', **user)  # передаем в шаблон именованный параметр username='dim-akim'


@app.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')


@app.route('/photo-<num>')
def photo(num):
    return render_template(f'photo-{num}.html')


if __name__ == '__main__':
    app.run()
