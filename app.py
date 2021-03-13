from flask import Flask, render_template

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

@app.route('/auth')
def authPage():
    return render_template('auth.html')

if __name__ == "__main__":
    app.run(debug=True)
