from models.database import db
from .basemodel import BaseModel  

class Song(BaseModel):
    __tablename__ = 'songs'

    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    artist =  db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100))  
    album = db.Column(db.String(100)) 