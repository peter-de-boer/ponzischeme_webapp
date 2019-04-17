import jsonpickle
from flask import jsonify, Blueprint, request
from backend.games.gameIO import *
from backend.games.gameActions import *
from backend.games.game import Game

from backend import Session
from backend.models import User, GameModel


games = Blueprint('games', __name__)

def getUser(req):
    token = None
    if 'token' in req:
        token = req['token']
    session = Session()
    user=User.verify_token(token)
    if user and user.confirmed:
        return user
    else:
        return None

def getUserData(req):
    userData = {"name": None, "id": None }
    user = getUser(req)
    if user:
        userData = {"name": user.username, "id": user.id}
    return userData

@games.route("/gameList", methods=['PUT'])
def gamelist():
    req = request.get_json()
    userData = getUserData(req)
    return gameList(userData)

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


def returnData(userData, error, id):
    if error:
        return json.dumps([userData, error])
    else:
        game, chat, notes = getGame(userData=userData, id=id)
        return json.dumps([userData, json.loads(game), json.loads(chat), notes])


@games.route("/game", methods=['GET','PUT'])
def get_game():
    req = request.get_json()
    userData = getUserData(req)
    id = req['id']
    #return getGame(userData=userData, id=id)
    #need to loads and dumps to keep correct json format
    return returnData(userData, None, id)
    #return json.dumps([userData, json.loads(getGame(userData=userData, id=id))])

@games.route("/game/chat", methods=['PUT'])
def post():
    req = request.get_json()
    userData = getUserData(req)
    id = req['id']
    post = req['post']
    error = addPost(post, id, userData['name'])
    return returnData(userData, error, id)

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
    #error = selectTileAndCard(id, value, tile, userData['name'])
    kwargs = {'value': value, 'tile': tile, 'name': userData['name']}
    error = executeAction("selectTileAndCard", id, **kwargs)
    return returnData(userData, error, id)

@games.route("/game/passFunding", methods=['PUT'])
def passfunding():
    """
       need input parameters:
           (player, currentPlayer)
    """
    req = request.get_json()
    id = req['id']
    userData = getUserData(req)
    #error = passFunding(id, userData['name'])
    kwargs = {'name': userData['name']}
    error = executeAction("passFunding", id, **kwargs)
    return returnData(userData, error, id)

@games.route("/game/passTrading", methods=['PUT'])
def passtrading():
    """
       need input parameters:
           (player, currentPlayer)
    """
    req = request.get_json()
    id = req['id']
    userData = getUserData(req)
    #error = passTrading(id, userData['name'])
    kwargs = {'name': userData['name']}
    error = executeAction("passTrading", id, **kwargs)
    return returnData(userData, error, id)

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
    #error = buyTrade(id, userData['name'])
    kwargs = {'name': userData['name']}
    error = executeAction("buyTrade", id, **kwargs)
    return returnData(userData, error, id)

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
    #error = sellTrade(id, userData['name'])
    kwargs = {'name': userData['name']}
    error = executeAction("sellTrade", id, **kwargs)
    return returnData(userData, error, id)

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
    #error = offerTrade(id, money, tile, opponentName, userData['name'])
    kwargs = {'money': money, 'tile': tile, 'opponentName': opponentName, 'name': userData['name']}
    error = executeAction("offerTrade", id, **kwargs)
    return returnData(userData, error, id)

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
    #error = buyLuxuryTile(id, tile, userData['name'])
    kwargs = {'tileIndex': tile, 'name': userData['name']}
    error = executeAction("buyLuxuryTile", id, **kwargs)
    return returnData(userData, error, id)


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
    #error = selectCardToDiscard(id, value, userData['name'])
    kwargs = {'value': value, 'name': userData['name']}
    error = executeAction("selectCardToDiscard", id, **kwargs)
    return returnData(userData, error, id)

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
    #error = discardTile(id, tile, userData['name'])
    kwargs = {'tile': tile, 'name': userData['name']}
    error = executeAction("discardTile", id, **kwargs)
    return returnData(userData, error, id)
