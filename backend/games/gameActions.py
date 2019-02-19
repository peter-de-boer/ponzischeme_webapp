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

def selectTileAndCard(id, value, tile, name):
    session = Session()
    game = session.query(GameModel) \
            .filter(GameModel.id==id).first()
    gm = jsonpickle.decode(game.game)
    error = gm.selectTileAndCard(value, tile, name)
    if error:
        session.close()
        return error
    else:
        game.game = jsonpickle.encode(gm)
        activePlayer = gm.getActivePlayer()
        active = session.query(User) \
                .filter(User.id==activePlayer.id).first()
        game.active = active
        session.commit()
        session.close()
        return None

def passFunding(id, name):
    session = Session()
    game = session.query(GameModel) \
            .filter(GameModel.id==id).first()
    gm = jsonpickle.decode(game.game)
    error = gm.passFunding(name)
    if error:
        session.close()
        return error
    else:
        game.game = jsonpickle.encode(gm)
        activePlayer = gm.getActivePlayer()
        active = session.query(User) \
                .filter(User.id==activePlayer.id).first()
        game.active = active
        session.commit()
        session.close()
        return None

def passTrading(id, name):
    session = Session()
    game = session.query(GameModel) \
            .filter(GameModel.id==id).first()
    gm = jsonpickle.decode(game.game)
    error = gm.passTrading(name)
    if error:
        session.close()
        return error
    else:
        game.game = jsonpickle.encode(gm)
        activePlayer = gm.getActivePlayer()
        active = session.query(User) \
                .filter(User.id==activePlayer.id).first()
        game.active = active
        session.commit()
        session.close()
        return None

def sellTrade(id, name):
    session = Session()
    game = session.query(GameModel) \
            .filter(GameModel.id==id).first()
    gm = jsonpickle.decode(game.game)
    error = gm.sellTrade(name)
    if error:
        session.close()
        return error
    else:
        game.game = jsonpickle.encode(gm)
        activePlayer = gm.getActivePlayer()
        active = session.query(User) \
                .filter(User.id==activePlayer.id).first()
        game.active = active
        session.commit()
        session.close()
        return None

def buyTrade(id, name):
    session = Session()
    game = session.query(GameModel) \
            .filter(GameModel.id==id).first()
    gm = jsonpickle.decode(game.game)
    error = gm.buyTrade(name)
    if error:
        session.close()
        return error
    else:
        game.game = jsonpickle.encode(gm)
        activePlayer = gm.getActivePlayer()
        active = session.query(User) \
                .filter(User.id==activePlayer.id).first()
        game.active = active
        session.commit()
        session.close()
        return None

def offerTrade(id, money, tile, opponentName, name):
    session = Session()
    game = session.query(GameModel) \
            .filter(GameModel.id==id).first()
    gm = jsonpickle.decode(game.game)
    error = gm.offerTrade(money, tile, opponentName, name)
    if error:
        session.close()
        return error
    else:
        game.game = jsonpickle.encode(gm)
        activePlayer = gm.getActivePlayer()
        active = session.query(User) \
                .filter(User.id==activePlayer.id).first()
        game.active = active
        session.commit()
        session.close()
        return None

def buyLuxuryTile(id, tile, name):
    session = Session()
    game = session.query(GameModel) \
            .filter(GameModel.id==id).first()
    gm = jsonpickle.decode(game.game)
    error = gm.buyLuxuryTile(tile, name)
    if error:
        session.close()
        return error
    else:
        game.game = jsonpickle.encode(gm)
        activePlayer = gm.getActivePlayer()
        active = session.query(User) \
                .filter(User.id==activePlayer.id).first()
        game.active = active
        session.commit()
        session.close()
        return None

def selectCardToDiscard(id, value, name):
    session = Session()
    game = session.query(GameModel) \
            .filter(GameModel.id==id).first()
    gm = jsonpickle.decode(game.game)
    error = gm.selectCardToDiscard(value, name)
    if error:
        session.close()
        return error
    else:
        game.game = jsonpickle.encode(gm)
        activePlayer = gm.getActivePlayer()
        active = session.query(User) \
                .filter(User.id==activePlayer.id).first()
        game.active = active
        session.commit()
        session.close()
        return None

def discardTile(id, tile, name):
    session = Session()
    game = session.query(GameModel) \
            .filter(GameModel.id==id).first()
    gm = jsonpickle.decode(game.game)
    error = gm.discardTile(tile, name)
    if error:
        session.close()
        return error
    else:
        game.game = jsonpickle.encode(gm)
        activePlayer = gm.getActivePlayer()
        active = session.query(User) \
                .filter(User.id==activePlayer.id).first()
        game.active = active
        session.commit()
        session.close()
        return None

