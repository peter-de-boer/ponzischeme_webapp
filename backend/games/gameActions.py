import json, jsonpickle
from backend.games.game import Game
from backend.games.gameIO import writeGame, readGame
from backend.models import GameModel, User
from backend import Session
from backend.users.utils import send_notification, send_end_of_game_email

"""
all very similor methods
could probably  simplify by putting most of it in a single method
and then pass methods as argument
"""

def execute(gm, method, **kwargs):
    # need to do a mapping of method string to Game class method
    if method=="selectTileAndCard":
        return gm.selectTileAndCard(**kwargs)
    elif method=="passFunding":
        return gm.passFunding(**kwargs)
    elif method=="passTrading":
        return gm.passTrading(**kwargs)
    elif method=="sellTrade":
        return gm.sellTrade(**kwargs)
    elif method=="buyTrade":
        return gm.buyTrade(**kwargs)
    elif method=="offerTrade":
        return gm.offerTrade(**kwargs)
    elif method=="buyLuxuryTile":
        return gm.buyLuxuryTile(**kwargs)
    elif method=="selectCardToDiscard":
        return gm.selectCardToDiscard(**kwargs)
    elif method=="discardTile":
        return gm.discardTile(**kwargs)

def executeAction(method, id, **kwargs):
    session = Session()
    game = session.query(GameModel) \
            .filter(GameModel.id==id).first()
    gm = jsonpickle.decode(game.game)
    error = execute(gm, method, **kwargs)
    if error:
        session.close()
        return error
    else:
        game.game = jsonpickle.encode(gm)
        if gm.status.endOfGame:
            game.status = "finished"
            game.active = None
            emails = [player.email for player in game.players]
            send_end_of_game_email(emails, id)
        else:
            activePlayer = gm.getActivePlayer()
            active = session.query(User) \
                    .filter(User.id==activePlayer.id).first()
            game.active = active
            if (active.username != kwargs['name']):
                send_notification(active, id)
        session.commit()
        session.close()
        return None

def addPost(post, id, name):
    session = Session()
    game = session.query(GameModel) \
            .filter(GameModel.id==id).first()
    chat = jsonpickle.decode(game.chat)
    if (chat is None):
        chat = []
    fullPost = name + ": " + post
    chat.append(fullPost)
    game.chat = jsonpickle.encode(chat)
    session.commit()
    session.close()
    return None
