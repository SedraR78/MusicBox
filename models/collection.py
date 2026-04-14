from models.database import db
from .basemodel import BaseModel  

class Collection(BaseModel):
    __tablename__ = 'collections'

    title = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    is_public =  db.Column(db.Boolean, default=True)
