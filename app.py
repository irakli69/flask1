from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'lecture14'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    gender = db.Column(db.Float, nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __str__(self):
        return f'first_name:{self.first_name}; last_name: {self.last_name}; sex: {self.sex}; email: {self.email}; password: {self.password}'


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        email = request.form['email']
        password = request.form['password']
        b1 = user(firs_name=first_name, last_name=last_name, gender=gender, email=email, password=password)
        db.session.add(b1)
        db.session.commit()
        return render_template('login.html')
    return render_template('login.html')


@app.route('/main')
def home():
    return render_template('index.html')


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/admin')
def admin():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)




















