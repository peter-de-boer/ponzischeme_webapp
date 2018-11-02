#import pickle
import json, jsonpickle
from game import Game

def writeGame(game):

    gamejs = jsonpickle.encode(game)
    g = json.dumps(json.loads(gamejs), indent=2)
    f = open('game.json', 'w')
    f.write(g)
    f.close()
    """
    with open('filename.pickle', 'wb') as handle:
        pickle.dump(gamejs, handle, protocol=pickle.HIGHEST_PROTOCOL)
    """

def readGame():

    f = open('game.json')
    gamejs = f.read()
    f.close()
    return jsonpickle.decode(gamejs)
    """
    with open('filename.pickle', 'rb') as handle:
        return pickle.load(handle)
    """

