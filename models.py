from setuptools.compat import unicode
from SchoolPortal import db
from SchoolPortal import bcrypt


from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class BlogPost(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<title {}'.format(self.title)

class Students(db.Model):
    __tablename__ = "student"

    uid = db.Column(db.Integer, primary_key=True)
    firstname= db.Column(db.String, nullable=False)
    second_name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    address1 = db.Column(db.String, nullable=False)
    address2 = db.Column(db.String, nullable=False)
    telephone = db.Column(db.String, nullable=False)
    cell_number = db.Column(db.String, nullable=False)
    dob = db.Column(db.String, nullable=False)
    identification_number = db.Column(db.String, nullable=False)
    passport_number = db.Column(db.String, nullable=False)
    marital_status = db.Column(db.Integer, nullable=False)
    full_spouse_name = db.Column(db.String, nullable=False)
    tracking = db.Column(db.String, nullable=False)
    rank = db.Column(db.Integer, nullable=False)

    def __init__(self, firstname, second_name, surname,gender,email,address1,address2,telephone,cell_number,dob,
                 identification_number, passport_number, marital_status, full_spouse_name, tracking, rank):
        self.firstname = firstname
        self.second_name = second_name
        self.surname = surname
        self.gender = gender
        self.email = email
        self.address1 = address1
        self.address2 = address2
        self.telephone = telephone
        self.cell_number = cell_number
        self.dob = dob
        self.identification_number = identification_number
        self.passport_number = passport_number
        self.marital_status = marital_status
        self.full_spouse_name = full_spouse_name
        self.tracking = tracking
        self.rank = rank

    def __repr__(self):
        return '<firstname - {}>'.format(self.firstname)




class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    posts = relationship("BlogPost", backref="author")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.name)