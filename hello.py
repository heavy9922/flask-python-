from flask import Flask, render_template, url_for, request
from markupsafe import escape
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)

# filtros personalizados


@app.add_template_filter
def today(date):
    return date.strftime('%d/%m/%Y')


# app.add_template_filter(today, 'today')
@app.add_template_global
def repeat(s, n):
    return s * n


@app.route('/')
def index():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('code', code='print(''hola)'))
    name = 'yeferson'
    friends = ['paola', 'alex', 'javier']
    date = datetime.now()
    return render_template('index.html', name=name, friends=friends, date=date)


@app.route("/hello")
@app.route("/hello/<name>")
@app.route("/hello/<name>/<int:age>/<email>")
def hello(name=None, age=None, email=None):
    my_data = {
        'name': name,
        'age': age,
        'email': email
    }
    return render_template('hello.html', data=my_data)

# escape de html


@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'

# create with library wtform


class RegisterForm(FlaskForm):
    username = StringField('Nombre de usuario:', validators=[
                        DataRequired(), Length(min=4, max=25)])
    passwd = PasswordField('Password:',validators=[
                        DataRequired(), Length(min=8, max=40)])
    submit = SubmitField('Registar')

# register users


@app.route('/auth/register', methods=['get', 'post'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        passwd = form.passwd.data
        return f'Nombre de usuario {username}, password {passwd}'

    # if request.method == 'POST':
    #     username = request.form['username']
    #     passwd = request.form['passwd']
        # if len(username) >= 4 and len(username) <= 25 and len(passwd) >= 6 and len(passwd) <= 40:
        #     return f'Nombre de usuario {username}, password {passwd}'
        # else:
        #     error = """ El nombre de usuario debe tener entre 4 a 25 caracteres y
        #     la contresenia debe tener entre 6 a 40 caracteres.
        #     """
        #     return render_template('auth/register.html',form = form ,error=error)
    return render_template('auth/register.html', form=form)
