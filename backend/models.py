
import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from backend.db import Base, db
from backend import Session
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
import jsonpickle
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
    confirmed = db.Column(db.Boolean)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    #posts = db.relationship('Post', backref='author', lazy=True)
    #games = db.relationship('GameModel', backref='author', lazy=True)
    own_games = relationship("GameModel", back_populates="owner",
                             foreign_keys="[GameModel.owner_id]")
    active_games = relationship("GameModel", back_populates="active",
                                foreign_keys="[GameModel.active_id]")
    own_notes = relationship("Notes", back_populates="player",
                             foreign_keys="[Notes.player_id]")

    def __init__(self, email, username, password, admin=False, confirmed=False):
        self.email = email
        self.username = username
        self.set_password(password)
        #hashed_password = generate_password_hash(password)
        #self.password = hashed_password
        self.registered_on = datetime.datetime.now()
        self.confirmed = confirmed
        self.admin = admin

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        hashed_password = generate_password_hash(password)
        self.password = hashed_password

    def get_reset_token(self, expires_sec=86400):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id},salt='reset').decode('utf-8')

    def get_token(self, expires_sec=2592000): #2592000sec=30days
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    def get_registration_token(self, expires_sec=86400): # 86400 = 1 day
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id},salt='registration').decode('utf-8')

    @staticmethod
    def verify_token(token, salt=None):
        s = Serializer(current_app.config['SECRET_KEY'])
        """
        print("try: ")
        stoken = s.loads(token)
        user_id = stoken['user_id']
        """
        try:
            user_id = s.loads(token, salt=salt)['user_id']
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
               f"'{self.password}', '{self.admin}', '{self.registered_on}'," \
                f"'{self.confirmed}')"


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
    chat = db.Column(db.PickleType)
    status = db.Column(db.String)
    # status can be: "new", "running", "finished"
    player_notes = relationship("Notes", back_populates="game",
                             foreign_keys="[Notes.game_id]")

    def __init__(self, advanced, nplayers, owner):
        self.advanced = advanced
        self.nplayers = nplayers
        self.owner = owner
        self.status = "new"
        self.chat = jsonpickle.encode([])

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
        game['player_notes'] = []
        for notes in self.player_notes:
            game['player_notes'].append(notes.dict())
        return game

    def __repr__(self):
        return f"GameModel({self.id}, {self.status}, {self.advanced}, "\
                f"{self.nplayers}, {self.chat})"


class Notes(Base):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String)
    # for the game and player I use the back_populates argument on both
    # side of the relationship, instead of backref on one
    player_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    player = relationship("User",  foreign_keys=[player_id],
                         back_populates="own_notes")
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    game = relationship("GameModel",  foreign_keys=[game_id],
                          back_populates="player_notes")

    def __init__(self, player, game):
        self.notes = ""
        self.player = player
        self.game = game

    def dict(self):
        # return the notes in dict format
        notes = {}
        notes['id'] = self.id
        notes['notes'] = self.notes
        notes['player_id'] = self.player.id
        notes['game_id'] = self.game.id
        return notes

    def __repr__(self):
        return f"Notes({self.id}, {self.player.id}, {self.game.id}, {self.notes})"

