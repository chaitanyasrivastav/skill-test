from database import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), nullable=False)
    topic = db.Column(db.String(120), nullable=False)
    weightage = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Question %r>' % self.topic
