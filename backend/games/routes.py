from flask import jsonify, Blueprint


games = Blueprint('games', __name__)


@games.route("/", methods=['GET'])
def get_def():
    return jsonify(game_id=2,
                   player1 = "no game")

@games.route("/game", methods=['GET'])
def get_game():
    return jsonify(game_id=1,
                   player1 = "peter")
