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

def getUser(req, salt=None):
    token = None
    if 'token' in req:
        token = req['token']
    session = Session()
    user=User.verify_token(token,salt)
    return user

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

@users.route("/user/confirm", methods=['POST'])
def confirm():
    session = Session()
    req = request.get_json()
    user=getUser(req,salt='registration')
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
    user=getUser(req,salt=None)
    data = {}
    if (user):
        data['status'] = 'authenticated'
        data['idToken'] = user.get_token()
        data['username'] = username
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
    user = getUser(req,salt=None)
    data = {}
    if (user):
        data['email'] = user.email
        data['status'] = 'success'
    else:
        data['status'] = 'failed'
    json_data = json.dumps(data)
    return json_data


