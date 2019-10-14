import json, jsonpickle
from backend.games.game import Game
from backend.models import GameModel, User, Notes, ChatModel
from backend import Session
from backend.users.utils import send_notification, send_end_of_game_email


def addMainPost(post, name, timestamp=None):
    session = Session()
    chatmodel = session.query(ChatModel).first()
    chat = jsonpickle.decode(chatmodel.chat)
    if (chat is None):
        chat = []
    fullPost = [name, post, timestamp]
    chat.append(fullPost)
    chatmodel.chat = jsonpickle.encode(chat)
    session.commit()
    session.close()
    return None

def getMainChat():
    session = Session()
    chatmodel = session.query(ChatModel).first()
    chat = chatmodel.chat
    session.close()
    return chat
