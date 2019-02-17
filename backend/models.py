
import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from backend.db import Base, db
from backend import Session
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
#from flask_login import UserMixin

games_players_association = db.Table(
    'games_players', Base.metadata,
    db.Column('game_id', db.Integer, db.ForeignKey('games.id')),
    db.Column('player_id', db.Integer, db.ForeignKey('users.id'))
)


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
    #games = db.relationship('GameModel', backref='author', lazy=True)
    own_games = relationship("GameModel", back_populates="owner",
                             foreign_keys="[GameModel.owner_id]")
    active_games = relationship("GameModel", back_populates="active",
                                foreign_keys="[GameModel.active_id]")

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

    def dict(self, includeGames=False):
        # return the user in dict format
        user = {}
        user['username'] = self.username
        user['id'] = self.id
        return user

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.email}', " \
               f"'{self.password}', '{self.admin}', '{self.registered_on}')"


class GameModel(Base):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    advanced = db.Column(db.Boolean, nullable=False, default=False)
    nplayers = db.Column(db.Integer, nullable=False)
    # backref="games" establishes that we can refer to User.games automatically
    players = relationship("User", secondary=games_players_association,
                           backref="games")
    # for the owner and active player I use the back_populates argument on both
    # side of the relationship, instead of backref on one
    owner_id = db.Column(db.Integer, db. ForeignKey('users.id'))
    owner = relationship("User",  foreign_keys=[owner_id],
                         back_populates="own_games")
    active_id = db.Column(db.Integer, db. ForeignKey('users.id'))
    active = relationship("User",  foreign_keys=[active_id],
                          back_populates="active_games")
    game = db.Column(db.PickleType)
    status = db.Column(db.String)
    # status can be: "new", "running", "finished"

    def __init__(self, advanced, nplayers, owner):
        self.advanced = advanced
        self.nplayers = nplayers
        self.owner = owner
        self.status = "new"

    def dict(self):
        # return the game in dict format
        game = {}
        game['id'] = self.id
        game['advanced'] = self.advanced
        game['nplayers'] = self.nplayers
        game['owner'] = self.owner.dict()
        game['active'] = self.active.dict() if self.active else None
        game['status'] = self.status
        game['players'] = []
        for plr in self.players:
            game['players'].append(plr.dict())
        return game

    def __repr__(self):
        return f"GameModel({self.id}, {self.status}, {self.advanced}, {self.nplayers})"

