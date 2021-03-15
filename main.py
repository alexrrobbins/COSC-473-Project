# main.py - the main Flask application
# Written by Alex Robbins, Niko Nuzzo, Gavin Homan
from flask import Flask, render_template, request, redirect, Response, jsonify, session, url_for
import secrets
from backend.user import User
from backend.admin import Admin
from backend.schedule import Schedule
from backend.email_password_reset import EmailPwdReset
app = Flask(__name__)
app.secret_key = secrets.token_bytes()

#######Render Template Paths (View)##############

# Render default page index when site is loaded
@app.route('/')
def index():
    return render_template('index.html')

# Render sign-up page when sign-up button is clicked
# or when admin add user button is clicked
@app.route('/signup')
def signup():
    return render_template('sign-up.html')

# Render the landing page - 2 different views:
# If user is admin, render admin view
# else render default user view
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

# Render login page when login button is clicked
@app.route('/login')
def login():
    return render_template("login.html")

# Render schedule actions page when Schedule Actions is clicked
@app.route('/schedule-actions')
def scheduleactions():
    return render_template('schedule-actions.html')

# Render schedule page
# Note: We need a different view for the guest without the buttons
# if we keep the buttons on that page or move them to the actions.
@app.route('/schedule')
def schedule():
    schedule_id = str(session['schedule_id'])
    passcode = session['passcode']
    owner = session['email']
    if 'username' in session:
        return render_template('schedule_buttons.html',schedule_id=schedule_id,
            passcode=passcode, owner=owner)
    else:
        return render_template('schedule.html',schedule_id=schedule_id,
            passcode=passcode, owner=owner)

@app.route('/schedule-id-passcode')
def schedule_id_passcode():
    return render_template("passcode.html")

@app.route('/change-password')
def change_password():
    return render_template("change-password.html")

#########Logical paths (Model) - User functionality##############

# Register the user - get the required field data from the html fields
# through ajax from JavaScript file app.js.
# Pass this field data to the backend:
# if registeration is successful, store user data in cookie and go to landing page
# if unsuccessful, redirect to signup page
# If done by admin, add user to database and return to admin view
@app.route('/register',methods=['GET','POST'])
def register():
    user_json = request.get_json()
    email = user_json['email']
    password = user_json['password']
    username = user_json['username']
    new_user = User(email, password, username)
    if 'admin_status' in session:
        if session['admin_status']:
            admin = Admin(session['email'],'dummy')
            admin.admin_add_user_to_db(new_user,session['email'])
            return '200 OK'
    if new_user.add_to_db():
        session['email'] = new_user.get_email()
        session['username'] = new_user.get_username()
        session['admin_status'] = new_user.check_admin_status()
        return '200 OK'
    else:
        return redirect('signup')

# Verify the login data of the user - get the required data from the html fields
# through ajax from JavaScript file app.js.
# Pass this field data to the backend:
# If login successful, store user data in cookie and go to landing page
# if unsuccessful, redirect to login page.
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

# When logout button is clicked, remove user data from cookie and return to index
@app.route('/user_logout',methods=['GET','POST'])
def uder_logout():
    if 'username' in session:
        session.pop('username')
    if 'email' in session:
        session.pop('email')
    if 'admin_status' in session:
        session.pop('admin_status')
    return '200 OK'

#########Logical paths (Model) - Admin functionality##############

# Remove the user from database by using an email (the key)
@app.route('/remove_user',methods=['GET','POST'])
def remove_user():
    admin = Admin(session['email'],'dummy') # 'dummy' is used in pwd field bc user class requires it
    user_json = request.get_json()
    target_email = user_json['email']
    admin.remove_user_from_db(target_email)
    return '200 OK'

# Promote a user that is in the database using an email (the key)
@app.route('/promote_user',methods=['GET','POST'])
def promote_user():
    admin = Admin(session['email'],'dummy')
    user_json = request.get_json()
    target_email = user_json['email']
    admin.promote_to_admin(target_email)
    return '200 OK'

#########Logical paths (Model) - Schedule functionality##############
@app.route('/create_new_schedule',methods=['GET','POST'])
def create_new_schedule():
    new_schedule = Schedule(session['email'])
    session["schedule_id"] = new_schedule.get_id()
    session["passcode"] = new_schedule.get_passcode()
    new_schedule.add_to_db()
    return '200 OK'

@app.route('/delete_schedule',methods=['GET','POST'])
def delete_schedule():
    schedule_to_delete = Schedule(session['email'], session['schedule_id'])
    schedule_to_delete.delete_from_db()
    return '200 OK'

@app.route('/retrieve_schedule',methods=['GET','POST'])
def retrieve_schedule():
    schedule_json = request.get_json()
    schedule_id = schedule_json['schedule_id']
    passcode = schedule_json['passcode']
    schedule_to_get = Schedule(email='null',schedule_id=schedule_id,passcode=passcode)
    if schedule_to_get.retrieve_schedule():
        session['email'] = schedule_to_get.get_owner()
        session['schedule_id'] = schedule_to_get.get_static_id()
        session['passcode'] = "CENSORED"
    return '200 OK'

#########Logical paths (Model) - Email functionality##############

# When forgot password button is clicked, send the user a reset email
@app.route('/email_change_password_request',methods=['GET','POST'])
def email_change_password_request():
    user_json = request.get_json()
    email = user_json['email']
    e = EmailPwdReset(email)
    e.send_pwd_reset_message()
    return '200 OK'

if __name__ == '__main__':
    app.run(debug=True)
