from flask import jsonify, Blueprint
from backend.games.gameIO import readGameJSON


games = Blueprint('games', __name__)


@games.route("/", methods=['GET'])
def get_def():
    return jsonify(game_id=2,
                   player1 = "no game")

@games.route("/game", methods=['GET'])
def get_game():
    return readGameJSON()
    """
    return jsonify(game_id=1,
                   player1 = "peter")
    """
