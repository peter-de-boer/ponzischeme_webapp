import json, jsonpickle
from backend.games.game import Game

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

