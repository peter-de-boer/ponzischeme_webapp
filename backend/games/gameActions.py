from backend.games.game import Game
from backend.games.gameIO import writeGame, readGame

def selectCard(value, name):
    game = readGame()
    active = game.activePlayerIndex
    if (name==game.players[active].name):
        card = game.removeCardFromBoard(value)
        if card:
            game.players[active].selectCard(card)
            game.addCardFromDeckToBoard()
            writeGame(game)

