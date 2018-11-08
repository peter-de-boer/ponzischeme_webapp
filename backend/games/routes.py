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

@games.route("/game/selectCard", methods=['PUT'])
def selectcard():
    req = request.get_json()
    value = req['value']
    selectCard(value)
    """
       need input parameters:
           selected card (value is unique),
           (player, currentPlayer)
    """
    return readGameJSON()
