from flask import jsonify, Blueprint, request
from backend.games.gameIO import readGameJSON, createGame
from backend.games.gameActions import *

from backend import Session
from backend.models import User


games = Blueprint('games', __name__)

def getUser(req):
    token = None
    if 'token' in req:
        token = req['token']
    session = Session()
    user=User.verify_token(token)
    return user

def getUserData(req):
    userData = {"name": None, "id": None }
    user = getUser(req)
    if user:
        userData = {"name": user.username, "id": user.id}
    return userData

@games.route("/createGame", methods=['PUT'])
def creategame():
    req = request.get_json()
    user = getUser(req)
    nplayers = req['nplayers']
    advanced = req['advanced']
    return createGame(user,nplayers,advanced)



@games.route("/game", methods=['GET','PUT'])
def get_game():
    req = request.get_json()
    userData = getUserData(req)
    return readGameJSON(userData=userData)

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
    userData = getUserData(req)
    error = selectTileAndCard(value, tile, userData['name'])
    if error:
        return error
    else:
        return readGameJSON(userData=userData)

@games.route("/game/passFunding", methods=['PUT'])
def passfunding():
    """
       need input parameters:
           (player, currentPlayer)
    """
    req = request.get_json()
    userData = getUserData(req)
    error = passFunding(userData['name'])
    if error:
        return error
    else:
        return readGameJSON(userData=userData)

@games.route("/game/passTrading", methods=['PUT'])
def passtrading():
    """
       need input parameters:
           (player, currentPlayer)
    """
    req = request.get_json()
    userData = getUserData(req)
    error = passTrading(userData['name'])
    if error:
        return error
    else:
        return readGameJSON(userData=userData)

@games.route("/game/buyTrade", methods=['PUT'])
def buytrade():
    """
       need input parameters:
           selected card (value is unique)
           (player, currentPlayer)
    """
    req = request.get_json()
    userData = getUserData(req)
    error = buyTrade(userData['name'])
    if error:
        return error
    else:
        return readGameJSON(userData=userData)

@games.route("/game/sellTrade", methods=['PUT'])
def selltrade():
    """
       need input parameters:
           selected card (value is unique)
           (player, currentPlayer)
    """
    req = request.get_json()
    userData = getUserData(req)
    error = sellTrade(userData['name'])
    if error:
        return error
    else:
        return readGameJSON(userData=userData)

@games.route("/game/offerTrade", methods=['PUT'])
def offertrade():
    """
       need input parameters:
           selected card (value is unique)
           (player, currentPlayer)
    """
    req = request.get_json()
    userData = getUserData(req)
    tile = req['tile']
    money = req['money']
    opponentName = req['opponentName']
    error = offerTrade(money, tile, opponentName, userData['name'])
    if error:
        return error
    else:
        return readGameJSON(userData=userData)

@games.route("/game/buyLuxuryTile", methods=['PUT'])
def buyluxurytile():
    """
       need input parameters:
           selected tile
           (player, currentPlayer)
    """
    req = request.get_json()
    tile = req['tile']
    userData = getUserData(req)
    error = buyLuxuryTile(tile, userData['name'])
    if error:
        return error
    else:
        return readGameJSON(userData=userData)


@games.route("/game/selectCardToDiscard", methods=['PUT'])
def selectcardtodiscard():
    """
       need input parameters:
           selected card (value is unique)
           (player, currentPlayer)
    """
    req = request.get_json()
    value = req['value']
    userData = getUserData(req)
    error = selectCardToDiscard(value, userData['name'])
    if error:
        return error
    else:
        return readGameJSON(userData=userData)

@games.route("/game/discardTile", methods=['PUT'])
def discardtile():
    """
       need input parameters:
           selected card (value is unique)
           (player, currentPlayer)
    """
    req = request.get_json()
    tile = req['tile']
    userData = getUserData(req)
    error = discardTile(tile, userData['name'])
    if error:
        return error
    else:
        return readGameJSON(userData=userData)
