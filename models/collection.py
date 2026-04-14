from .database import db
from .basemodel import BaseModel 


collection_songs = db.Table('collection_songs',
    db.Column('collection_id',db.ForeignKey('collections.id')),
    db.Column('song_id',db.ForeignKey('songs.id'))
) 

class Collection(BaseModel):
    __tablename__ = 'collections'

    title = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    is_public =  db.Column(db.Boolean, default=True)
    songs = db.relationship('Song', secondary=collection_songs, backref='collections')