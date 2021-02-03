from flask import Flask, jsonify, render_template, request
from backend.register import Register
app = Flask(__name__)

@app.route('/login')
def login_user():
    if request.method == 'POST':
        email = request.get_json()['email']
        password = request.get_json()['password']
        register = Register()
        login_status = register.login_user(email, password)
        return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
