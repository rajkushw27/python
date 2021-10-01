from logging import DEBUG
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> Hello World </h1>'


@app.route('/python')
def check():
    return "<h1> I love python3 </h1>"


@app.route('/hello/<name>')
def hello(name):
    return f'welcome to the flask development {name.upper()}'


if __name__ == "__main__":
    app.run(debug=True)
