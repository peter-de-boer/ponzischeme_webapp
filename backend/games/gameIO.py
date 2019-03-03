import json, jsonpickle
from backend.games.game import Game
from backend.models import GameModel, User
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

def getUserData(user):
    if user:
        userData = {"name": user.username, "id": user.id}
    else:
        userData = {"name": None, "id": None }
    return userData

def getGame(userData = None, id = None):

    session = Session()
    game = session.query(GameModel) \
            .filter(GameModel.id==id).first()
    gm = jsonpickle.decode(game.game)
    session.commit()
    session.close()
    gm.removeHiddenInfo(userData)
    gamejs_expand = jsonpickle.encode(gm, unpicklable=False)
    return gamejs_expand

def createGame(user, nplayers, advanced):
    userData = getUserData(user)
    if user:
        session = Session()
        newgame = GameModel(advanced=advanced, nplayers=nplayers, owner=user)
        newgame.players= [user]
        session.add(newgame)
        session.commit()
        session.close()
    return gameList(userData)

def deleteGame(user, gameid):
    userData = getUserData(user)
    if user:
        session = Session()
        game = session.query(GameModel) \
                .filter(GameModel.id==gameid).first()
        if game.owner==user and game.status=="new":
            session.delete(game)
        session.commit()
        session.close()
    return gameList(userData)

def joinGame(user, gameid):
    userData = getUserData(user)
    if user:
        session = Session()
        game = session.query(GameModel) \
                .filter(GameModel.id==gameid).first()
        if ((user not in game.players) and
           (len(game.players)<game.nplayers) and
           game.status=="new"):
            game.players.append(user)
        session.commit()
        session.close()
    return gameList(userData)

def leaveGame(user, gameid):
    userData = getUserData(user)
    if user:
        session = Session()
        game = session.query(GameModel) \
                .filter(GameModel.id==gameid).first()
        if (user!=game.owner) and (user in game.players) and game.status=="new":
            game.players.remove(user)
        session.commit()
        session.close()
    return gameList(userData)

def startGame(user, gameid):
    userData = getUserData(user)
    if user:
        session = Session()
        game = session.query(GameModel) \
                .filter(GameModel.id==gameid).first()
        if ((user==game.owner) and (user in game.players) and 
            game.status=="new" and (len(game.players)==game.nplayers)):
            players = []
            for player in game.players:
                players.append({'name': player.username, 'id': player.id})
            newgame = Game(players, game.advanced, game.id)
            activePlayer = newgame.getActivePlayer()
            active = session.query(User) \
                    .filter(User.id==activePlayer.id).first()
            game.active = active
            game.status="running"
            game.game = jsonpickle.encode(newgame)
        session.commit()
        session.close()
    return gameList(userData)

def dbToDict(objects):
    dct = []
    for obj in objects:
        dct.append(obj.dict())
    return dct

def gameList(userData):
    json_data = json.dumps([userData, listOfGames()])
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



