from flask import Flask, request, url_for, redirect, abort, make_response, jsonify, session
import os
# request 是flask中的请求对象，封装了从客户端发送的请求报文

app = Flask(__name__)
# 读取环境变量中的密钥
app.secret_key = os.getenv('SECRET_KEY', 'SECRET STRING')

@app.route('/')
@app.route('/hello', methods=['GET', 'POST'])  # methods参数用于设置监听方法
def hello():
    name = request.args.get('name')  # 获取查询参数name的值
    if name is None:
        name = request.cookies.get('name', 'Human')  # 通过cookie来获取用户名
        response = '<h1>Hello, %s</h1>' % name
    if 'logged_in' in session:  # 读取session中的内容，根据状态返回不同内容
        response += '[Authenticated]'
    else:
        response += '[Not Authenticated]'
    return response


@app.route('/goback/<int:year>')  # int是变量类型的转换器
def go_back(year):
    return 'Welcome back to the {}'.format(2022 - year)


colors = ['blue', 'white', 'red']


@app.route('/color/<any(%s):color>' % str(colors)[1:-1])
def three_colors(color):
    return '<p>Love is patient and kind. Love is not jealous or boastful or proud or rude.</p>'


@app.route('/')
def default():
    # return "", 301, {'Location': url_for("hello", _external=True)} or
    return redirect(url_for("hello"), 301)


@app.route('/404')
def not_found():
    abort(418)

# return response with different formats
@app.route('/note', defaults={'content_type': 'text'})
@app.route('/note/<content_type>')
def note(content_type):
    content_type = content_type.lower()
    if content_type == 'text':
        body = '''Note
to: Peter
from: Jane
heading: Reminder
body: Don't forget the party!
'''
        response = make_response(body)
        response.mimetype = 'text/plain'
    elif content_type == 'html':
        body = '''<!DOCTYPE html>
<html>
<head></head>
<body>
  <h1>Note</h1>
  <p>to: Peter</p>
  <p>from: Jane</p>
  <p>heading: Reminder</p>
  <p>body: <strong>Don't forget the party!</strong></p>
</body>
</html>
'''
        response = make_response(body)
        response.mimetype = 'text/html'
    elif content_type == 'xml':
        body = '''<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Peter</to>
  <from>Jane</from>
  <heading>Reminder</heading>
  <body>Don't forget the party!</body>
</note>
'''
        response = make_response(body)
        response.mimetype = 'application/xml'
    elif content_type == 'json':
        body = {"note": {
            "to": "Peter",
            "from": "Jane",
            "heading": "Reminder",
            "body": "Don't forget the party!"
        }
        }
        response = jsonify(body)
        # equal to:
        # response = make_response(json.dumps(body))
        # response.mimetype = "application/json"
    else:
        abort(400)
    return response


@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)   # 在响应中包含cookie  cookie中包含明文很危险
    return response

# 登录，给session中加一个认证
@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('hello'))

# 要去掉认证，pop即可
@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))


@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403)
    return 'Welcome back administrator!'


