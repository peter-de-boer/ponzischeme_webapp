import json, jsonpickle
from backend.games.game import Game
from backend.models import GameModel, User, Notes, ChatModel
from backend import Session
from backend.users.utils import send_notification, send_end_of_game_email
import datetime, time


def addMainPost(post, name, timestamp=None):
    # add a new post to the main chat
    # if timestamp is not provided, save the current time 
    # as UTC, and in iso format for easy handling on frontend
    session = Session()
    chatmodel = session.query(ChatModel).first()
    chat = jsonpickle.decode(chatmodel.chat)
    if (chat is None):
        chat = []
    if timestamp is None:
        now = datetime.datetime.now(tz=datetime.timezone.utc)
        timestamp = now.isoformat()
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
