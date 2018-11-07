from backend.games.game import Game
from backend.games.gameIO import writeGame, readGame

def selectCard(value):
    game = readGame()
    if game.removeCardFromBoard(value):
        game.addCardFromDeckToBoard()
        writeGame(game)

