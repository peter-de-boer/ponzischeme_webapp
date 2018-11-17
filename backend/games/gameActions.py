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

def passFunding(name):
    game = readGame()
    error = game.passFunding(name)
    if error:
        return error
    else:
        writeGame(game)
        return None

def selectCardToDiscard(value, name):
    game = readGame()
    error = game.selectCardToDiscard(value, name)
    if error:
        return error
    else:
        writeGame(game)
        return None

def discardTile(tile, name):
    game = readGame()
    error = game.discardTile(tile, name)
    if error:
        return error
    else:
        writeGame(game)
        return None

