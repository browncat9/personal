
from flask import Blueprint , render_template , request , flash , redirect  , url_for
from .models import  User , db
from werkzeug.security import  generate_password_hash , check_password_hash
from  flask_login import login_user , login_required , logout_user , current_user


auth = Blueprint("auth" , __name__)

# login
@auth.route("/" , methods = ['GET'  , 'POST'])
def login():

    if request.method == "POST" :

        email = request.form.get("email")
        password = request.form.get("password")

        user =  User.query.filter_by(email = email).first()

        if user :

            if check_password_hash(user.password , password) :

                flash("Logged in successfully !" , category="success")

                login_user(user, remember=True)

                if user.userrole == "admin" :

                    return redirect(url_for("views.admin_dashboard"))

                elif user.userrole == "student" :

                     return redirect(url_for("views.student_dashboard"))

                elif user.userrole == "lecturer" :

                    return redirect(url_for("views.lecturer_dashboard"))

                elif user.userrole == "coordinator" :

                    return redirect(url_for("views.coordinator_dashboard"))
                else :
                    flash("Please choose of user role !", category="success")

            else :
                flash("Incorrect password , try again !" , category="error")
        else :
            flash("username does not exist !", category="error")


    return render_template("login.html"  , user = current_user)


# sign in
@auth.route("/sign-up" , methods = ["GET"  , "POST"])
def sign_in():

    if request.method == "POST" :

        userrole = request.form.get("userrole")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")

        user =  User.query.filter_by(email = email).first()

        print(request.form)

        if user :

            flash("email already exist " , category = "error")

        elif len(email) < 4 :
            # failed
            flash("Email must greater then 4 characters" , category = "error")

        elif len(username) < 2 :
            # failed
            flash("Username must greater then 2 characters" , category = "error")
        elif password !=  confirmPassword :
            # failed
            flash("Password and confirmed password not matched " , category = "error")

        elif len(password) < 7 :
            # failed
            flash("Password too short , password greater then 7 characters" , category = "error")

        else :
            # Success

            new_user =  User(email = email , username = username , userrole = userrole , password = generate_password_hash(password , method = "sha256"))

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True)

            flash("Account Created", category = "success")

            return redirect(url_for("auth.login"))

    return render_template("sign_up.html" , user = current_user)

# login out
@auth.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("auth.login"))
