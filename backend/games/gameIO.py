import json, jsonpickle
from game import Game

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
    return jsonpickle.decode(gamejs)

