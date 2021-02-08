from flask import Flask, render_template, request, redirect, Response, jsonify
from backend.user import User
app = Flask(__name__)

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
    new_user.add_to_db()
    return '200 OK'

@app.route('/login_verify',methods=['GET','POST'])
def login_verify():
    user_json = request.get_json()
    email = user_json['email']
    password = user_json['password']
    new_user = User(email, password)
    new_user.verify_credentials()
    return '200 OK'

app.run(debug=True)
