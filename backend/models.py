
import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from backend.db import Base, db
from backend import Session 
from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import UserMixin


class User(Base): #, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False ,default=datetime.datetime.utcnow)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    #posts = db.relationship('Post', backref='author', lazy=True)
    #games = db.relationship('Game', backref='author', lazy=True)

    def __init__(self, email, username, password, admin=False):
        self.email = email
        self.username = username
        hashed_password = generate_password_hash(password)
        #if user and check_password_hash(user.password, form.password.data):
        self.password = hashed_password
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def check_password(self, password):
        return check_password_hash(self.password, password)


    def get_token(self, expires_sec=259200): #259200sec=30days
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return Session.query(User).get(user_id)

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.email}', " \
               f"'{self.password}', '{self.admin}', '{self.registered_on}')"


class Game(Base):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    advanced = db.Column(db.Boolean, nullable=False, default=False)
    nplayers = db.Column(db.Integer, nullable=False)
    #title = db.Column(db.String(100), nullable=False)
    #date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #content = db.Column(db.Text, nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, advanced, nplayers):
        self.advanced = advanced
        self.nplayers = nplayers

    def __repr__(self):
        return f"Post('{self.id}')"

