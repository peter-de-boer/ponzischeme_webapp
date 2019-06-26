# template for viewing db contents

from backend.db import engine, Base
from backend.models import User, GameModel, Notes
import json,jsonpickle

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

'''
print("********* notes ***********")
for instance in session.query(Notes).order_by(Notes.id):
    print(instance)
'''

'''
print("********* games/notes ***********")
for instance in session.query(GameModel).order_by(GameModel.id):
    print("player_notes: ", instance.player_notes)
    if instance.player_notes is None:
        print("no player_notes yet")
    else:
        for notes in instance.player_notes:
            print(notes)
'''

'''
print("********* users ***********")
for instance in session.query(User).order_by(User.id):
    print(instance)
    #print(instance.username, instance.email)
    print(instance.dict())

'''


'''
print("********* game2 ***********")
game = session.query(GameModel).filter(GameModel.id==2).first()
gm = jsonpickle.decode(game.game)
print(game.game)
'''



'''
print("********* games ***********")
for instance in session.query(GameModel).order_by(GameModel.id):
    print(instance)
'''
'''
    print("chat: ", instance.chat)
    chati = instance.chat
    chat = jsonpickle.decode(chati)
    #print("chat: ", chat)
    print("number of players: ", len(instance.players))
    for player in instance.players:
        print(player.username)
    print(instance.dict())
'''

'''
alice_games = session.query(GameModel) \
        .join(User, GameModel.players) \
        .filter(User.username == "Alice") \
        .all()

alice = session.query(User) \
        .filter(User.username=="Alice") \
        .first()

print("Alice games")

for game in alice_games:
    print(game)

print("Alice games(2)")

for game in alice.games:
    print(game)


alice_owner_games = session.query(GameModel) \
        .join(User, GameModel.owner) \
        .filter(User.username=="Alice") \
        .all()

print("Alice owns games")

for game in alice_owner_games:
    print(game)


alice_owner_games2 = alice.own_games

print("Alice owns games (2)")

for game in alice_owner_games2:
    print(game)
'''

#print("Games in JSON format: ")
#games = GameModel.__table__
#res = session.execute(games.select())
#jsongames = json.dumps([dict(r) for r in res])
#print(jsongames)

#print("Games in dict format: ")
#for u in session.query(GameModel).all():
#    print(u.__dict__)


session.close()
