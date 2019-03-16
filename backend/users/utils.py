
import os
import secrets
#from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from backend import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    #i = Image.open(form_picture)
    #i.thumbnail(output_size)
    #i.save(picture_path)

    return picture_fn

def sendMessage(msg):
    try:
        mail.send(msg)
    except:
        print("message could not be sent")
        print(msg)

def send_reset_email(user, url):
    token = user.get_reset_token()
    link = url + '/reset_password/' + token
    msg = Message('Password Reset Request',
                  sender='peterdb001@gmail.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{link}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    sendMessage(msg)

def send_registration_email(user, url):
    token = user.get_registration_token()
    link = url + '/confirm/' + token
    msg = Message('Confirm your registration',
                  sender='peterdb001@gmail.com',
                  recipients=[user.email])
    msg.body = f'''To confirm your registration, follow the following link:
{link}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    sendMessage(msg)


def send_notification(user, game_id):
    url = os.environ.get('BASE_URL')
    link = url + f'/game/{game_id}'
    print("link: ", link)
    msg = Message(f'[ponzischeme]: your turn in game {game_id}',
                  sender='peterdb001@gmail.com',
                  recipients=[user.email])
    msg.body = f'''It is your turn in game {game_id}:
{link}
'''
    sendMessage(msg)

def send_end_of_game_email(emails, game_id):
    url = os.environ.get('BASE_URL')
    link = url + f'/game/{game_id}'
    msg = Message(f'[ponzischeme]: end of game {game_id}',
                  sender='peterdb001@gmail.com',
                  recipients=emails)
    msg.body = f'''Game {game_id} is finished:
{link}
'''
    sendMessage(msg)

def send_start_game_email(emails, game_id):
    url = os.environ.get('BASE_URL')
    link = url + f'/game/{game_id}'
    msg = Message(f'[ponzischeme]: start of game {game_id}',
                  sender='peterdb001@gmail.com',
                  recipients=emails)
    msg.body = f'''Game {game_id} is started:
{link}
'''
    sendMessage(msg)


def send_ready_game_email(user, game_id):
    url = os.environ.get('BASE_URL')
    link = url
    msg = Message(f'[ponzischeme]: game {game_id} is ready to start',
                  sender='peterdb001@gmail.com',
                  recipients=[user.email])
    msg.body = f'''All seats in game {game_id} are occupied.
You can start the game now:
{link}
'''
    sendMessage(msg)


