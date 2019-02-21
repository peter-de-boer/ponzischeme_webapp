import json, jsonpickle
from backend.games.game import Game
from backend.games.gameIO import writeGame, readGame
from backend.models import GameModel, User
from backend import Session

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
    print("************* in executeAction *************")
    print(kwargs)
    print(method)
    session = Session()
    game = session.query(GameModel) \
            .filter(GameModel.id==id).first()
    gm = jsonpickle.decode(game.game)
    print("just before method call")
    error = execute(gm, method, **kwargs)
    print("just after method call")
    if error:
        session.close()
        return error
    else:
        game.game = jsonpickle.encode(gm)
        if gm.status.endOfGame:
            game.status = "finished"
            game.active = None
        else:
            activePlayer = gm.getActivePlayer()
            active = session.query(User) \
                    .filter(User.id==activePlayer.id).first()
            game.active = active
        session.commit()
        session.close()
        return None

