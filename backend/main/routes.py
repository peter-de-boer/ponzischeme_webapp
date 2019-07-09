import jsonpickle
from flask import jsonify, Blueprint, request

from backend import Session
from backend.models import User
from backend.main.chat import *

main = Blueprint('main', __name__)



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


def returnData(userData, error):
    if error:
        return json.dumps([userData, error])
    else:
        mainChat= getMainChat()
        return json.dumps([userData, json.loads(mainChat)])


@main.route("/mainchat", methods=['PUT', 'GET'])
def post():
    print("************* mainchat ***************")
    if request.method == 'PUT':
        req = request.get_json()
        userData = getUserData(req)
        post = req['post']
        error = addMainPost(post, userData['name'])
    else:
        req = {}
        req['token'] = request.args.get('token', None)
        userData = getUserData(req)
        error = None
    return returnData(userData, error)

