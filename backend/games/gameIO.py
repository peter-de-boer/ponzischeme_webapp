import json, jsonpickle
from backend.games.game import Game
from backend.models import GameModel
from backend import Session

def writeGame(game):

    gamejs = jsonpickle.encode(game)
    g = json.dumps(json.loads(gamejs), indent=2)
    f = open('game.json', 'w')
    f.write(g)
    f.close()

def readGame():

    f = open('game.json')
    gamejs = f.read()
    f.close()
    return jsonpickle.decode(str(gamejs))

def readGameJSON(userData = None):

    f = open('game.json')
    gamejs = f.read()
    f.close()
    gm = jsonpickle.decode(gamejs)
    gm.removeHiddenInfo(userData)
    gamejs_expand = jsonpickle.encode(gm, unpicklable=False)
    return gamejs_expand

def createGame(user, nplayers, advanced):
    if user:
        session = Session()
        newgame = GameModel(advanced=advanced, nplayers=nplayers, owner=user)
        newgame.players= [user]
        session.add(newgame)
        session.commit()
        session.close()
    return gameList()

def dbToDict(objects):
    dct = []
    for obj in objects:
        dct.append(obj.dict())
    return dct

def gameList():
    json_data = json.dumps(listOfGames())
    return json_data

def listOfGames():
    session = Session()
    newgames = session.query(GameModel) \
            .filter(GameModel.status=="new").all()
    runninggames = session.query(GameModel) \
            .filter(GameModel.status=="running").all()
    finishedgames = session.query(GameModel) \
            .filter(GameModel.status=="finished").all()
    lst = {}
    lst['new'] = dbToDict(newgames)
    lst['running'] = dbToDict(runninggames)
    lst['finished'] = dbToDict(finishedgames)
    session.close()
    return lst



