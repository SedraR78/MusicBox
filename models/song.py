from .database import db
from .basemodel import BaseModel  

class Song(BaseModel):
    __tablename__ = 'songs'

    title = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    artist =  db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(200))  
    album = db.Column(db.String(50)) 