from flask import Flask, render_template, redirect
from loginform import LoginForm
from registerform import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwekwqkJDHASIqwop'

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/task')
def task():
    return render_template('task.html')

@app.route('/auth', methods=['GET', 'POST'])
def authPage():
    form = LoginForm()
    label = ['Авторизация', 'Вы тут впервые?', '/register', 'Зарегистрируйтесь']
    if form.validate_on_submit():
        return redirect('/')
    return render_template('auth.html', form=form, label=label)

@app.route('/register', methods=['GET', 'POST'])
def registerPage():
    form = RegisterForm()
    label = ['Регистрация', 'Уже есть аккаунт?', '/auth', 'Авторизуйтесь']
    if form.validate_on_submit():
        return redirect('/')
    return render_template('auth.html', form=form, label=label)

if __name__ == "__main__":
    app.run(debug=True)
