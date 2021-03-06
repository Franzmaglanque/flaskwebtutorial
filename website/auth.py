from xmlrpc.client import boolean
from flask import Blueprint,render_template, request, flash
from .models import User
# from wekzeug.security import generate_password_hash, check_password_hash



auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    
    return render_template("login.html",boolean=False)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash("Email must be greater than 4 characters", category="error")
        elif len(firstName) < 2:
        # elif len(first_name) < 2:
            flash("First Name must be greater than 2 characters", category="error")
        elif password1 != password2:
            flash("Passwords does not match", category="error")
        elif len(password1) < 7:
            flash("Password  must be greater than 4 characters", category="error")
        else:
            # new_user = User(email=email,firstName=firstName,password=generate_password_hash(password1,method='sha256'))
            flash("Account created!", category="success")
            # db.session.add(new_user)
            # db.session.commit()
             
            # pass
    return render_template("sign-up.html")