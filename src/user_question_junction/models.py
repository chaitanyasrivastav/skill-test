from datetime import datetime
from database import db

class UserQuestion(db.Model):
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.ForeignKey('question.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    last_attempt = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<UserQuestion %r>' % self.user_id