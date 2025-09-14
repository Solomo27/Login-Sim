from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login_validation', methods=["POST"])
def login_validation():
    email  = request.form.get('email')
    password  = request.form.get('password')

    conn = sqlite3.connect('LoginData.db')
    cursor = conn.cursor()

    user = cursor.execute("SELECT * FROM Users WHERE email=? AND password=?", (email, password)).fetchall()
    conn.close()
    if len(user) > 0:
        return redirect(f'/home?fname={user[0][1]}&lname={user[0][2]}&email={user[0][3]}')
    else: 
        return redirect('/')
@app.route('/home')
def home():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    email = request.args.get('email')

    return render_template('home.html', fname=fname, lname=lname, email=email)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/add_user', methods=["POST"])
def add_user():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')
    
    conn = sqlite3.connect('LoginData.db')
    cursor = conn.cursor()

    ans = cursor.execute("SELECT * FROM Users WHERE email=? AND password=?", (email, password)).fetchall()
    
    if len(ans) > 0:
        conn.close()
        return render_template('login.html')
    else:
        cursor.execute("INSERT INTO Users(first_name, last_name, email, password) VALUES (?,?,?,?)", (fname,lname,email,password))
        conn.commit()
        conn.close()
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)