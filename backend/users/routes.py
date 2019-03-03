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

def getUser(req):
    token = None
    if 'token' in req:
        token = req['token']
    session = Session()
    user=User.verify_token(token,salt='registration')
    return user

@users.route("/user/signup", methods=['POST'])
def signup():
    session = Session()
    req = request.get_json()
    print(req)
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
    print("req: ", req)
    user=getUser(req)
    print("user: ", user)
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
    password = req['password']
    username = req['username']
    data = {}
    user = session.query(User).filter_by(username=username).first()
    if (user and user.check_password(password) and user.confirmed):
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


@users.route("/user/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)


@users.route("/user/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route("/user/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        #hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        hashed_password = generate_password_hash(form.password.data)
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
