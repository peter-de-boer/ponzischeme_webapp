# template for creating a fresh new db for testing purposes

from backend.db import engine, Base, db
from backend.models import User, GameModel, ChatModel

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

admin = User(username='admin', email='admin@example.com', password='123',
             admin=True, confirmed = True )
alice =   User(username='Alice',   email='alice@example.com',   password='abc',
              confirmed = True)
bob =     User(username='Bob',     email='bob@example.com',     password='abc',
              confirmed = True)
charlie = User(username='Charlie', email='charlie@example.com', password='abc',
              confirmed = True)
ww = User(username='ww', email='peterdeboer_private@hotmail.com', password='abc',
              confirmed = True)

game1 = GameModel(advanced=False, nplayers=3, owner=bob)
game1.players= [alice, bob, charlie]

game2 = GameModel(advanced=True, nplayers=3, owner=alice)
game2.players= [alice]

game3 = GameModel(advanced=False, nplayers=3, owner=bob)
game3.players= [bob, charlie]

game4 = GameModel(advanced=False, nplayers=4, owner=bob)
game4.players= [alice, bob, charlie]

game5 = GameModel(advanced=True, nplayers=3, owner=alice)
game5.players= [alice, bob]

chat = ChatModel()

session.add(chat)

session.add(admin)
session.add(alice)
session.add(bob)
session.add(charlie)
session.add(ww)

session.add(game1)
session.add(game2)
session.add(game3)
session.add(game4)
session.add(game5)


session.commit()
session.close()

