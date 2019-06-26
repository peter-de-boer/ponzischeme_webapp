# template for changing the db

from backend.db import engine, Base
from backend.models import User, GameModel, Notes
import jsonpickle
import copy
from werkzeug.security import generate_password_hash, check_password_hash

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

'''
gameToBeDeleted = session.query(GameModel).filter(GameModel.id==13).first()
session.delete(gameToBeDeleted)
'''


'''
findName = "<old_username>"
newName = "<new_username>"

userToBeChanged = session.query(User) \
        .filter(User.username==findName) \
        .first()


user_games = session.query(GameModel) \
        .join(User, GameModel.players) \
        .filter(User.username == findName)

for gms in user_games:
    print(gms.id)
    gmp = gms.game
    if gmp is not None:
        gm = jsonpickle.decode(gmp)
        for plr in gm.players:
            print(plr.name)
            if plr.name==findName:
                plr.changeName(newName)
        print("after change:")
        for plr in gm.players:
            print(plr.name)
        gms.game = jsonpickle.encode(gm)

userToBeChanged.username = newName
'''

'''
usr=session.query(User).filter(User.email=="<email>").first()
password="<new_password>"
hashed_password = generate_password_hash(password)
usr.password = hashed_password
'''




session.commit()

session.close()
