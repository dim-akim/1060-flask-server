from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return """
    <h1>Добро пожаловать на сервер flask-server</h1>
    Ссылка на <a href="index">index</a> страницу<br>
    """


@app.route('/index')
def index():
    user = {'username': 'dim-akim'}
    return render_template('index.html', **user)  # передаем в шаблон именованный параметр username='dim-akim'


if __name__ == '__main__':
    app.run()
