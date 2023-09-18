from app import db


class Comment(db.Model):
    """Комментарий"""
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    # comment_date = db.Column(db.Date)
    # likes_count = db.Column(db.Integer, db.ForeignKey(''))

