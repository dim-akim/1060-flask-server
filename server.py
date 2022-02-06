from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/index')
def index():  # возвращаем HTML-код
    return '''
    <html>
      <head>
        <title>Flask Server</title>
      </head>
      <body>
        <h1>Hello, World!</h1>
      </body>
    </html>
    '''


if __name__ == '__main__':
    app.run()
