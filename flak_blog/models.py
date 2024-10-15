ECHO is on.
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.string(100), nullable = False)
    content = db.Column(db.Text, nullable = False)

    def __repr__(self):
        retuen f'<BlogPost {self.title}>'