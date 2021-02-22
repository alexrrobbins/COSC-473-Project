from flask import Flask, render_template, request, redirect, Response, jsonify, session, url_for
import secrets
from backend.user import User
from backend.admin import Admin
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
    username = session['username']
    email = session['email']
    if session['admin_status']:
        return render_template("admin.html",
        username=username, email=email)
    else:
        return render_template("welcome.html",
            username=username, email=email)

@app.route('/login')
def login():
    return render_template("login.html")

#########Logical paths (Model) - User functionality##############
@app.route('/register',methods=['GET','POST'])
def register():
    user_json = request.get_json()
    email = user_json['email']
    password = user_json['password']
    username = user_json['username']
    new_user = User(email, password, username)
    if 'admin_status' in session:
        if session['admin_status']:
            new_user.add_to_db()
            return '200 OK'
    if new_user.add_to_db():
        session['email'] = new_user.get_email()
        session['username'] = new_user.get_username()
        session['admin_status'] = new_user.check_admin_status()
        return '200 OK'
    else:
        return redirect('signup')

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
        session['admin_status'] = new_user.check_admin_status()
        return '200 OK'
    else:
        return redirect('login')

@app.route('/user_logout',methods=['GET','POST'])
def uder_logout():
    if 'username' in session:
        session.pop('username')
    if 'email' in session:
        session.pop('email')
    return '200 OK'

#########Logical paths (Model) - Admin functionality##############
@app.route('/remove_user',methods=['GET','POST'])
def remove_user():
    admin = Admin(session['email'],'dummy')
    user_json = request.get_json()
    target_email = user_json['email']
    admin.remove_user_from_db(target_email)
    return '200 OK'

@app.route('/promote_user',methods=['GET','POST'])
def promote_user():
    admin = Admin(session['email'],'dummy')
    user_json = request.get_json()
    target_email = user_json['email']
    admin.promote_to_admin(target_email)
    return '200 OK'

if __name__ == '__main__':
    app.run(debug=True)
