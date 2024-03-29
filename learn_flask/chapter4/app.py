from flask import Flask, render_template
from forms import LoginForm

app = Flask(__name__)
app.secret_key = 'secret string'


@app.route('/basic')
def basic():
    form = LoginForm()
    return render_template('basic.html', form=form)
