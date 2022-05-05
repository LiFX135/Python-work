from flask import Flask, render_template, redirect, url_for, Markup, flash
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", 'secret string')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)


# 注册模板上下文处理函数
@app.context_processor
def inject_foo():
    foo = 'i am foo'
    return dict(foo=foo)


# 此函数的参数可以自定义全局函数名称
@app.template_global()
def bar():
    return "I'm a bar."


# 注册了一个自定义过滤器， 用markup标记 音符 为安全字符
@app.template_filter()
def musical(s):
    return s + Markup(' &#9835')    # 即在输入字符后加个音符符号


# 自定义测试器
@app.template_test()
def baz(n):
    if n == 'baz':
        return True
    return False


@app.route('/watchlist2')
def watchlist2():
    return render_template('watchlist2.html', user=user, movies=movies)


@app.route('/flash')
def just_flash():
    flash("I'm flash, who is looking for me?")
    return redirect(url_for('index'))

user = {
    'username': 'FireSniper',
    'bio': 'A boy who loves Sci-Fi.',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]