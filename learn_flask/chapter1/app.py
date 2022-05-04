encoding = 'UTF-8'
from flask import Flask
import click

app = Flask(__name__)


@app.cli.command()
def hello():
    """注册一个flask命令,Just say hi"""
    click.echo('Hello, Human!')


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/hi')
@app.route("/hello")
def say_hello():
    return "<h1>Hello, Flask!</h1>"


@app.route("/greet", defaults={'name': 'Programmer'})
@app.route("/greet/<name>")
def greet(name):
    return "<h1>Hello, {}! </h1>".format(name)
