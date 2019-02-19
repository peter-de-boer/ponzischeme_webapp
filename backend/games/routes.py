from flask import jsonify, Blueprint, request
from backend.games.gameIO import *
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

@games.route("/gameList", methods=['GET'])
def gamelist():
    return gameList()

@games.route("/createGame", methods=['PUT'])
def creategame():
    req = request.get_json()
    user = getUser(req)
    nplayers = req['nplayers']
    advanced = req['advanced']
    return createGame(user,nplayers,advanced)

@games.route("/deleteGame", methods=['PUT'])
def deletegame():
    req = request.get_json()
    user = getUser(req)
    gameid = req['id']
    return deleteGame(user,gameid)

@games.route("/joinGame", methods=['PUT'])
def joingame():
    req = request.get_json()
    user = getUser(req)
    gameid = req['id']
    return joinGame(user,gameid)

@games.route("/leaveGame", methods=['PUT'])
def leavegame():
    req = request.get_json()
    user = getUser(req)
    gameid = req['id']
    return leaveGame(user,gameid)

@games.route("/startGame", methods=['PUT'])
def startgame():
    req = request.get_json()
    user = getUser(req)
    gameid = req['id']
    return startGame(user,gameid)




@games.route("/game", methods=['GET','PUT'])
def get_game():
    req = request.get_json()
    userData = getUserData(req)
    id = req['id']
    return getGame(userData=userData, id=id)

@games.route("/game/selectTileAndCard", methods=['PUT'])
def selecttileandcard():
    """
       need input parameters:
           selected card (value is unique), tile
           (player, currentPlayer)
    """
    req = request.get_json()
    id = req['id']
    value = req['value']
    tile = req['tile']
    userData = getUserData(req)
    error = selectTileAndCard(id, value, tile, userData['name'])
    if error:
        return error
    else:
        return getGame(userData=userData, id=id)

@games.route("/game/passFunding", methods=['PUT'])
def passfunding():
    """
       need input parameters:
           (player, currentPlayer)
    """
    req = request.get_json()
    id = req['id']
    userData = getUserData(req)
    error = passFunding(id, userData['name'])
    if error:
        return error
    else:
        return getGame(userData=userData, id=id)

@games.route("/game/passTrading", methods=['PUT'])
def passtrading():
    """
       need input parameters:
           (player, currentPlayer)
    """
    req = request.get_json()
    id = req['id']
    userData = getUserData(req)
    error = passTrading(id, userData['name'])
    if error:
        return error
    else:
        return getGame(userData=userData, id=id)

@games.route("/game/buyTrade", methods=['PUT'])
def buytrade():
    """
       need input parameters:
           selected card (value is unique)
           (player, currentPlayer)
    """
    req = request.get_json()
    id = req['id']
    userData = getUserData(req)
    error = buyTrade(id, userData['name'])
    if error:
        return error
    else:
        return getGame(userData=userData, id=id)

@games.route("/game/sellTrade", methods=['PUT'])
def selltrade():
    """
       need input parameters:
           selected card (value is unique)
           (player, currentPlayer)
    """
    req = request.get_json()
    id = req['id']
    userData = getUserData(req)
    error = sellTrade(id, userData['name'])
    if error:
        return error
    else:
        return getGame(userData=userData, id=id)

@games.route("/game/offerTrade", methods=['PUT'])
def offertrade():
    """
       need input parameters:
           selected card (value is unique)
           (player, currentPlayer)
    """
    req = request.get_json()
    id = req['id']
    userData = getUserData(req)
    tile = req['tile']
    money = req['money']
    opponentName = req['opponentName']
    error = offerTrade(id, money, tile, opponentName, userData['name'])
    if error:
        return error
    else:
        return getGame(userData=userData, id=id)

@games.route("/game/buyLuxuryTile", methods=['PUT'])
def buyluxurytile():
    """
       need input parameters:
           selected tile
           (player, currentPlayer)
    """
    req = request.get_json()
    id = req['id']
    tile = req['tile']
    userData = getUserData(req)
    error = buyLuxuryTile(id, tile, userData['name'])
    if error:
        return error
    else:
        return getGame(userData=userData, id=id)


@games.route("/game/selectCardToDiscard", methods=['PUT'])
def selectcardtodiscard():
    """
       need input parameters:
           selected card (value is unique)
           (player, currentPlayer)
    """
    req = request.get_json()
    id = req['id']
    value = req['value']
    userData = getUserData(req)
    error = selectCardToDiscard(id, value, userData['name'])
    if error:
        return error
    else:
        return getGame(userData=userData, id=id)

@games.route("/game/discardTile", methods=['PUT'])
def discardtile():
    """
       need input parameters:
           selected card (value is unique)
           (player, currentPlayer)
    """
    req = request.get_json()
    id = req['id']
    tile = req['tile']
    userData = getUserData(req)
    error = discardTile(id, tile, userData['name'])
    if error:
        return error
    else:
        return getGame(userData=userData, id=id)
