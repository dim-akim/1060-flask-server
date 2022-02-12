from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return """
    <h1>Добро пожаловать на сервер flask-server</h1>
    Ссылка на <a href="index">index</a> страницу<br>
    """


@app.route('/index')
def index():  # возвращаем отображение шаблона
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
