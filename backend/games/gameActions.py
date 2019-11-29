import json, jsonpickle
from backend.games.game import Game
from backend.models import GameModel, User, Notes
from backend import Session
from backend.users.utils import send_notification, send_end_of_game_email
import datetime, time


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
            # removed the condition if the active player is not changed
            # since apparently players do not notice it is still their turn
            # if (active.username != kwargs['name']):
            if True:
                send_notification(active, id)
        session.commit()
        session.close()
        return None

def addPost(post, id, name, timestamp=None):
    # add a new post to the chat
    # if timestamp is not provided, save the current time
    # as UTC, and in iso format for easy handling on frontend
    session = Session()
    game = session.query(GameModel) \
            .filter(GameModel.id==id).first()
    chat = jsonpickle.decode(game.chat)
    if (chat is None):
        chat = []
    if timestamp is None:
        now = datetime.datetime.now(tz=datetime.timezone.utc)
        timestamp = now.isoformat()
    fullPost = [name, post, timestamp]
    chat.append(fullPost)
    game.chat = jsonpickle.encode(chat)
    session.commit()
    session.close()
    return None

def changeNotes(newnotes, name):
    data = {}
    session = Session()
    user_id = newnotes['player_id']
    player = session.query(User) \
            .filter(User.id==user_id).first()
    if (player is None) or (player.username!=name):
        data['error'] = 'user error'
        return data
    id = newnotes['id']
    notes = session.query(Notes) \
            .filter(Notes.id==id).first()
    if notes is None:
        data['error'] = 'notes error'
        return data
    notes.notes = newnotes['notes']
    session.commit()
    session.close()
    return None
