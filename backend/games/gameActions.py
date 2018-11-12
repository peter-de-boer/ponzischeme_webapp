import json
from backend.games.game import Game
from backend.games.gameIO import writeGame, readGame

def selectTileAndCard(value, tile, name):
    game = readGame()
    error = game.selectTileAndCard(value, tile, name)
    if error:
        return error
    else:
        writeGame(game)
        return None
