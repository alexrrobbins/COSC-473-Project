from flask import Flask, render_template, request, redirect, Response, jsonify
from backend.user import User
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome',methods=['GET','POST'])
def welcome():
    user_json = request.get_json()
    email = user_json['email']
    password = user_json['password']
    username = user_json['username']
    new_user = User(email, password, username)
    new_user.add_to_db()
    return render_template("welcome.html",
            email=email,username=username)

app.run(debug=True)
