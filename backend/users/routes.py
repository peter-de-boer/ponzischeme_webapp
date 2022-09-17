from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from backend import Session # db # , bcrypt
from backend.models import User #, Post
#from backend.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
#                                   RequestResetForm, ResetPasswordForm)
from backend.users.utils import send_reset_email, send_registration_email
import json

users = Blueprint('users', __name__)

def exists_email(email):
    user = Session.query(User).filter_by(email=email).first()
    return user

def exists_username(username):
    user = Session.query(User).filter_by(username=username).first()
    return user

def getUserByPassword(req, salt=None, onlyIfConfirmed=True):
    username = None
    if 'username' in req:
        username = req['username']
    password = None
    if 'password' in req:
        password = req['password']
    if username and password:
        session = Session()
        user = Session.query(User).filter_by(username=username).first()
        if (user and user.check_password(password)):
            if (onlyIfConfirmed and not user.confirmed):
                return None
            else:
                return user
        else:
            return None
    else:
        return None

def getUserByToken(req, salt=None, onlyIfConfirmed=True):
    token = None
    if 'token' in req:
        token = req['token']
    session = Session()
    user=User.verify_token(token,salt)
    if (onlyIfConfirmed and not (user and user.confirmed)):
        return None
    else:
        return user

@users.route("/user/request_confirm_email", methods=['POST'])
def requestconfirmemail():
    session = Session()
    req = request.get_json()
    email = req['email']
    #password = req['password']
    #username = req['username']
    url = req['url']
    data = {}
    user = Session.query(User).filter_by(email=email).first()
    if not user:
        data['status'] = 'failed'
    else:
        send_registration_email(user, url)
        data['status'] = 'success'
    json_data = json.dumps(data)
    return json_data

@users.route("/user/request_reset_password", methods=['POST'])
def requestresetpassword():
    session = Session()
    req = request.get_json()
    email = req['email']
    #password = req['password']
    #username = req['username']
    url = req['url']
    data = {}
    user = Session.query(User).filter_by(email=email).first()
    if not user:
        data['status'] = 'failed'
    else:
        send_reset_email(user, url)
        data['status'] = 'success'
    json_data = json.dumps(data)
    return json_data

@users.route("/user/reset_password", methods=['POST'])
def resetpassword():
    session = Session()
    req = request.get_json()
    user=getUserByToken(req,salt='reset', onlyIfConfirmed=False)
    data = {}
    if user:
        data['status'] = 'reset_password'
        data['token'] = req['token']
    else:
        data['status'] = 'failed'
    json_data = json.dumps(data)
    return json_data

@users.route("/user/signup", methods=['POST'])
def signup():
    session = Session()
    req = request.get_json()
    email = req['email']
    password = req['password']
    username = req['username']
    url = req['url']
    data = {}
    if exists_email(email):
        data['status'] = 'email_exists'
    elif exists_username(username):
        data['status'] = 'username_exists'
    else:
        user = User(username=username, email=email, password=password)
        session.add(user)
        # now first commit before sending email, else the new user has no id
        # yet...
        session.commit()
        send_registration_email(user, url)
        data['status'] = 'success'
    json_data = json.dumps(data)
    return json_data

@users.route("/user/change_password", methods=['POST'])
def changepassword():
    session = Session()
    req = request.get_json()
    user=getUserByToken(req,salt='reset', onlyIfConfirmed=False)
    data = {}
    if not user:
        data['status'] = 'failed'
    else:
        password = req['password']
        user.set_password(password)
        data['status'] = 'changed'
        session.commit()
    json_data = json.dumps(data)
    return json_data


@users.route("/user/confirm", methods=['POST'])
def confirm():
    session = Session()
    req = request.get_json()
    user=getUserByToken(req,salt='registration', onlyIfConfirmed=False)
    data = {}
    if user:
        user.confirmed = True
        session.commit()
        data['status'] = 'confirmed'
    else:
        data['status'] = 'not confirmed'
    json_data = json.dumps(data)
    return json_data


@users.route("/user/login", methods=['GET', 'POST'])
def login():
    session = Session()
    req = request.get_json()
    user=getUserByPassword(req,salt=None)
    data = {}
    if (user):
        data['status'] = 'authenticated'
        data['idToken'] = user.get_token()
        data['username'] = user.username
    else:
        data['status'] = 'failed'
    json_data = json.dumps(data)
    return json_data


@users.route("/user/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/user/account", methods=['PUT'])
def account():
    print("NOW IN  /user/account")
    session = Session()
    req = request.get_json(force=True)
    user = getUserByToken(req,salt=None)
    data = {}
    if (user):
        data['email'] = user.email
        data['status'] = 'success'
    else:
        data['status'] = 'failed'
    json_data = json.dumps(data)
    return json_data


