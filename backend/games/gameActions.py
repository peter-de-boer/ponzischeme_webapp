import json
from backend.games.game import Game
from backend.games.gameIO import writeGame, readGame

def selectTileAndCard(value, tile, name):
    game = readGame()
    data = {}
    # check if player is active player
    active = game.activePlayerIndex
    if (name!=game.players[active].name):
        data['error'] = name + " is not the active player"
        return json.dumps(data)
    # check if player is allowed to take this combination of tile and card
    numberOfTiles = game.players[active].industryTiles[tile]
    row = game.fundingBoard.getRow(value)
    if (row != numberOfTiles+1):
        data['error'] = "You have " +  str(numberOfTiles) + \
                       " tiles, you cannot select a card from  row " + str(row)
        return json.dumps(data)
    card = game.removeCardFromBoard(value)
    if card:
        game.players[active].selectCardAndTile(card, tile)
        game.addCardFromDeckToBoard()
        writeGame(game)
        return None


