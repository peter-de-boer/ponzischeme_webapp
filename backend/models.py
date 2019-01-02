from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from backend import db, create_app
#from flask_login import UserMixin


class User(db.Model): #, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    #posts = db.relationship('Post', backref='author', lazy=True)
    #games = db.relationship('Game', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


'''
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #title = db.Column(db.String(100), nullable=False)
    #date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}')"
'''


def init_db():
    '''
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    import os
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    # See important note below
    from backend.models import User
    '''
    app=create_app(createdb=True)

    with app.app_context():
        db.create_all()
        db.session.commit()

        admin = User(username='admin', email='admin@example.com', password='123')
        guest = User(username='guest', email='guest@example.com', password='abc')
        db.session.add(admin)
        db.session.add(guest)
        db.session.commit()
        users = User.query.all()
        print(users)

if __name__ == '__main__':
    init_db()
