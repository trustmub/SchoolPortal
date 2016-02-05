
from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
#import sqlite3
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from form import LoginForm
#from models import User, bcrypt


app = Flask(__name__)

bcrypt = Bcrypt(app)

#config
import os
app.config.from_object('config.DevelopmentConfig')

# create the sqlalchemy object

db = SQLAlchemy(app)
from models import *

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You Need To Login First.')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    usrname = User.name
    return render_template('dashboard.html', posts=posts)

@app.route('/welcome', methods=['GET', 'POST'])
@login_required
def welcome():
    return render_template("dashboard.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
                session['logged_in'] = True
                flash('You where logged in!')
                return redirect(url_for('home'))
        else:
             error = 'Invalid credentials. please log again.'

    return render_template('login.html', form=form, error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You where logged out!')
    return redirect(url_for('welcome'))
#
# def connect_db():
#      return sqlite3.connect(app.database)

@app.route('/register/', methods=['GET', 'POST'])   # pragma: no cover
@login_required
def register():
    return render_template('regform.html')


@app.route('/addrecord',methods = ['POST', 'GET'])
def addrecord():

   if request.method == 'POST':
         firstname = request.form['firstname']
         second_name = request.form['second_name']
         surname = request.form['surname']
         gender = request.form['gender']
         email = request.form['email']
         address1 = request.form['address1']
         address2 = request.form['address2']
         telephone = request.form['telephone']
         cell_number = request.form['cell_number']
         dob = request.form['dob']
         identification_number = request.form['identification_number']
         passport_number = request.form['passport_number']
         marital_status = request.form['marital_status']
         full_spouse_name = request.form['full_spouse_name']
         # tracking = request.form['tracking']
         tracking = os.urandom(12)
         rank = request.form['rank']


         stud = Students(firstname,second_name,surname,gender,email,address1,address2,telephone,
                cell_number,dob,identification_number,passport_number,marital_status,full_spouse_name,tracking,rank)
         db.session.add(stud)
         db.session.commit()
   return render_template("dashboard.html")


@app.route('/databaselist', methods=['POST','GET'])
@login_required
def databaselist():
    student =  db.session.query(Students).all()
    return render_template('result.html', student = student)


@app.route('/signup', methods=['POST', 'GET'])
@login_required
def signup():
    return render_template('signup.html')






if __name__ == '__main__':
    app.run()
