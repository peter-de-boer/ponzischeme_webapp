from backend.games.game import Game
from backend.games.gameIO import writeGame, readGame

def selectCard(value):
    game = readGame()
    card = game.removeCardFromBoard(value)
    if card:
        active = game.activePlayerIndex
        game.players[active].selectCard(card)
        game.addCardFromDeckToBoard()
        writeGame(game)

