from datetime import datetime
from app import db


class Post(db.Model):
    """Пост"""
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey) (Foreign Key)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
