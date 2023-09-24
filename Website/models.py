from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True) , default = func.now())

    # add foreign key
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class Notification(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    s_userrole = db.Column(db.String(150))

    s_userid = db.Column(db.Integer, db.ForeignKey("user.id"))

    r_userrole = db.Column(db.String(150))

    r_userid = db.Column(db.Integer, db.ForeignKey("user.id"))

    module_code = db.Column(db.String(150), db.ForeignKey("module.module_code"))

    message = db.Column(db.String(300))

    module = db.relationship("Module")

    user_s = db.relationship("User", foreign_keys=[s_userid])
    
    user_r = db.relationship("User", foreign_keys=[r_userid])


class User(db.Model , UserMixin) :

    id = db.Column(db.Integer , primary_key = True)

    email = db.Column(db.String(150) , unique = True)

    username = db.Column(db.String(150))

    userrole = db.Column(db.String(150))

    password = db.Column(db.String(150))

    credit = db.Column(db.String(150))

    enrollment_date = db.Column(db.Date() , default = "1970-01-01")


class Module(db.Model , UserMixin) :

    module_code = db.Column(db.String(150) ,primary_key = True)

    module_name = db.Column(db.String(150))

    module_credit = db.Column(db.Integer)

    semester = db.Column(db.Date() , default = "1970-01-01")

    module_status = db.Column(db.Boolean , default = False)

    # add relationship
    # user = db.relationship("User")

class Config(db.Model , UserMixin) :

    id = db.Column(db.Integer , primary_key = True)

    module_code = db.Column(db.String(150), db.ForeignKey("module.module_code"))

    coordinator_id = db.Column(db.Integer)

    lecturer_id = db.Column(db.Integer)

    student_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    mark = db.Column(db.Double)

    gpa = db.Column(db.Double)

    earn_credit = db.Column(db.Double)

    status = db.Column(db.Boolean , default = False)

    module = db.relationship("Module")

    user = db.relationship("User")




