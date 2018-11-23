from flask import jsonify, Blueprint, request
from backend.games.gameIO import readGameJSON
from backend.games.gameActions import *



games = Blueprint('games', __name__)


@games.route("/game", methods=['GET'])
def get_game():
    return readGameJSON()
    """
    return jsonify(game_id=1,
                   player1 = "peter")
    """

@games.route("/game/selectTileAndCard", methods=['PUT'])
def selecttileandcard():
    """
       need input parameters:
           selected card (value is unique), tile
           (player, currentPlayer)
    """
    req = request.get_json()
    value = req['value']
    tile = req['tile']
    name = req['name']
    error = selectTileAndCard(value, tile, name)
    if error:
        return error
    else:
        return readGameJSON()

@games.route("/game/passFunding", methods=['PUT'])
def passfunding():
    """
       need input parameters:
           (player, currentPlayer)
    """
    req = request.get_json()
    name = req['name']
    error = passFunding(name)
    if error:
        return error
    else:
        return readGameJSON()

@games.route("/game/passTrading", methods=['PUT'])
def passtrading():
    """
       need input parameters:
           (player, currentPlayer)
    """
    req = request.get_json()
    name = req['name']
    error = passTrading(name)
    if error:
        return error
    else:
        return readGameJSON()

@games.route("/game/buyTrade", methods=['PUT'])
def buytrade():
    """
       need input parameters:
           selected card (value is unique)
           (player, currentPlayer)
    """
    req = request.get_json()
    name = req['name']
    error = buyTrade(name)
    if error:
        return error
    else:
        return readGameJSON()

@games.route("/game/sellTrade", methods=['PUT'])
def selltrade():
    """
       need input parameters:
           selected card (value is unique)
           (player, currentPlayer)
    """
    req = request.get_json()
    name = req['name']
    error = sellTrade(name)
    if error:
        return error
    else:
        return readGameJSON()

@games.route("/game/offerTrade", methods=['PUT'])
def offertrade():
    """
       need input parameters:
           selected card (value is unique)
           (player, currentPlayer)
    """
    req = request.get_json()
    tile = req['tile']
    money = req['money']
    opponentName = req['opponentName']
    name = req['name']
    error = offerTrade(money, tile, opponentName, name)
    if error:
        return error
    else:
        return readGameJSON()


@games.route("/game/selectCardToDiscard", methods=['PUT'])
def selectcardtodiscard():
    """
       need input parameters:
           selected card (value is unique)
           (player, currentPlayer)
    """
    req = request.get_json()
    value = req['value']
    name = req['name']
    error = selectCardToDiscard(value, name)
    if error:
        return error
    else:
        return readGameJSON()

@games.route("/game/discardTile", methods=['PUT'])
def discardtile():
    """
       need input parameters:
           selected card (value is unique)
           (player, currentPlayer)
    """
    req = request.get_json()
    tile = req['tile']
    name = req['name']
    error = discardTile(tile, name)
    if error:
        return error
    else:
        return readGameJSON()
