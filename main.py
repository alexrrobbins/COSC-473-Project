from flask import Flask, render_template, request, redirect, Response, jsonify, session
import secrets
from backend.user import User
app = Flask(__name__)
app.secret_key = secrets.token_bytes()

#######Render Template Paths (View)##############
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('sign-up.html')

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/login')
def login():
    return render_template("login.html")

#########Logical paths (Model)##############
@app.route('/register',methods=['GET','POST'])
def register():
    user_json = request.get_json()
    email = user_json['email']
    password = user_json['password']
    username = user_json['username']
    new_user = User(email, password, username)
    if new_user.add_to_db():
        session['email'] = new_user.get_email()
        session['username'] = new_user.get_username()
        return '200 OK'
    else:
        return redirect(url_for('signup'))

@app.route('/login_verify',methods=['GET','POST'])
def login_verify():
    user_json = request.get_json()
    email = user_json['email']
    password = user_json['password']
    new_user = User(email, password)
    if new_user.verify_credentials():
        session['email'] = new_user.get_email()
        new_user.set_username()
        session['username'] = new_user.get_username()
        return '200 OK'
    else:
        return redirect(url_for('login'))

@app.route('/user_logout',methods=['GET','POST'])
def uder_logout():
    if 'username' in session:
        session.pop('username')
    if 'email' in session:
        session.pop('email')
    return '200 OK'

app.run(debug=True)
