from datetime import datetime
from app import db


class User(db.Model):
    """Пользователь"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))
    # first_name = db.Column(db.String())
    # last_name = db
    # date_of_birth = db.Column(db.Date)
    # profile_picture = db.Column(db.)
    # joined_date = db.Column(db.String)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
