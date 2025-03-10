# Create database model
from . import db # imports from current package (website folder)
from flask_login import UserMixin 
from sqlalchemy.sql import func # Can get current date and time

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # user.id references User (not case-sensitive)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # No 2 same emails
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

    notes = db.relationship('Note') # Capital

# Relationship needs to be set between Note and User using foreign key references
# One user - to - many notes
# lowercase for foreignkey, uppercase for relationship
