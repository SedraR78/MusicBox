from .database import db
from .basemodel import BaseModel  

class User(BaseModel):
    __tablename__ = 'users'

    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password =  db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum('boxer','contributor','admin'), default= 'boxer' )