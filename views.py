__author__ = 'trust'
from flask import Flask, request


app = Flask(__name__)

@app.route('/studentlist', methods=['GET', 'POST'])
def welcome():
    return "hello registration"

@app.route('/signup', methods = ['POST'])
def signup():
    firstname = request.form['firstname']
    second_name = request.form['second_name']
    surname = request.form['surname']

    g.db.execute("INSERT INTO email_addresses VALUES (?)", [email])
    g.db.commit()
    return redirect('/')