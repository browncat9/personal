import json

from flask import Blueprint , render_template , flash,request , redirect , url_for, request, jsonify
from  flask_login import login_required , current_user
from .import utils
from .models import User , Module , Config ,Notification, db
import json
from werkzeug.security import  generate_password_hash , check_password_hash
from sqlalchemy import update
import  datetime

views = Blueprint("views" , __name__)

@views.route("/admin_dashboard" , methods = ["GET" , "POST"] )
@login_required
def admin_dashboard():

    if request.method == "POST" :

        userrole = request.form.get("userrole")

        username = request.form.get("username")

        email = request.form.get("email")

        credit = request.form.get("credit") # only applicable to student

        if credit == "" :
            credit = "N/A"

        enrollment_date = request.form.get("enrollment_date") # only applicable to student
        enrollment_date = datetime.datetime.strptime(enrollment_date , "%Y-%m-%d")

        if enrollment_date == "" :
            enrollment_date = None

        password = "password" # each user will set default password

        user = User.query.filter_by(email=email).first()

        if user :
            flash("Current User already created " , category = "error")

        elif userrole == "" :
            flash("Please proceed to choose choose user role ", category="error")

        elif len(username) < 1 :
            flash("Please enter proper username ", category="error")

        elif len(email) < 4 :
            flash("Please enter proper email ", category="error")

        else :

            new_user = User(email=email, username=username, userrole=userrole,
                        credit= credit, enrollment_date = enrollment_date, password=generate_password_hash(password, method="sha256"))
            db.session.add(new_user)
            db.session.commit()

            flash(f"{userrole} Account Created", category="success")

    all_user = User.query.filter().all()

    all_module = Module.query.filter().all()

    all_config = Config.query.filter().all()

    all_coordinators = User.query.filter_by(userrole="coordinator").all()


    return render_template("admin_dashboard.html" ,all_user = all_user, all_module = all_module ,  user = current_user , config = all_config, all_coordinators = all_coordinators)

@views.route("/module_status" , methods = ["GET" , "POST"] )
@login_required
def module_status():

    if request.method == "POST":

        module_code = request.form.get("module_code")

        module_name = request.form.get("module_name")

        module_credit = request.form.get("module_credit")

        assign_semester = request.form.get("assign_semester")

        assign_semester = datetime.datetime.strptime(assign_semester , "%Y-%m-%d")

        new_module = Module(module_code=module_code, module_name=module_name, module_credit = module_credit , semester = assign_semester );

        db.session.add(new_module)
        db.session.commit()

        flash("Module Created Success ", category="success")

    return redirect(url_for("views.admin_dashboard"))

@views.route("/assign_coordinator" , methods = [ "POST"] )
@login_required
def assign_coordinator():
    selected_coordinator_ids = request.json

    error_messages = []

    for coordinator_id in selected_coordinator_ids:
        if Config.query.filter_by(coordinator_id=coordinator_id).first():
            error_messages.append(f"Coordinator {coordinator_id} already assigned to a module")

    if len(error_messages) == 0:
        return redirect(url_for("views.admin_dashboard"))
    else:
        return jsonify(error= ", ".join(error_messages))
    


@views.route("/assign_module" , methods = ["GET" , "POST"] )
@login_required
def assign_module():


    if request.method == "POST":


        print((request.form))

        module_assign = request.form.get("module_assign")

        lecturer_assign = request.form.get("lecturer_assign")

        coordinator_assign = request.form.get("coordinator_assign") #edit

        student_ids = request.form.getlist("student_id")

        if module_assign == "" :
            flash("Please choose one module to assign")

        elif lecturer_assign == "":
            flash("Please choose one lecturer to assign")

        elif coordinator_assign == "":
            flash("Please choose one coordinator to assign") #edit

        elif len(student_ids) == 0:

            flash("Please choose at least one student to assign")

        else:
            flash(f"{module_assign} Module successfully assigned to lecturer and student")

            for each in student_ids :

                print(f"Coordinator: {coordinator_assign}")
                new_cofig = Config(module_code=module_assign, coordinator_id=coordinator_assign, lecturer_id=lecturer_assign ,
                                student_id = each)

                db.session.add(new_cofig)
                db.session.commit()

    return redirect(url_for("views.admin_dashboard"))

@views.route("/student_dashboard" , methods = ["GET" , "POST"] )
@login_required
def student_dashboard():

    all_user = User.query.filter().all()

    current_id = current_user.id

    all_module = Config.query.filter_by(student_id=current_id).all()

    #what i added to use the function in utils.py

    module_marks = [mark.mark for mark in all_module]
    module_gpas = [utils.marks_gpa(mark) for mark in module_marks]

    #update config objects with new GPA

    for config, gpa in zip(all_module, module_gpas):
        config.gpa = gpa
        db.session.commit()


    for each in all_module :
        print(each.module.module_name)

    return render_template("student_dashboard.html", all_user=all_user, all_module=all_module, user=current_user, module_gpas=module_gpas, module_marks=module_marks)

@views.route("/lecturer_dashboard", methods=["GET", "POST"])
@login_required
def lecturer_dashboard():
    current_id = current_user.id

    all_config = Config.query.filter_by(lecturer_id=current_id).all()

    if not all_config:
        return render_template("lecturer_dashboard.html", module=None, all_config=[], user=current_user)

    all_config_deduplicated = []
    module_codes_inserted = []

    for config in all_config:
        if config.module_code not in module_codes_inserted:
            all_config_deduplicated.append(config)
            module_codes_inserted.append(config.module_code)

    module = Module.query.filter_by(module_code=all_config[0].module_code).first()

    return render_template("lecturer_dashboard.html", module=module, all_config=all_config_deduplicated, user=current_user)


@views.route("/grade_module/<module_code>", methods=["GET", "POST"])
@login_required
def grade_module(module_code):

    current_id = current_user.id
    grade_module_config = Config.query.filter_by(lecturer_id = current_id , module_code = module_code).first()
    students = Config.query.filter_by(module_code=module_code).all()

    module_status = grade_module_config.module.module_status
    module = Module.query.filter_by(module_code=module_code).first() 

    if request.method == "POST":
        for student in students:
            student_id = student.user.id
            mark = request.form.get(f"grade_{student_id}")  

            if mark is not None and mark != "":
                stmt = update(Config).where(
                    (Config.student_id == student_id) & (Config.module_code == module_code)
                ).values(mark=mark) 

                db.session.execute(stmt)

        db.session.commit()

        flash(f"Grades updated for module {module_code}", category="success")


    return render_template("grade_module.html", module_code=module_code, students=students, grade_module_config = grade_module_config, user = current_user, module_status=module_status, module= module)

@views.route("/notify_coordinator/<module_code>", methods=["GET", "POST"])
@login_required
def notify_coordinator(module_code):
    s_userid = current_user.id 
    s_userrole = current_user.userrole

    r_userid = Config.query.filter_by(module_code=module_code).first().coordinator_id
    r_userrole = User.query.filter_by(id=r_userid).first().userrole

    if request.method == "POST":
        message = request.form.get("message")
        new_note = Notification(
            s_userid=s_userid,
            s_userrole=s_userrole,
            r_userid=r_userid,
            r_userrole=r_userrole,
            message= message,
            module_code=module_code,
        )
        db.session.add(new_note)
        db.session.commit()

        flash("Message sent", category="success")
        return redirect(url_for("views.grade_module", module_code=module_code))


@views.route("/coordinator_dashboard" , methods = ["GET" , "POST"] ) #edit
@login_required
def coordinator_dashboard():

    all_user = User.query.filter().all()
    current_id = current_user.id 

    # Get all config for current coordinator
    configs = Config.query.filter_by(coordinator_id = current_id ).all()
    all_notification = Notification.query.filter().all()

    unique_modules = {}  # to store modules

    for config in configs:
        module = Module.query.filter_by(module_code=config.module_code).first()

        key = (module.module_code, module.semester)
        if key not in unique_modules:
            lecturer_id = config.lecturer_id
            lecturer = User.query.get(lecturer_id)
            if lecturer:
                module.lecturer_name = lecturer.username
                module.lecturer_id = lecturer.id
            else:
                module.lecturer_name = "Unknown Lecturer"
            unique_modules[key] = module

    modules = list(unique_modules.values())

    all_config = Config.query.filter().all()

    module = Module.query.filter_by(module_code=configs[0].module_code).first()

    notifications = Notification.query.filter_by(r_userid=current_id).all()


    return render_template("coordinator_dashboard.html", all_user=all_user, modules=modules, module=module, config=configs, user=current_user,
                           all_config=all_config, all_notification= all_notification, notifications=notifications)

#todo: change vet_module to vet module... 
@views.route("/vet_module/<module_code>", methods=["GET", "POST"]) 
@login_required
def vet_module(module_code):

    current_id = current_user.id

    module = Module.query.filter_by(module_code=module_code).first() 
    if not module:
        flash(f"Module {module_code} not found.", category="error")
        return redirect(url_for('views.coordinator_dashboard'))
    
    config = Config.query.filter_by(coordinator_id = current_id , module_code = module_code).first()
    
    students = Config.query.filter_by(module_code=module_code).all()

    module_status = config.module.module_status
    module = Module.query.filter_by(module_code=module_code).first() 

    if request.method == "POST":
        for student in students:
            student_id = student.user.id
            mark = request.form.get(f"grade_{student_id}")  

            if mark is not None and mark != "":
                stmt = update(Config).where(
                    (Config.student_id == student_id) & (Config.module_code == module_code)
                ).values(mark=mark) 

                db.session.execute(stmt)

        db.session.commit()

        flash(f"Grades updated for module {module_code}", category="success")


    return render_template("vet_module.html", module_code=module_code, students=students, config = config, user = current_user, module_status=module_status, module= module)


@views.route("/lock_module/<module_code>/<semester>", methods=["POST"])
@login_required
def lock_module(module_code, semester):
   
    module = Module.query.filter_by(module_code=module_code, semester=semester).first()
    if module:
        module.module_status = True
        db.session.commit()
        flash(f"Module {module_code} is now locked.", category="success")
    else:
        flash(f"Module {module_code} not found.", category="error")

    return redirect(url_for('views.vet_module', module_code=module_code))


   



@views.route("/notify_admin/<module_code>", methods=["GET", "POST"])
@login_required
def notify_admin(module_code):
    s_userid = current_user.id 
    s_userrole = current_user.userrole

    #only will work if db only has one admin
    r_userid = User.query.filter_by(userrole="admin").first().id
    r_userrole = User.query.filter_by(id=r_userid).first().userrole

    if request.method == "POST":
        message = request.form.get("message")
        new_note = Notification(
            s_userid=s_userid,
            s_userrole=s_userrole,
            r_userid=r_userid,
            r_userrole=r_userrole,
            message= message,
            module_code=module_code,
        )
        db.session.add(new_note)
        db.session.commit()

        flash("Message sent", category="success")
        return redirect(url_for("views.vet_module", module_code=module_code))

@views.route("/delete-note" , methods = ["POST"])
def delete_note():

    note = json.loads(request.data)

    noteId = note["nodeId"]

    # note = Note.query.get(noteId)

    if note :

        if note.user_id == current_user.id :

            db.session.delete(note)
            db.session.commit()

    return ""

